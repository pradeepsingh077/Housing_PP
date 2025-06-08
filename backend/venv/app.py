
import pandas as pd
from flask import Flask, request, jsonify # type: ignore

import pickle

app = Flask(__name__)
house = pd.read_csv('clean_data.csv')
pipe = pickle.load(open('XGBoostingModel.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    city = request.form.get('City')
    bhk = request.form.get('BHK')
    size = request.form.get('Size')
    floor = request.form.get('Floor')
    area_type = request.form.get('AreaType')
    furnishing_status = request.form.get('FurnishingStatus')
    bathrooms = request.form.get('Bathroom')

    print(city, bhk, size, floor, area_type, furnishing_status, bathrooms)
    input_data = pd.DataFrame([[city, bhk, size, floor, area_type, furnishing_status, bathrooms]],
                              columns=['City', 'BHK', 'Size', 'Floor', 'AreaType', 'FurnishingStatus', 'Bathroom'])
    prediction = pipe.predict(input_data)[0]

    return str(prediction)

@app.route('/predict_api', methods=['POST'])
def predict_api():

    # For direct API calls trought request
    
    data = request.get_json(force=True)
    city = data['City']
    bhk = data['BHK']
    size = data['Size'] 
    floor = data['Floor']
    area_type = data['AreaType']   
    furnishing_status = data['FurnishingStatus']
    bathrooms = data['Bathroom']
    input_data = pd.DataFrame([[city, bhk, size, floor, area_type, furnishing_status, bathrooms]],
                              columns=['City', 'BHK', 'Size', 'Floor', 'AreaType', 'FurnishingStatus', 'Bathroom'])
    prediction = pipe.predict(input_data)[0]

    return jsonify(prediction)
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
