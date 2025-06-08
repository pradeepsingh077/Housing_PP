import pandas as pd
from flask import Flask, request, jsonify  # type: ignore
import pickle

app = Flask(__name__)

pipe = pickle.load(open('XGBoostingModel.pkl', 'rb'))

@app.route('/api', methods=['POST'])
def predict():
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
