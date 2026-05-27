import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load FAQ data
faq = pd.read_csv("faq.csv")

questions = faq["question"].astype(str).tolist()
answers = faq["answer"].astype(str).tolist()

# Better preprocessing
vectorizer = TfidfVectorizer(
    stop_words='english',
    ngram_range=(1,2)
)

question_vectors = vectorizer.fit_transform(questions)


def get_response(user_input):

    user_input = user_input.lower()

    user_vector = vectorizer.transform([user_input])

    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match = similarity.argmax()

    score = similarity[0][best_match]

    if score < 0.45:
        return "Sorry, I couldn't find a suitable answer."

    return answers[best_match]