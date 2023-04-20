import pandas as pd
import matplotlib.pyplot as matplot

#Read in the data from the CSV
DATA = pd.read_csv("Tagged-Data-Final.csv")

def genreCriticScores(option):

    if option == "Mean_Scores":

        genre_data = DATA.groupby("Genre").mean(numeric_only=True)["Critic_Score"].reset_index()
        genre_data = genre_data.sort_values("Critic_Score", ascending=False)

        genre_names = genre_data.Genre
        critic_score = genre_data.Critic_Score

        matplot.bar(genre_names, critic_score)


        matplot.title("Mean Critic Scores of Each Genre")
        matplot.xlabel("Genre")
        matplot.ylabel("Mean Critic Score")

        matplot.show()
    
    if option == "Top_3":
        genre_data = DATA.groupby("Genre").sum(numeric_only=True)["Critic_Score"].reset_index()
        genre_data = genre_data.sort_values("Critic_Score", ascending=False).head(3)

        genre_names = genre_data.Genre
        critic_score = genre_data.Critic_Score

        matplot.bar(genre_names, critic_score)


        matplot.title("Top 3 Genres by Total Critic Score")
        matplot.xlabel("Genre")
        matplot.ylabel("Total Critic Score")

        matplot.show()
    
    if option == "Bottom_3":
        genre_data = DATA.groupby("Genre").sum(numeric_only=True)["Critic_Score"].reset_index()
        genre_data = genre_data.sort_values("Critic_Score", ascending=True).head(3)

        genre_names = genre_data.Genre
        critic_score = genre_data.Critic_Score

        matplot.bar(genre_names, critic_score)


        matplot.title("Bottom 3 Genres by Total Critic Score")
        matplot.xlabel("Genre")
        matplot.ylabel("Total Critic Score")

        matplot.show()
