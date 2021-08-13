# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 20:09:33 2021

@author: Tufail Ahmad
"""

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    variable = request.form['variable']
    return variable

if __name__=='__main__':
    app.run()