# Netflix Data Analysis Project using Pandas

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('netflix_titles.csv')

# Clean the data
df = df.rename(columns={
    'show_id':    'Show_ID',
    'type':       'Type',
    'title':      'Title',
    'country':    'Country',
    'date_added': 'Date_Added',
    'release_year':'Release_Year',
    'rating':     'Rating',
    'listed_in':  'Genre'
})

df['Date_Added'] = pd.to_datetime(df['Date_Added'].str.strip(), errors='coerce')
df['Country'] = df['Country'].fillna('Unknown')
df['Rating']  = df['Rating'].fillna('Not Rated')

# Total Movies vs TV Shows
type_counts = df['Type'].value_counts()
print("Content Type Count:")
print(type_counts)

# Bar chart – Movies vs TV Shows
type_counts.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Movies vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Top 10 countries producing Netflix content
top_countries = df['Country'].str.split(',').str[0].str.strip()
top_countries = top_countries[top_countries != 'Unknown'].value_counts().head(10)

print("\nTop 10 Countries:")
print(top_countries)

# Bar chart – Top 10 Countries
top_countries.plot(kind='bar', color='orange')
plt.title('Top 10 Countries Producing Netflix Content')
plt.xlabel('Country')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Trend – content added per year
df['Year_Added'] = df['Date_Added'].dt.year
yearly = df['Year_Added'].value_counts().sort_index()
yearly = yearly[yearly.index >= 2008]

yearly.plot(figsize=(10, 5), color='green', marker='o')
plt.title('Netflix Content Added Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.grid(True)
plt.tight_layout()
plt.show()
