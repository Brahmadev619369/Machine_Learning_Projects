import streamlit as st
import pandas as pd
import pickle
import requests
from streamlit_option_menu import option_menu

movies = pd.compat.pickle_compat.load(open('movies.pkl' , 'rb'))
similarity = pickle.load((open('similarity.pkl' , 'rb')))
top_movies = pd.compat.pickle_compat.load(open('top_movies.pkl' , 'rb'))

with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>" , unsafe_allow_html=True)


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8fac9e46a405792a5e797d7625f6fc9f&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return poster_path


def movies_recommend(movie_name):
    # to get movie index
    movie_index = movies[movies['title'] == movie_name].index[0]

    # find reccomended movies index and score
    similar_movies = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:11]

    # print movies name use index
    recommend_movies = []
    recommend_poster = []
    ids = []
    for i in similar_movies:
        recc_indx = i[0]
        movie_id = movies.iloc[recc_indx]['id']
        recommend_movies.append(movies.iloc[recc_indx]['title'])
        recommend_poster.append(fetch_poster(movie_id))

        ids.append(str(movie_id))
    return recommend_movies , recommend_poster , ids






selected = option_menu(
    menu_title=None,
    options=['Recommended','Top Movies'],
    orientation='horizontal'
)

if selected=="Recommended":
    st.title('Movie Recommender System')

    selected_movies = st.selectbox(
    'Which movies would you like ?',
    (movies['title']))




    if st.button('recommend'):
        st.markdown("******")
        movies_name  , movies_poster ,ids = movies_recommend(selected_movies)


        col1, col2, col3 = st.columns(3,gap='large')

        with col1:
            st.text(movies_name[0])
            st.image(movies_poster[0])
            url0 = 'https://www.themoviedb.org/movie/' + ids[0]
            st.write("More Details: [click](%s)" % url0)

        with col2:
            st.text(movies_name[1] )
            st.image(movies_poster[1])
            url1 = 'https://www.themoviedb.org/movie/'+ids[1]
            st.write("More Details: [link](%s)" % url1)

        with col3:
            st.text(movies_name[2])
            st.image(movies_poster[2])
            url2 = 'https://www.themoviedb.org/movie/' + ids[2]
            st.write("More Details: [link](%s)" % url2)

        st.markdown("******")

        col1, col2, col3 = st.columns(3,gap='large')

        with col1:
            st.text(movies_name[3])
            st.image(movies_poster[3])
            url3 = 'https://www.themoviedb.org/movie/' + ids[3]
            st.write("More Details: [link](%s)" % url3)

        with col2:
            st.text(movies_name[4] )
            st.image(movies_poster[4])
            url4 = 'https://www.themoviedb.org/movie/' + ids[4]
            st.write("More Details: [link](%s)" % url4)

        with col3:
            st.text(movies_name[5])
            st.image(movies_poster[5])
            url5 = 'https://www.themoviedb.org/movie/' + ids[5]
            st.write("More Details: [link](%s)" % url5)



if selected=='Top Movies':
    def top_movies_fun(top_movies_df):
        names = []
        posters = []
        ids =[]
        for i in range(top_movies.head(15).shape[0]):
            title = top_movies["title"][i]
            names.append(title)
        
            poster = top_movies['poster_path'][i]
            full_post = "https://image.tmdb.org/t/p/w500/" + poster
            posters.append(full_post)
        
            ids.append(str(top_movies['id'][i]))
        
        return names , posters , ids

    names , posters , ids = top_movies_fun(top_movies)

    st.title("Top 15 Movies")



    col1, col2, col3= st.columns(3,gap='large')


    with col1:
        st.text(names[0])
        st.image(posters[0])
        url0 = 'https://www.themoviedb.org/movie/' + ids[0]
        st.write("More Details: [click](%s)" % url0)

    with col2:
        st.text(names[1])
        st.image(posters[1])
        url0 = 'https://www.themoviedb.org/movie/' + ids[1]
        st.write("More Details: [click](%s)" % url0)

    with col3:
        st.text(names[2])
        st.image(posters[2])
        url0 = 'https://www.themoviedb.org/movie/' + ids[2]
        st.write("More Details: [click](%s)" % url0)

    col1, col2, col3= st.columns(3,gap='large')


    with col1:
        st.text(names[3])
        st.image(posters[3])
        url0 = 'https://www.themoviedb.org/movie/' + ids[3]
        st.write("More Details: [click](%s)" % url0)

    with col2:
        st.text(names[4])
        st.image(posters[4])
        url0 = 'https://www.themoviedb.org/movie/' + ids[4]
        st.write("More Details: [click](%s)" % url0)

    with col3:
        st.text(names[5])
        st.image(posters[5])
        url0 = 'https://www.themoviedb.org/movie/' + ids[5]
        st.write("More Details: [click](%s)" % url0)

    col1, col2, col3= st.columns(3,gap='large')


    with col1:
        st.text(names[6])
        st.image(posters[6])
        url0 = 'https://www.themoviedb.org/movie/' + ids[6]
        st.write("More Details: [click](%s)" % url0)

    with col2:
        st.text(names[7])
        st.image(posters[7])
        url0 = 'https://www.themoviedb.org/movie/' + ids[7]
        st.write("More Details: [click](%s)" % url0)

    with col3:
        st.text(names[8])
        st.image(posters[8])
        url0 = 'https://www.themoviedb.org/movie/' + ids[8]
        st.write("More Details: [click](%s)" % url0)

    col1, col2, col3= st.columns(3,gap='large')


    with col1:
        st.text(names[9])
        st.image(posters[9])
        url0 = 'https://www.themoviedb.org/movie/' + ids[9]
        st.write("More Details: [click](%s)" % url0)

    with col2:
        st.text(names[10])
        st.image(posters[10])
        url0 = 'https://www.themoviedb.org/movie/' + ids[10]
        st.write("More Details: [click](%s)" % url0)

    with col3:
        st.text(names[11])
        st.image(posters[11])
        url0 = 'https://www.themoviedb.org/movie/' + ids[11]
        st.write("More Details: [click](%s)" % url0)

    col1, col2, col3= st.columns(3,gap='large')


    with col1:
        st.text(names[12])
        st.image(posters[12])
        url0 = 'https://www.themoviedb.org/movie/' + ids[12]
        st.write("More Details: [click](%s)" % url0)

    with col2:
        st.text(names[13])
        st.image(posters[13])
        url0 = 'https://www.themoviedb.org/movie/' + ids[13]
        st.write("More Details: [click](%s)" % url0)

    with col3:
        st.text(names[14])
        st.image(posters[14])
        url0 = 'https://www.themoviedb.org/movie/' + ids[14]
        st.write("More Details: [click](%s)" % url0)
