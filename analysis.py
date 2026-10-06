import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_books_dataset.csv")

print("===== BASIC DATA ANALYSIS =====")

# Total books
print("\nTotal books:", len(df))

# Price analysis
print("\n--- Price Analysis ---")
print("Average price:", round(df["Price"].mean(), 2))
print("Minimum price:", round(df["Price"].min(), 2))
print("Maximum price:", round(df["Price"].max(), 2))

# Rating analysis
print("\n--- Rating Analysis ---")
print("Average rating:", round(df["Rating"].mean(), 2))

print("\nNumber of books by rating:")
print(df["Rating"].value_counts().sort_index())

# Availability analysis
print("\n--- Availability Analysis ---")
print(df["Availability"].value_counts())

# Most expensive books
print("\n--- Top 5 Most Expensive Books ---")
print(df[["Title", "Price"]].sort_values("Price", ascending=False).head(5))

print("\nAnalysis completed successfully!")