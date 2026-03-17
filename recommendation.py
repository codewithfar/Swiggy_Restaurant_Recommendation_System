import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# load datasets
cleaned = pd.read_csv("cleaned_data.csv")
encoded = pd.read_csv("encoded_data.csv")

def recommend(index):

    # get selected restaurant vector
    restaurant_vector = encoded.iloc[index].values.reshape(1, -1)

    # compute similarity with all restaurants
    similarity = cosine_similarity(restaurant_vector, encoded)[0]

    # sort similarity scores
    scores = list(enumerate(similarity))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # top 5 recommendations
    scores = scores[1:6]

    restaurant_index = [i[0] for i in scores]

    return cleaned.iloc[restaurant_index][['name','city','cuisine','rating','cost']]