from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_classifier_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        age = int(request.form['age'])
        sex=int(request.form['sex'])
        cp=int(request.form['cp'])
        trtbps=int(request.form['trtbps'])
        chol=int(request.form['chol'])
        fbs=int(request.form['fbs'])
        restecg=int(request.form['restecg'])
        thalach=int(request.form['thalach'])
        exng=int(request.form['exng'])
        oldpeak=float(request.form['oldpeak'])
        slp=int(request.form['slp'])
        caa=int(request.form['caa'])
        thall=int(request.form['thall'])
        
        prediction=model.predict([[age, sex, cp, trtbps, chol, fbs, restecg, thalach, exng, oldpeak, slp, caa, thall]])
        output=prediction[0]
        if output<1:
            return render_template('index.html',prediction_texts="Patient has less chance of Heart Attack")
        else:
            return render_template('index.html',prediction_text="Patient has less chance of Heart Attack")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)