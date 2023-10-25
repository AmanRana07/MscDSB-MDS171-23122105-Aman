# All the use full Resources For the Project
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud
import seaborn as sns

# Here it read the Excel File
data = pd.read_excel("CAC.xlsx")


# this function for checking gender of male and female we getting a response
def plot_gender_distribution():
    # count the gender
    gender_counts = data["Gender"].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(
        gender_counts, labels=gender_counts.index, autopct="%1.1f%%", startangle=140
    )
    plt.title("Gender Distribution")
    plt.show()


def plot_yearwise_registration():
    yes_data = data[data["Are part of any extra-curricular activities?"] == "Yes"]

    # Calculate year-wise registration counts for "Yes" responses
    year_counts = yes_data["Year"].value_counts().sort_index()

    plt.figure(figsize=(8, 4))
    plt.bar(year_counts.index, year_counts.values)
    plt.title("Year-wise Interest of Students in Extra-curricular Activities")
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.show()


# displaying Most Likable Tings in the inter-college events?
def plot_sports_management_opinion():
    # skip the empty values
    suggestions = data[
        "What things do you like most about the inter-college events?"
    ].dropna()
    suggestion_text = " ".join(suggestions)
    # count Value To make all the word Capital so don't come repeated value
    suggestion_counts = suggestions.str.capitalize().value_counts().head(5)

    if suggestion_counts.empty:
        print("No suggestions available.")
        # Printing Most likable Things
    else:
        print("Top 5 Likable Things in inter-college events:")
        # looping the Value in suggestion Count
        for i, (suggestion, count) in enumerate(suggestion_counts.items(), start=1):
            print(f"{i}. {suggestion}: {count} votes")
            print("=" * 40)

    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(
        suggestion_text
    )
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Likable Things in inter-college events")
    plt.show()
    # Visualizing This in Bar Graph
    plt.figure(figsize=(10, 6))
    plt.bar(suggestion_counts.index, suggestion_counts.values, color="skyblue")
    plt.title("Top 5 Likable Things in inter-college events:")
    plt.xlabel("Suggestions")
    plt.ylabel("Number of Votes")
    plt.xticks(rotation=15, ha="right")
    plt.tight_layout()
    plt.show()


# Plotting Review Given By the Tudents
def plot_sports_management_ratings():
    ratings = data["How much would you rate Christ's sports management?"]
    plt.figure(figsize=(8, 4))
    plt.hist(ratings, bins=5, edgecolor="k")
    plt.title("Ratings for Christ's Sports Management")
    plt.xlabel("Rating")
    plt.ylabel("Count")

    # Calculating Mean
    mean_rating = np.mean(ratings)

    # Add a vertical line at the mean
    plt.axvline(  # This is For Vertical line Create to Display Mean
        mean_rating,
        color="red",
        linestyle="dashed",
        linewidth=2,
        label=f"Mean: {mean_rating:.2f}",
    )
    plt.legend()
    plt.show()


# Displaying Sports Which Sports Mostly played By the Different Gender
def prefered_sports_by_gender():
    data_filtered = data.dropna(subset=["Which sport do you like to play?"])

    # Create a grouped bar chart to show preferred sports by gender
    plt.figure(figsize=(10, 6))
    # Groung the Two Data
    sns.countplot(
        data=data_filtered,
        x="Which sport do you like to play?",
        hue="Gender",
        palette={"Male": "blue", "Female": "pink"},
    )
    plt.title("Preferred Sports by Gender")
    plt.xlabel("Sport")
    plt.ylabel("Count")
    plt.xticks(rotation=90)
    plt.legend(title="Gender")
    plt.show()


def plot_management_by_gender():
    gender_management_counts = (
        data.groupby(
            [
                "Gender",
                "How to do you feel about the management of leagues and inter college events?",
            ]
        )
        .size()
        .unstack()
        .fillna(0)
    )
    gender_management_counts.plot(kind="bar", figsize=(10, 6))
    plt.title("Management of Leagues and Inter College Events by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.legend(title="Opinion")
    plt.show()


# Displaying Which Department giving more rating
def plot_rating_by_department():
    # Filter the Data Rename the Repeated Value so it count only ine time
    department_mapping = {
        "MSc Data Science": "Msc Data Science",
        "BCOM": "BCom",
        "B Com": "BCom",
        "Bcom": "BCom",
    }
    # replace the
    data["Department"] = data["Department"].replace(department_mapping)
    # Taking to Coluraph
    ratings_by_department = (
        data.groupby("Department")[
            "How much would you rate Christ's sports management?"
        ]
        .mean()
        .sort_values()
    )

    df = pd.DataFrame(
        {
            "Department": ratings_by_department.index,
            "Mean Rating": ratings_by_department.values,
        }
    )

    # Create an interactive grouped bar chart using Plotly Express
    fig = px.bar(
        df,
        x="Department",
        y="Mean Rating",
        title="Average Rating by Department",
        text="Mean Rating",
    )

    fig.update_traces(
        texttemplate="%{text:.2f}", textposition="outside", marker_color="skyblue"
    )

    fig.show()


# dipplaing a Top % suggestions


def display_top_suggestions():
    suggestions = data["Things you would like to be improved?"].dropna()
    suggestion_text = " ".join(suggestions)
    # counting the only top 5
    suggestion_counts = suggestions.value_counts().head(5)
    # check it the rows are empty not
    if suggestion_counts.empty:
        print("No suggestions available.")
    else:
        print("Top 5 Suggestions:")
        for i, (suggestion, count) in enumerate(suggestion_counts.items(), start=1):
            print(f"{i}. {suggestion}: {count} votes")
            print("=" * 40)
        fig = px.sunburst(
            names=suggestion_counts.index,
            parents=["Top 5 Suggestions"] * len(suggestion_counts.index),
            values=suggestion_counts.values,
            title="Top 5 Suggestions to Improve Sports in Christ",
        )
        fig.show()

        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(
            suggestion_text
        )
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title("Suggestions to Improve Sports in Christ")
        plt.show()


def plot_yearwise_ratings():
    # Assuming you have a 'Year' and 'How much would you rate Christ's sports management?' columns
    year_ratings = (
        data.groupby("Year")["How much would you rate Christ's sports management?"]
        .mean()
        .reset_index()
    )

    # Creating a time series line plot
    fig = px.line(
        year_ratings,
        x="Year",
        y="How much would you rate Christ's sports management?",
        title="Year-wise Ratings for Christ's Sports Management",
    )

    fig.update_traces(mode="lines+markers")
    fig.update_layout(xaxis_title="Year", yaxis_title="Average Rating")
    fig.show()


# graph for gender wise department displaying


def plot_gender_by_department():
    department_mapping = {
        "MSc Data Science": "Msc Data Science",
        "BCOM": "BCom",
        "B Com": "BCom",
        "Bcom": "BCom",
    }
    data["Department"] = data["Department"].replace(department_mapping)

    department_gender_counts = (
        data.groupby(["Department", "Gender"]).size().unstack().fillna(0)
    )

    # Create a stacked bar chart
    department_gender_counts.reset_index(inplace=True)
    fig = px.bar(
        department_gender_counts,
        x="Department",
        y=["Female", "Male"],
        barmode="stack",
        # color_discrete_map={"Female": "pink", "Male": "blue"},
    )

    fig.update_layout(
        title="Gender Distribution by Department",
        xaxis_title="Department",
        yaxis_title="Count",
    )
    fig.show()


# Displaying Which Gender involve in sports or not
def gender_wise_involvement_in_sports():
    yes_data = data[data["Are part of any extra-curricular activities?"] == "Yes"]

    male_yes_count = yes_data[yes_data["Gender"] == "Male"].shape[0]
    female_yes_count = yes_data[yes_data["Gender"] == "Female"].shape[0]

    # Create a pie chart
    labels = ["Male", "Female"]
    counts = [male_yes_count, female_yes_count]
    # colors = ["blue", "pink"]
    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("How many Males And Females are involved in Sports")
    plt.show()


def plot_preferred_sports():
    preferred_sports_counts = data["Which sport do you like to play?"].value_counts()

    # Creating a horizontal bar chart
    plt.figure(figsize=(10, 6))
    preferred_sports_counts.plot(kind="barh", color="skyblue")
    plt.title("Preferred Sports by Students")
    plt.xlabel("Count")
    plt.ylabel("Sport")
    plt.show()


# here it created a Menu Driven For My Program

while True:
    print("Menu:")
    print("1. Gender Distribution")
    print("2. Year-wise Interest of Students in Extra-curricular Activities")
    print("3. Most Likable things in Inter College Event")
    print("4. Ratings for Christ's Sports Management")
    print("5. Preferred Sports by Gender")
    print("6. Management of Leagues and Inter College Events by Gender")
    print("7. Average Rating By department")
    print("8. Top 5 Suggestion from Students to Improve Sports in Christ")
    print("9. Average YearWise Rating")
    print("10. Gender Distribution by Department")
    print("11. Involvement in Sports by Male and Females")
    print("12. Preferred Sports by Students")
    print("13. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        plot_gender_distribution()
    elif choice == "2":
        plot_yearwise_registration()
    elif choice == "3":
        plot_sports_management_opinion()
    elif choice == "4":
        plot_sports_management_ratings()
    elif choice == "5":
        prefered_sports_by_gender()
    elif choice == "6":
        plot_management_by_gender()
    elif choice == "7":
        plot_rating_by_department()
    elif choice == "8":
        display_top_suggestions()
    elif choice == "9":
        plot_yearwise_ratings()
    elif choice == "10":
        plot_gender_by_department()
    elif choice == "11":
        gender_wise_involvement_in_sports()
    elif choice == "12":
        plot_preferred_sports()

    elif choice == "13":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice!! Please select a valid option.")
