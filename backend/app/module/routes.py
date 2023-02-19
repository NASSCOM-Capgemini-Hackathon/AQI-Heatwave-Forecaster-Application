from flask import request, jsonify, make_response
from app import app
import pickle
from .model import LSTM_Model

allowed_cities = ['Warnagal','Adilabad','Karimnagar','Khammam','Nizamabad']

@app.route("/api/aqi/getMonthlyPredictions", methods=['POST'])
def getMonthlyAqiPredictions():
    global allowed_cities
    city=request.json.get('City')
    if city not in allowed_cities:
        return make_response({"Error":"Invalid City Input Given"},500)
    try:
        picklefile=open(r'E:/NASSCOMM Hackathon/AQI-Heatwave-Forecaster-Application/backend/app/module/models/adilabad_AQI_LSTM.pickle','rb')
        print("Here")
        model = pickle.load(picklefile)
        picklefile.close()
        forecasted=model.forecast_future(15)
        print(forecasted)
    except Exception as e:
            print(e)
            return make_response({"Error":"Model Not Found"},500)
    return "Monthly Predictions-{}".format(city.lower())

@app.route("/api/aqi/getDailyAQI", methods=['POST'])
def getDailyAQI():
    global allowed_cities
    city=request.json.get('City')
    if city not in allowed_cities:
        return make_response({"Error":"Invalid City Input Given"},500)
    return "Forecast AQI"

@app.route("/api/aqi/forecastAQI", methods=['POST'])
def forecastAQI():
    global allowed_cities
    city=request.json.get('City')
    if city not in allowed_cities:
        return make_response({"Error":"Invalid City Input Given"},500)
    return "Forecast AQI"

@app.route("/api/aqi/forecastAQI", methods=['POST'])
def getHistroicalAQI():
    global allowed_cities
    city=request.json.get('City')
    if city not in allowed_cities:
        return make_response({"Error":"Invalid City Input Given"},500)
    return "Historical AQI"
