import pandas as pd
import streamlit as st
import pickle
import requests

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    for i in distances:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


similarity= pickle.load(open('similarity.pkl','rb'))
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)

st.title("movie")
selected_movie = st.selectbox('how will you like to contacted',(movies['title'].values))

if st.button('recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)