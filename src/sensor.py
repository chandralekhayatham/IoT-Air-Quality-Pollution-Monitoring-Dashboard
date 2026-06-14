import random

def get_air_quality():
    return random.randint(20, 300)

def get_temperature():
    return round(random.uniform(20, 40), 1)

def get_humidity():
    return round(random.uniform(30, 90), 1)