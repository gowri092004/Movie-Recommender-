# Movie Recommendation System


## Introduction

This project presents a **movie recommendation system** designed to suggest movies to users based on their preferences. By leveraging movie metadata, primarily genres, the system recommends movies similar to the one selected by the user.


## Recommendation Techniques

Recommendation systems typically use two main approaches:

- **Collaborative Filtering:** Utilizes user ratings and interactions to find patterns and suggest movies liked by similar users.
- **Content-Based Filtering:** Uses features of movies such as genres, cast, or description to recommend similar content. This project implements content-based filtering due to lack of user rating data.


## Project Overview

- Built using Python and Streamlit for an interactive, web-based interface.
- Employs content-based filtering using the TMDB 5000 Movies dataset.
- Allows users to select a movie and receive genre-based recommendations.
- Provides a clean, user-friendly UI with smooth animations.


## Dataset

The system uses the TMDB 5000 Movies dataset from Kaggle:  
https://www.kaggle.com/tmdb/tmdb-movie-metadata


## How to Use

1. Clone or download the repository.  
2. Install the necessary Python packages:  
   ```bash
   pip install streamlit pandas scikit-learn
