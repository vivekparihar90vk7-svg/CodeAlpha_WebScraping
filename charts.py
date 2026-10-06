import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_books_dataset.csv")

# 1. Price Distribution
plt.figure(figsize=(8, 5))

plt.hist(df["Price"], bins=20)

plt.title("Book Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.savefig("charts/price_distribution.png")
plt.show()
plt.close()


# 2. Rating Distribution
plt.figure(figsize=(8, 5))

df["Rating"].value_counts().sort_index().plot(kind="bar")

plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("charts/rating_distribution.png")
plt.show()
plt.close()


# 3. Availability
plt.figure(figsize=(8, 5))

df["Availability"].value_counts().plot(kind="bar")

plt.title("Book Availability")
plt.xlabel("Availability")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("charts/availability.png")
plt.show()
plt.close()


print("All charts created successfully!")