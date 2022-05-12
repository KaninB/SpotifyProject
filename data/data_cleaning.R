#Read in all songs release in 2020-2021
data_2020 <- read.csv("data/songs_2020.csv", header =  TRUE)

#Read in all songs that topped charts in 2020-2021
data_top <- read.csv("data/spotify_top200.csv", header =  TRUE)

#Remove duplicate entries from both data sets
data_2020 <- data_2020[!duplicated(data_2020$name), ]
data_top <- data_top[!duplicated(data_top$Song.Name), ]

#Finding number of similar values
data_2020_matches <- data_2020
data_2020_matches$index <- 1+nrow(data_top):nrow(data_top)+nrow(data_2020_matches)
for(songA in data_top$Song.Name) {
  data_2020_matches <- data_2020_matches[!(data_2020_matches$name == songA),]
}

#Adding class
data_2020_matches$class <- FALSE
data_top$class <- TRUE

#Rename Columns
library(tidyverse)
names(data_2020_matches)[names(data_2020_matches) == "name"] <- "Song.Name"
names(data_2020_matches)[names(data_2020_matches) == "popularity"] <- "Popularity"
names(data_2020_matches)[names(data_2020_matches) == "duration_ms"] <- "Duration_ms"
names(data_2020_matches)[names(data_2020_matches) == "loudness"] <- "Loudness"
names(data_2020_matches)[names(data_2020_matches) == "energy"] <- "Energy"
names(data_2020_matches)[names(data_2020_matches) == "danceability"] <- "Danceability"
names(data_2020_matches)[names(data_2020_matches) == "artists"] <- "Artist"
names(data_2020_matches)[names(data_2020_matches) == "acousticness"] <- "Acousticness"
names(data_2020_matches)[names(data_2020_matches) == "speechiness"] <- "Speechiness"
names(data_2020_matches)[names(data_2020_matches) == "tempo"] <- "Tempo"
names(data_2020_matches)[names(data_2020_matches) == "valence"] <- "Valence"
names(data_2020_matches)[names(data_2020_matches) == "liveness"] <- "Liveness"
names(data_2020_matches)[names(data_2020_matches) == "release_date"] <- "Release.Date"
names(data_2020_matches)[names(data_2020_matches) == "ï..id"] <- "Song.ID"
names(data_2020_matches)[names(data_2020_matches) == "index"] <- "Index"

#Combine Datasets
library(plyr)
data <- rbind.fill(data_top, data_2020_matches)

write.csv(data, "data/cleaned.csv", row.names = FALSE)

y <- rev(c(0.48, 0.48, 0.49, 0.48, 0.49, 0.50, 0.50, 0.51, 0.52, 0.52, 0.51, 0.52, 0.53, 0.52, 0.52, 0.53, 0.53, 0.53))
z <- rev(c(0.29, 0.29, 0.31, 0.30, 0.32, 0.33, 0.33, 0.34, 0.35, 0.34, 0.34, 0.34, 0.34, 0.34, 0.33, 0.32, 0.33, 0.33))
x <- rev(c(0.91, 0.91, 0.91, 0.91, 0.91, 0.91, 0.91, 0.92, 0.92, 0.92, 0.92, 0.92, 0.92, 0.92, 0.92, 0.92, 0.92, 0.92))
mean(y)
mean(x)
mean(z)
a <- seq(0.1, 0.95, by=0.05)
a <- c(a,a,a)
c <- c(rep("acc", length(x)), rep("prec", length(y)), rep("rec",length(z)))
b <- c(x,y,z)
b <- cbind(b,c)
plot(a, x, col="red")
plot(a, y, col="blue")
plot(a, z, col="purple")

library(ggplot2)
b1 = b[,1]
b2 = b[,2]
ggplot() + geom_point(aes(x=a, y=b1, colour = b2)) + labs(x="Training Size", y="Metric Value", colour = "Metric")
