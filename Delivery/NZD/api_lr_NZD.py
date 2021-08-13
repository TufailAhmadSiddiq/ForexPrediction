
from flask import Flask, request, jsonify, render_template
import joblib
import traceback
import pandas as pd
import numpy as np
import sys

# Your API definition
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET', 'POST'])


def predict():
    pred = ''
    if request.method == 'POST':
        
        Open = float(request.form.get('Open'))
        high = float(request.form.get('High'))
        low = float(request.form.get('Low'))
        
        query = [[Open, low, high]]
        print(query)
        
        if query:
            pred = lr.predict(query)
    
        #prediction = jsonify({'prediction': str(prediction)})
            
    return render_template('index.html', prediction=pred)



if __name__ == '__main__':

    lr = joblib.load("Model/model_NZD.pkl") # Load "model.pkl"
    print ('Model loaded')

    app.run(debug=True)