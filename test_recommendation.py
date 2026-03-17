import pandas as pd
from recommendation import recommend

df = pd.read_csv("cleaned_data.csv")

# test with first restaurant
print(recommend(0))