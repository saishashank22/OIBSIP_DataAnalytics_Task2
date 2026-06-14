import pandas as pd

# Load Dataset
df = pd.read_csv("AB_NYC_2019.csv")

print("Original Shape:", df.shape)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill name and host_name
df["name"].fillna("Unknown", inplace=True)
df["host_name"].fillna("Unknown", inplace=True)

# Fill reviews_per_month
df["reviews_per_month"].fillna(0, inplace=True)

# Fill last_review
df["last_review"].fillna("Not Reviewed", inplace=True)

# Remove duplicates
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

df.drop_duplicates(inplace=True)

# Standardize column names
df.columns = df.columns.str.lower().str.strip()

# Remove price outliers
Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df["price"] >= lower) & (df["price"] <= upper)]

# Save Cleaned Data
df.to_csv("cleaned_data.csv", index=False)

print("\nFinal Shape:", df.shape)
print("Data Cleaning Completed Successfully!")
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
df["price"].hist(bins=50)
plt.title("Distribution of Airbnb Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.savefig("price_distribution.png")
plt.savefig("price_distribution.png")
plt.close()