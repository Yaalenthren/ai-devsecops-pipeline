import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

def train_model():
    data = pd.read_csv("data/log_data.csv")

    X = data["log_text"]
    y = data["label"]

    vectorizer = CountVectorizer()
    X_vectorized = vectorizer.fit_transform(X)

    model = LogisticRegression()
    model.fit(X_vectorized, y)

    return model, vectorizer


def predict_log(log_text, model, vectorizer):
    log_vector = vectorizer.transform([log_text])
    prediction = model.predict(log_vector)[0]
    probability = model.predict_proba(log_vector)[0][1]

    return prediction, probability