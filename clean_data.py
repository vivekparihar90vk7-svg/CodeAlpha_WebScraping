import pandas as pd

# Load the scraped dataset
df = pd.read_csv("books_dataset.csv")

print("Original dataset:")
print(df.info())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Make sure Price is numeric
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Remove rows where Price could not be converted
df = df.dropna(subset=["Price"])

# Make Rating numeric
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

# Remove rows where Rating could not be converted
df = df.dropna(subset=["Rating"])

# Reset row numbers
df = df.reset_index(drop=True)

# Save cleaned dataset
df.to_csv("cleaned_books_dataset.csv", index=False)

print("\nCleaning completed!")
print("Rows after cleaning:", len(df))
print("Columns:", list(df.columns))
print("\nFirst 5 records:")
print(df.head())

print("\nCleaned dataset saved successfully!")