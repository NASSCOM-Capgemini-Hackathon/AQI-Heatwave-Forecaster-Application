from flask import request, jsonify , make_response
from app import app

allowed_cities = ['Warnagal','Adilabad','Karimnagar','Khammam','Nizamabad']

@app.route("/", methods=['GET'])
def index():
    data = {"text": "Hello World"}
    return (jsonify(data))

@app.route("/api/aqi/getMonthlyPredictions", methods=['POST'])
def getMonthlyAqiPredictions():
    global allowed_cities
    city=request.json.get('City')
    if city not in allowed_cities:
        return make_response({"Error":"Invalid City Input Given"},500)
    
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
def getHistoricalAQI():
    global allowed_cities
    city=request.json.get('City')
    if city not in allowed_cities:
        return make_response({"Error":"Invalid City Input Given"},500)
    return "Historical AQI"
