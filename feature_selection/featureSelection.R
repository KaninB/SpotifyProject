trainData = read.csv("cleaned-edited.csv",stringsAsFactors=FALSE, sep=",")
trainData = trainData[, c('Artist.Followers', 'Danceability', 'Energy', 'Loudness',
                           'Speechiness', 'Acousticness', 'Liveness', 'Tempo', 'Duration_ms',
                           'Valence', 'explicit', 'mode',
                           'instrumentalness', 'time_signature', 'Key', 'class')]
for (i in length(trainData))
{
  if (trainData[i, "explicit"] == "TRUE")
  {
    trainData[i, "explicit"] = 1;
  }
  else
  {
    trainData[i, "explicit"] = 0;
  }
}

head(trainData)

# Used from https://www.machinelearningplus.com/machine-learning/feature-selection/
library(Boruta)

# Perform Boruta search
boruta_output <- Boruta(class ~ ., data = na.omit(trainData), doTrace = 0)

# Do a tentative rough fix
roughFixMod <- TentativeRoughFix(boruta_output)
boruta_signif <- getSelectedAttributes(roughFixMod)
print(boruta_signif)

# Variable Importance Scores
imps <- attStats(roughFixMod)
imps2 = imps[imps$decision != 'Rejected', c('meanImp', 'decision')]
head(imps2[order(-imps2$meanImp), ]) 

# Plot variable importance
plot(boruta_output, cex.axis=.7, las=2, xlab="", main="Variable Importance")  
