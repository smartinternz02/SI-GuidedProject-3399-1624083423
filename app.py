# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask,request,render_template
import numpy as np
import re
import requests as HTTP
from bs4 import BeautifulSoup as SOUP
import os
import pandas as pd


app=Flask(__name__,template_folder="templates")

@app.route('/',methods=['GET'])
def index():
    return render_template('emojis.html')
@app.route('/',methods=['GET'])
def about():
    return render_template('emojis.html')
@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method=="POST":
        emotion=request.form['recom']
        print(emotion)
    if(emotion=="Sad"):
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
    elif(emotion=="Enjoyment"):
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Trust"):
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Anger"):
        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Anticipation"):
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    response = HTTP.get(urlhere)
    data = response.text
    soup = SOUP(data, "lxml")
    supa = soup.find_all('h3', attrs={'class' : 'lister-item-header'})
    list1=[]
    for header in supa:
        name=""
        aElement_soup=header.find_all('a')
        spanElement_soup=header.find_all('span')
        spanElement=spanElement_soup[0]
        name=name+spanElement.text
        aElement=aElement_soup[0]
        name=name+" "+aElement.text
        if(len(spanElement_soup)>1):
            spanElement=spanElement_soup[1]
            name=name+" "+spanElement.text
        name=name.split('.')
        list1.append([int(name[0]),name[1]])
    #list1=pd.DataFrame(list1)
    #print(list1)
    return render_template("result.html",prediction_text=list1)
if __name__ == "__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)
    predict()