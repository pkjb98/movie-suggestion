# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 06:05:21 2025

@author: J.B.pradeep kumar
"""

import numpy as np
import pandas as pd
import difflib
import streamlit as st
import pickle 


# loading the dataset package

movies = pickle.load(open('C:/Users/J.B.pradeep kumar/Documents/Machine Learing/Deployment/Movie Recommandations/movies.pkl','rb'))

# loading the trained model

loaded_model = pickle.load(open('C:/Users/J.B.pradeep kumar/Documents/Machine Learing/Deployment/Movie Recommandations/trained_pkl_movie_model.pkl','rb'))

# list of all movie sin the package

list_of_movies = movies['title'].tolist()

# creating a for suggestion  
def suggestion(movie_name):
  
   
    find_close_match = difflib.get_close_matches(movie_name,list_of_movies)

    close_match = find_close_match[0]

    index_of_movie = movies[movies['title']==close_match]['index'].values[0]

    similarity_score = list(enumerate(loaded_model[index_of_movie]))

    sorted_similar_score = sorted(similarity_score,key =lambda x:x[1],reverse=True)


    print('Movies Suggested to you : \n')
    
    i = 1
    
    movie_names =[]
    
    for movie in sorted_similar_score:
        index = movie[0]
        movie_title = movies[movies['index']==index]['title'].values[0]
        if i<11:
            movie_names.append(movie_title)
            i+=1
    return movie_names   
    
def main():
    
    recommened = ' '
    
    # giving a title 
    
    st.title = ('Movie Recommandation Syatem')
    
    # getting the movie name from the user
    
    option = st.selectbox('Hoe wuld you like to be contactes',list_of_movies)
    
    # Creating a butto n for selection
    
    if st.button('Recommend'):
        recommend =suggestion(option)
        
        for i in recommend:
            st.write(i)
    st.success(recommened)
    
    

if __name__=='__main__':
    main()