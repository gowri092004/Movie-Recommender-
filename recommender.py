import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:
    def __init__(self, data_path):
        self.movies = pd.read_csv(data_path)
        self._process_genres()
        self._create_similarity()

    def _process_genres(self):
        # Convert JSON-like string into genre names
        self.movies['genres'] = self.movies['genres'].apply(
            lambda x: ' '.join([g['name'] for g in ast.literal_eval(x)])
        )

    def _create_similarity(self):
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.movies['genres'])
        self.similarity = cosine_similarity(tfidf_matrix)

    def recommend(self, movie_title, top_n=5):
        if movie_title not in self.movies['title'].values:
            return []

        index = self.movies[self.movies['title'] == movie_title].index[0]
        scores = list(enumerate(self.similarity[index]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        recommendations = []
        for i in scores[1:top_n + 1]:
            recommendations.append(self.movies.iloc[i[0]]['title'])

        return recommendations
