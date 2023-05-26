import pandas as pd


# Air Passengers Data
def load_air_passengers():

    air_passengers = pd.read_csv('../data/AirPassengers.csv')
    air_passengers['month_start'] = pd.to_datetime(air_passengers['Month'])
    air_passengers['year'] = air_passengers['month_start'].dt.year

    return air_passengers


# Monthly Milk Data
def load_monthly_milk():

    milk_data = pd.read_csv('../data/MonthMilkDataset.csv')
    milk_data['month_start'] = pd.to_datetime(milk_data['Month'])
    milk_data['year'] = milk_data['month_start'].dt.year
    milk_data.columns = ['Month', 'pounds_per_cow', 'month_start', 'year']

    return milk_data


# Air Pollution Data
def load_air_pollution():

    air_pollution = pd.read_csv('../data/airpollution.csv')
    air_pollution['time_of_day'] = pd.to_datetime(air_pollution[['year', 'month', 'day', 'hour']])
    air_pollution.drop(columns='No', axis=1, inplace=True)

    return air_pollution
