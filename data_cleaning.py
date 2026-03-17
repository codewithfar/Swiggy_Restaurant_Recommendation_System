import pandas as pd

# load dataset
df = pd.read_csv("swiggy.csv")

print(df.head())

# remove duplicates
df = df.drop_duplicates()

# remove missing values
df = df.dropna()

# save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("Cleaning Completed")