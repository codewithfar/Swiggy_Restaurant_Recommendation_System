import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder

# load cleaned data
df = pd.read_csv("cleaned_data.csv")

# fix rating_count
df['rating_count'] = df['rating_count'].astype(str)
df['rating_count'] = df['rating_count'].str.replace('+','', regex=False)
df['rating_count'] = df['rating_count'].str.replace(' ratings','', regex=False)
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')

# fix cost column
df['cost'] = df['cost'].astype(str)
df['cost'] = df['cost'].str.replace('₹','', regex=False)
df['cost'] = df['cost'].str.replace(',','', regex=False)
df['cost'] = pd.to_numeric(df['cost'], errors='coerce')

# drop missing
df = df.dropna()

# select required columns
df = df[['city','cuisine','rating','rating_count','cost']]

# reduce dataset size (RAM safe)
df = df.sample(20000, random_state=42)

# encoding
encoder = OneHotEncoder(handle_unknown='ignore')

encoded = encoder.fit_transform(df[['city','cuisine']])

encoded_df = pd.DataFrame(encoded.toarray())

# combine data
final_df = pd.concat(
    [df[['rating','rating_count','cost']].reset_index(drop=True), encoded_df],
    axis=1
)

# save encoded data
final_df.to_csv("encoded_data.csv", index=False)

# save encoder
pickle.dump(encoder, open("encoder.pkl","wb"))

print("Encoding Completed Successfully")