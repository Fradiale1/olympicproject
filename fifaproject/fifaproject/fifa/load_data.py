# fifas/load_data.py

import pandas as pd
from fifaproject.fifas.models import Airline, Airplane, fifa


def load_data():
    airlines_df = pd.read_csv('airlines.csv')
    airplanes_df = pd.read_csv('airplanes.csv')
    fifas_df = pd.read_csv('fifas.csv')

    for _, row in airlines_df.iterrows():
        Airline.objects.create(id=row['id'], name=row['name'], country=row['country'])

    for _, row in airplanes_df.iterrows():
        Airplane.objects.create(id=row['id'], model=row['model'], capacity=row['capacity'])

    for _, row in fifas_df.iterrows():
        fifa.objects.create(fifa_number=row['fifa_number'], airline=row['airline'],
                              destination=row['destination'], departure_date=row['departure_date'])
