import pickle
import streamlit as st
import requests #for fetching movie posters

movies_dataframe = pickle.load(open('pickle.pkl','rb'))
movie_names = movies_dataframe['title'].values
cosine_similarity = pickle.load(open('cosine_pickle.pkl','rb'))

st.title('Movie Recommendation System')
movie = st.selectbox('Which movie recommendations would you like to have?', movie_names)

# fetch movie posters from API
def fetch_poster(movie_id):
    # themoviedb.org
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path'] #tmdb image path


def recommendation(movie):
    index = movies_dataframe[movies_dataframe['title'] == movie].index[0]
    similarity = cosine_similarity[index]
    top_5_movies = sorted(list(enumerate(similarity)), reverse=True, key=lambda x: x[1])[1:6]
    movies_recommended = []
    movies_poster = []
    for i in top_5_movies:
        movies_recommended.append(movies_dataframe.iloc[i[0]]['title'])
        #getting poster from TMDB API
        movies_poster.append(fetch_poster(movies_dataframe.iloc[i[0]]['id']))
    return movies_recommended,movies_poster

if st.button('Recommend'):
    recommendations,posters = recommendation(movie)
    col1, col2, col3, col4, col5 = st.columns(5) # 5 recommendations
    # --  try with for loop --
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])

    with col2:
        st.text(recommendations[1])
        st.image(posters[1])

    with col3:
        st.text(recommendations[2])
        st.image(posters[2])

    with col4:
        st.text(recommendations[3])
        st.image(posters[3])

    with col5:
        st.text(recommendations[4])
        st.image(posters[4])