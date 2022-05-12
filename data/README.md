## About this Folder

- songs2020.csv -> A csv file containing the raw data from [this Kaggle dataset](https://www.kaggle.com/lehaknarnauli/spotify-datasets?select=tracks.csv)
- spotify_top200.csv -> A csv file containg the raw data from [this Kaggle dataset](https://www.kaggle.com/sashankpillai/spotify-top-200-charts-20202021)
- data_cleaning.R -> This R script can be (and was) ran on songs2020.csv and spotify_top200.csv to combine and clean the datasets so they could be put in the cleaned.csv file.
- cleaned.csv -> A cleaned version of the two datasets above. All data mining/analysis tasks should be done on this dataset for this project.
- cleaned-edited.csv -> Contains all values missing from the cleaned.csv
- gatherData.py -> Python program that collects the data found in cleaned-edited.csv missing from cleaned.csv
- config.cfg -> Contains user credentials for Spotipy to collect the data from the Spotify API
