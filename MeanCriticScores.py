import pandas as pd
import matplotlib.pyplot as matplot

#Read in the data from the CSV
DATA = pd.read_csv("Tagged-Data-Final.csv")

def MeanCriticScores():
    publisher_data = DATA.groupby("Genre").mean(numeric_only=True)["Critic_Score"].reset_index()
    publisher_data = publisher_data.sort_values("Critic_Score", ascending=False)

    genre_names = publisher_data.Genre
    critic_score = publisher_data.Critic_Score

    matplot.bar(genre_names, critic_score)


    matplot.title("Mean Critic Scores of Each Genre")
    matplot.xlabel("Genres")
    matplot.ylabel("Critic Scores")

    matplot.show()
#
