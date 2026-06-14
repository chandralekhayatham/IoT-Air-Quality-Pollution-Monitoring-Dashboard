def get_status(aqi):

    if aqi <= 50:
        return "GOOD"

    elif aqi <= 100:
        return "MODERATE"

    elif aqi <= 200:
        return "POOR"

    else:
        return "HAZARDOUS"