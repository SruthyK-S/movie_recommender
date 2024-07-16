import pickle
import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key={YOUR_API_KEY}&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['original_title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    movie_names = []
    movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        movie_posters.append(fetch_poster(movie_id))
        movie_names.append(movies.iloc[i[0]].original_title)

    return movie_names,movie_posters

st.header('Movie Recommendation System')
movies = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['original_title'].values
selected_movie = st.selectbox(
    "Select a movie",
    movie_list
)

if st.button('Show Recommendation'):
    movie_names,movie_posters = recommend(selected_movie)
    col = st.columns(5)
    for i in range(5):
        with col[i]:
            st.text(movie_names[i])
            st.image(movie_posters[i])
    for i in range(5,10):
        with col[i%5]:
            st.text(movie_names[i])
            st.image(movie_posters[i])
