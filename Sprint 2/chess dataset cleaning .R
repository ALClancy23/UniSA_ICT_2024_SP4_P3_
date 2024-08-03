# clean up global environment
rm(list = ls())

# Set the working directory
setwd("C:/Users/crews/Dropbox/University/UNISA/202404 INFT3039/Chess Dataset") # to set a new working directory

# Double check that working directory is set
getwd() # to check your current working directory

# Install libraries
library(readr)
library(dplyr)
library(tidyr)

# Load the data
chessdata <- read_csv("200k_blitz_rapid_classical_bullet.csv")

#size of dataset
dim(chessdata)

# # View 1st 6 rows of the control and test data sets
head(chessdata)

# View the structure of the control and test data sets.Variables and their types.
str(chessdata)

# View the summary of variables in the control and test data sets.  
summary(chessdata)

# count total missing or null values 
print("Count of total missing values  ")
sum(is.na(chessdata))

# Drop specific columns not needed
chessdata <- subset(chessdata, select = -c(Index...2,Black,BlackElo,BlackRatingDiff,Event,
                                           Round,Site,White,WhiteElo,WhiteRatingDiff,BlackTitle,
                                           WhiteTitle,Weekday))

# Drop a range of columns not needed
chessdata <- chessdata %>% select(-(Eval_ply_1:Eval_ply_200))

# Rename column 1 to just Index
chessdata <- rename(chessdata,c('Index'='Index...1'))

# Do new count of Null values 
print("Count of total missing values  ")
sum(is.na(chessdata))

# write dataset to csv with new name
write.csv(chessdata, "chessdata.csv", row.names = FALSE)