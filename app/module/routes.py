from flask import request, jsonify , make_response
from app import app
from .utils import prepare_data_for_api


@app.route("/", methods=['GET'])
def index():
    data = {"text": "Hello World"}
    return (jsonify(data))

@app.route("/api/aqi/getMonthlyAQIPredictions", methods=['POST'])
def getMonthlyAQIPredictions():
    city=request.json.get('City')
    forecast_type = 'monthly'
    parameter_type = 'aqi'
    return make_response(prepare_data_for_api(city,forecast_type,parameter_type))
    

@app.route("/api/aqi/getDailyAQIPredictions", methods=['POST'])
def getDailyAQIPredictions():
    city=request.json.get('City')
    forecast_type = 'daily'
    parameter_type = 'aqi'
    return make_response(prepare_data_for_api(city,forecast_type,parameter_type))

@app.route("/api/weather/getMonthlyWeatherPredictions", methods=['POST'])
def getMonthlyWeatherPredictions():
    city=request.json.get('City')
    forecast_type = 'monthly'
    parameter_type = 'weather'
    return make_response(prepare_data_for_api(city,forecast_type,parameter_type))
    

@app.route("/api/weather/getDailyWeatherPredictions", methods=['POST'])
def getDailyWeatherPredictions():
    city=request.json.get('City')
    forecast_type = 'daily'
    parameter_type = 'weather'
    return make_response(prepare_data_for_api(city,forecast_type,parameter_type))

# @app.route("/api/aqi/forecastAQI", methods=['POST'])
# def forecastAQI():
#     city=request.json.get('City')
#     forecast_type = 'daily'
#     parameter_type = 'aqi'
#     return make_response(prepare_data_for_api(city,forecast_type,parameter_type))

# @app.route("/api/aqi/forecastAQI", methods=['POST'])
# def getHistoricalAQI():
#     city=request.json.get('City')
#     forecast_type = 'daily'
#     parameter_type = 'aqi'
#     return make_response(prepare_data_for_api(city,forecast_type,parameter_type))
