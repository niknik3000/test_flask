# -*- coding: utf-8 -*-
from test_app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Батя чё)))'}
    posts = [
        {
            'author': {'username': 'ДонДимон'},
            'body': 'Съел ЛИМОН!!!!!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)