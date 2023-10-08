# Content-based Movie Recommender System

This Python project implements a content-based movie recommendation system. The system analyzes movie data to provide personalized movie recommendations to users. Below are the key features and steps involved in this project:

## Overview

The goal of this project is to predict which movies a user might like based on their past interactions with movies. It uses a content-based recommendation approach, which means it recommends movies similar to those the user has already shown interest in. The similarity between movies is calculated based on their genres, keywords, cast, and crew.

## Dataset

The project uses a dataset sourced from [The Movie Database (TMDb)](https://www.themoviedb.org/), which contains information about thousands of movies. This dataset includes details such as movie titles, genres, keywords, cast, crew, and overviews.

## Implementation Details

The project is implemented in Python and utilizes various libraries and techniques for data preprocessing and recommendation. Here's an overview of the main components:

### Data Preprocessing

- The dataset is cleaned to remove missing values, and duplicates are handled.
- Features like genres, keywords, cast, and crew are processed to extract relevant information for recommendation.
- Text data is stemmed to reduce words to their root form and to improve similarity calculations.
- A count vectorization technique is applied to convert text data into numerical form for machine learning.

### Recommendation Algorithm

- The cosine similarity between movies is calculated based on their textual features (genres, keywords, cast, and crew).
- A Streamlit web application is developed to provide an interactive interface for users to get movie recommendations.

### Web Application (app.py)

- The `app.py` file contains the implementation of a Streamlit web application for users to interact with the recommendation system.
- Users can select a movie for which they want recommendations, and the application displays the top 5 recommended movies along with their posters.
- Movie posters are fetched from 'https://api.themoviedb.org' using movie IDs, enhancing the user experience.
- The recommendation function in `app.py` utilizes the cosine similarity matrix calculated during data preprocessing to recommend movies based on user selections.

## Running the Web Application

To run the Streamlit web application, make sure you have the required libraries installed and execute the `app.py` file. The application will launch in your web browser, allowing you to explore movie recommendations interactively.

This content-based movie recommender system, along with the Streamlit application, is a valuable tool for movie enthusiasts and platforms looking to provide personalized movie recommendations to users based on their preferences.

---

**Note**: 'cosine_pickle.pkl' is not included in the initial commit. To make it work, run jupyter and then run streamlit (app.py)
