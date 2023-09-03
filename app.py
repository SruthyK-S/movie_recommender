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
    url = "https://api.themoviedb.org/3/movie/{}?api_key=5f734f1803d88471b1eeb4587c834162&language=en-US".format(movie_id)
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
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.text(movie_names[0])
        st.image(movie_posters[0])
    with col2:
        st.text(movie_names[1])
        st.image(movie_posters[1])
    with col3:
        st.text(movie_names[2])
        st.image(movie_posters[2])
    with col4:
        st.text(movie_names[3])
        st.image(movie_posters[3])
    with col5:
        st.text(movie_names[4])
        st.image(movie_posters[4])
    
    col6, col7, col8, col9, col10 = st.columns(5)

    with col6:
        st.text(movie_names[5])
        st.image(movie_posters[5])
    with col7:
        st.text(movie_names[6])
        st.image(movie_posters[6])
    with col8:
        st.text(movie_names[7])
        st.image(movie_posters[7])
    with col9:
        st.text(movie_names[8])
        st.image(movie_posters[8])
    with col10:
        st.text(movie_names[9])
        st.image(movie_posters[9])
