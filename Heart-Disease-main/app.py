import joblib
import pandas as pd
import pickle
from flask import Flask, request, jsonify, render_template

#load the model
model=joblib.load('heart.pkl')

app=Flask(__name__,template_folder='templates',static_folder='static_files')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict' , methods=['POST'])
def predict():
    try:
        #getting inputs from the form
        age =request.form.get('Age')
        sex =request.form.get('Sex')
        cp =request.form.get('CP')
        trestbps =request.form.get('TrestBPS')
        chol = request.form.get('chol')
        fbs=request.form.get('fbs')
        restecg=request.form.get('restecg')
        thalach=request.form.get('thalac')
        exang=request.form.get('exang')
        oldpeak=request.form.get('oldpeak')
        slope=request.form.get('slope')
        ca=request.form.get('ca')
        thal=request.form.get('thal')
        
        input_data=pd.DataFrame({
            'age':[age],
            'sex':[sex],
        	'cp':[cp],
        	'trestbps':[trestbps],
            'chol':[chol],
            'fbs':[fbs],
            'restecg':[restecg],
            'thalach':[thalach],
            'exang'	:[exang],
            'oldpeak':[oldpeak],
            'slope'	:[slope],
            'ca'	:[ca],
            'thal'	:[thal]

        })
        print(input_data)
        prediction = model.predict(input_data)
        
        
        if prediction[0]==0:
            prediction="Healthy"
        else:
            prediction="Not Healthy"

        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
