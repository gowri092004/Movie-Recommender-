import streamlit as st
from recommender import MovieRecommender
import time

st.set_page_config(page_title="Movie Recommendation System", layout="wide")

# Gen Z full screen style CSS
genz_full_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

html, body, .main {
    height: 100%;
    margin: 0;
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #8e2de2, #4a00e0);
    color: #fff;
    overflow-x: hidden;
}

/* Streamlit main container */
.css-1d391kg {
    padding: 40px 60px;
    max-width: 100% !important;
}

/* Title */
h1, h2 {
    font-weight: 800;
    color: #ff77ff;
    text-align: center;
    text-shadow: 0 0 15px #ff77ffaa;
}

/* Subtitle */
.stMarkdown p {
    font-weight: 500;
    font-size: 20px;
    color: #e0ccff;
    text-align: center;
    margin-bottom: 40px;
}

/* Selectbox style */
div[role="listbox"] > div {
    border-radius: 12px !important;
    border: 2px solid #ff77ff !important;
    background: #38006b !important;
    color: white !important;
}

/* Button style */
.stButton > button {
    background: linear-gradient(90deg, #ff00cc, #333399);
    color: white;
    font-weight: 700;
    font-size: 22px;
    border-radius: 25px;
    padding: 16px 48px;
    border: none;
    box-shadow: 0 0 20px #ff00cccc;
    transition: all 0.3s ease;
    display: block;
    margin: 30px auto 50px auto;
    cursor: pointer;
    max-width: 350px;
    width: 100%;
}
.stButton > button:hover {
    box-shadow: 0 0 40px #ff00ccff;
    transform: scale(1.05);
}

/* Movie cards */
@keyframes fadeIn {
  from {opacity: 0; transform: translateY(30px);}
  to {opacity: 1; transform: translateY(0);}
}
.fade-in {
  animation: fadeIn 0.7s ease forwards;
  margin: 14px 0;
  padding: 20px 28px;
  border-radius: 20px;
  background: #6a00ffcc;
  box-shadow: 0 10px 30px #8e2de299;
  color: #f3e8ff;
  font-weight: 700;
  font-size: 22px;
  transition: background-color 0.3s ease, transform 0.3s ease;
  cursor: default;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}
.fade-in:hover {
  background: #ff00ccdd;
  color: white;
  transform: scale(1.05);
}
</style>
"""

st.markdown(genz_full_css, unsafe_allow_html=True)

st.title("🎬 Movie Recommendation System")
st.write("Enjoy your Moive Time🍿")


# Load recommender
recommender = MovieRecommender("data/tmdb_5000_movies.csv")

# Movie selection dropdown
movie_list = recommender.movies['title'].values
selected_movie = st.selectbox("Select a Movie", movie_list)

def format_movie_title(movie_title):
    movie_row = recommender.movies[recommender.movies['title'] == movie_title]
    if not movie_row.empty and 'release_date' in movie_row.columns:
        release_date = movie_row.iloc[0]['release_date']
        if release_date:
            year = release_date.split("-")[0]
            return f"{movie_title} ({year})"
    return movie_title

if st.button("Recommend Movies"):
    with st.spinner("Finding recommendations... 🍿"):
        time.sleep(1)
        recommendations = recommender.recommend(selected_movie)

    st.subheader("Recommended Movies:")

    for movie in recommendations:
        formatted_title = format_movie_title(movie)
        st.markdown(f'<div class="fade-in">🎥 {formatted_title}</div>', unsafe_allow_html=True)

        