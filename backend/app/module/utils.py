import pandas as pd
import boto3
from datetime import date
import os
import botocore
from dotenv import load_dotenv

load_dotenv('backend\.env')
ALLOWED_CITIES = ['Warangal', 'Adilabad', 'Karimnagar', 'Khammam', 'Nizamabad']


def prepare_data_for_api(city, forecast_type, parameter_type):
    """utils functions for API endpoint

    Args:
        city (string)
        forecast_type (monthly | daily)
        parameter_type (aqi | weather)

    Returns:
        json of predictions
    """
    global ALLOWED_CITIES
    today = date.today()
    if city not in ALLOWED_CITIES:
        return ({"Error": "Invalid City Input Given"}, 500)

    filename = '{}/{}/{}/{}-{}.csv'.format(forecast_type,
                                           parameter_type, city, parameter_type, '2023-02-20')
    df = get_xlsx_from_aws(filename, forecast_type, parameter_type, city)
    if df == None or df.empty:
        return ({"Error": "Data doesn't exists"}, 500)
    json_data = df.to_json(orient='records')
    return (json_data, 200)


def get_xlsx_from_aws(filename, forecast_type, parameter_type, city_name):
    """utils functions for API endpoint

    Args:
        filename (string)
        forecast_type (monthly | daily)
        parameter_type (aqi | weather)
        city_name (string)

    Returns:
        pandas data frame
    """
    today = date.today()

    req_dst = '../backend/temp/{}/{}/{}/{}-{}.csv'.format(
        forecast_type, parameter_type, city_name, parameter_type, '2023-02-20')

    if os.path.exists(req_dst):
        df = pd.read_csv(req_dst, header=0)
        return df
    else:
        cli = boto3.client('s3', aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                           aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
        
        s3 = boto3.resource('s3', aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                           aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

        bucket_name = 'capegemini-hackathon'

        print(filename)

        try:
            s3.Object(bucket_name, filename).load()
            print("here",req_dst)

            with open(req_dst, 'wb') as f:
                cli.download_fileobj(bucket_name, filename, f)
            df = pd.read_csv(req_dst, header=0)
            return df
        except botocore.exceptions.ClientError as e:
            print("+++",os.getenv('AWS_ACCESS_KEY_ID'),e)
            return None
