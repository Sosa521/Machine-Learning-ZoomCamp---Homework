import pandas as pd

# Load dataset
df = pd.read_csv("data-week-3.csv")

print("\n=== ORIGINAL COLUMNS ===")
print(df.columns.tolist())

# Normalize column names, same as in train.py
df.columns = df.columns.str.lower().str.replace(" ", "_")

print("\n=== NORMALIZED COLUMNS ===")
print(df.columns.tolist())

print("\n=== SHAPE ===")
print(df.shape)

print("\n=== FIRST ROWS ===")
print(df.head())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== CHURN COLUMN CHECK BEFORE CLEANING ===")
print("Unique values:")
print(df["churn"].unique())

print("\nValue counts:")
print(df["churn"].value_counts(dropna=False))

# Clean categorical columns
categorical_columns = list(df.dtypes[df.dtypes == "object"].index)

for c in categorical_columns:
    df[c] = df[c].str.lower().str.replace(" ", "_")

print("\n=== CHURN COLUMN CHECK AFTER CLEANING ===")
print("Unique values:")
print(df["churn"].unique())

print("\nValue counts:")
print(df["churn"].value_counts(dropna=False))

# Convert churn to 0/1
df["churn"] = (df["churn"] == "yes").astype(int)

print("\n=== CHURN COLUMN AFTER CONVERSION ===")
print(df["churn"].value_counts(dropna=False))

print("\n=== SAMPLE ROWS ===")
print(df[["customerid", "churn"]].head(20))