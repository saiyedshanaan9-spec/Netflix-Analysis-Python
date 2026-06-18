Netflix Data Analysis Project


📝 Objective

To analyze a real-world Netflix dataset using the Pandas library and extract useful insights such as total Movies vs TV Shows, top content-producing countries, and trends of content added over the years.


🛠️ Tools and Libraries


Python 3
Pandas
Matplotlib



📂 Dataset Source

The dataset used is a CSV file named netflix_titles.csv, which contains columns like:


show_id
type
title
director
cast
country
date_added
release_year
rating
duration
listed_in
description



📊 Key Steps

Data Loading:
The dataset was loaded using pandas.read_csv().

Data Cleaning:


Renamed columns for clarity.
Converted date_added strings into datetime format.
Filled missing values in Country and Rating.


Data Analysis:


Counted total Movies and TV Shows.
Found top 10 countries producing Netflix content.
Grouped data by year to analyze content addition trends.


Visualization:


Bar chart of Movies vs TV Shows.
Bar chart of Top 10 Countries by content count.
Line chart showing Netflix content added per year (2008 onwards).



📈 Observations


Netflix has a higher number of Movies compared to TV Shows.
The United States produces the most content on Netflix by a large margin.
A consistent rise in Netflix content additions was observed from 2015 to 2020.
The dataset allows for trend tracking and insights into Netflix's global expansion.



📌 Conclusion

Using Pandas, we efficiently cleaned and analyzed Netflix data to discover meaningful trends and patterns. The project highlights how data science tools can be used for real-world entertainment data analysis and decision-making.


▶️ How to Run


Make sure netflix_titles.csv is in the same folder as NETFLIX_ANALYSIS.py.
Install required libraries:


bash   pip install pandas matplotlib


Run the script:


bash   python NETFLIX_ANALYSIS.py
ShareContentcovid_19_data.csvcsvCOVID_ANALYSIS.py56 linespyREADME.md61 linesmd
