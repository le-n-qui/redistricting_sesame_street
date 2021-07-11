getwd()
df <- read.csv('b1.csv')

library(ggplot2)
library(dplyr)

df1= na.omit(df)

b12020 <- ggplot(df1, aes(x = party, fill=party)) +
  geom_bar()

b12020+labs(x="Party",y="# of Districts",
          title="Number of Districts - Florida 2020")


