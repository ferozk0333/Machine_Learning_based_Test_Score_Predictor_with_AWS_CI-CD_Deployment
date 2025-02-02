from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from logging import FileHandler,WARNING


from sklearn.preprocessing import StandardScaler   #to scale pickle file
from src.pipeline.predict_pipeline import CustomData,PredictPipeline


application = Flask(__name__,template_folder="templates")       #entry point to application
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

app =application

# route for home page

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():                                             #fetching data and returning output
    
    if request.method == 'GET':
        return render_template('home.html')
    else:   #POST request
        
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )

        pred_df = data.get_data_as_data_frame()                         #function defined in predict_pipeline
        

        predict_pipeline = PredictPipeline()                            #object of PredictPipeline class
        results = predict_pipeline.predict(pred_df)                     #transfers flow to predict fn in predict_pipeline.py
        return render_template('home.html', results = str(round(results[0],2)))       #all the values are in list format, so results[0]
    
    #testing app
    if __name__=="__main__":
        
        app.run(host='0.0.0.0', port = 8080)  
    
    
