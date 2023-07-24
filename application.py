from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('home.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            Age=request.form.get('Age'),
            Gender=request.form.get('Gender'),
            Cold=request.form.get('Cold'),
            Cough=request.form.get('Cough'),
            Fever=request.form.get('Fever'),
            BP=request.form.get('BP'),
            Diabetes=request.form.get('Diabetes'),
            Thyroid=request.form.get('Thyroid'),
            Arthritis=request.form.get('Arthritis'),
            Acidity=request.form.get('Acidity'),
            Others=request.form.get('Others'),								
        )

        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=round(results[0]))
    

if __name__=="__main__":
    app.run(host="0.0.0.0")        

