from flask import Flask
from flask import render_template,request
import pickle
import pandas as pd
import numpy as np


app=Flask(__name__)

popular_books = pd.compat.pickle_compat.load(open("popular_books.pkl" , "rb"))
final = pd.compat.pickle_compat.load(open("final.pkl" , 'rb'))
similarity = pickle.load(open("similarity.pkl" , 'rb'))
books = pd.compat.pickle_compat.load(open("books.pkl" , 'rb'))
popular_author = pd.compat.pickle_compat.load(open("popular_author.pkl" , "rb"))

@app.route('/')
def home():
    return render_template('home.html',
                           book_title = list(popular_books['Book-Title'].values),
                           author = list(popular_books['Book-Author'].values),
                           img = list(popular_books['Image-URL-M'].values),
                           num_rating = list(popular_books['num_ratings'].values),
                           avg_rating = list(popular_books['avg_ratings'].values)
                           )

@app.route("/recommend")
def recommend_ui():
    return render_template("recommend.html")

@app.route("/recommend_books" ,methods = ['POST'])
def recommend():
    user_input = request.form.get("Book-Title")

        # fetch index
    index = np.where(final.index==user_input)[0][0]
    
    # fetch top 10 books similar to given book
    simi_book = sorted(list(enumerate(similarity[index])) , key = lambda x:x[1]  , reverse=True)[1:11]
    data = []
    for i in simi_book:
        item = []
        
        df = books[books['Book-Title']==final.index[i[0]]]
        df.drop_duplicates('Book-Title' , inplace = True)
        item.extend(list(df['Book-Title'].values))
        item.extend(list(df['Book-Author'].values))
        item.extend(list(df['Image-URL-M'].values))
        item.extend(list(df['Publisher'].values))
        
        data.append(item)
    
    return render_template("recommend.html" , data=data)


@app.route("/top_author")
def top_author():
    return render_template("top_author.html" , 
                           book_title = list(popular_author['Book-Title'].values),
                           author = list(popular_author['Book-Author'].values),
                           img = list(popular_author['Image-URL-L'].values),
                           num_rating = list(popular_author['num_ratings'].values),
                           avg_rating = list(popular_author['avg_ratings'].values)
                           )

if __name__=="__main__":
    app.run(debug=True)