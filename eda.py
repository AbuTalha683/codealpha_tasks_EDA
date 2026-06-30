import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books_dataset.csv")

df["Price"] = df["Price"].astype(str)
df["Price"] = df["Price"].str.extract(r'(\d+\.\d+)')
df["Price"] = df["Price"].astype(float)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

plt.figure(figsize=(8,5))
plt.hist(df["Price"], bins=10)

plt.title("Book Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")

plt.savefig("price_distribution.png")
plt.show()