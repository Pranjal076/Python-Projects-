# 🎶 Music Playlist Analysis Project
# Author: Pranjal
# Libraries: Pandas, NumPy, Matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load Dataset
df = pd.read_csv("playlist.csv")

# Step 2: Basic Info
print("----- Playlist Overview -----")
print("Total Songs:", df['Song'].nunique())
print("Average Duration (sec):", df['Duration (sec)'].mean())
print("Most Played Song:", df.loc[df['Play Count'].idxmax(), 'Song'])
print("Top Rated Song:", df.loc[df['Rating'].idxmax(), 'Song'])

# Step 3: Genre-wise Analysis
genre_counts = df['Genre'].value_counts()
print("\n----- Songs per Genre -----")
print(genre_counts)

# Plot Genre Distribution
plt.figure(figsize=(8,5))
genre_counts.plot(kind='bar', color='skyblue')
plt.title("Songs per Genre")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

# Step 4: NumPy Calculations
ratings = df['Rating'].to_numpy()
play_counts = df['Play Count'].to_numpy()

z_scores = (play_counts - np.mean(play_counts)) / np.std(play_counts)
print("\nZ-scores for Play Counts:", z_scores)

# Step 5: Visualization
# Top 10 Songs by Play Count
top10 = df.nlargest(10, 'Play Count')
plt.figure(figsize=(10,5))
plt.bar(top10['Song'], top10['Play Count'], color='orange')
plt.xticks(rotation=45, ha='right')
plt.title("Top 10 Songs by Play Count")
plt.ylabel("Play Count")
plt.show()

# Average Duration by Genre
avg_duration = df.groupby('Genre')['Duration (sec)'].mean()
plt.figure(figsize=(8,5))
avg_duration.plot(kind='bar', color='green')
plt.title("Average Song Duration per Genre")
plt.ylabel("Duration (sec)")
plt.show()

# Step 6: Release Year Trend
yearly_counts = df['Release Year'].value_counts().sort_index()
plt.figure(figsize=(8,5))
yearly_counts.plot(kind='line', marker='o', color='purple')
plt.title("Songs Added by Release Year")
plt.xlabel("Year")
plt.ylabel("Number of Songs")
plt.show()
