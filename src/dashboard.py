import pandas as pd
from datetime import datetime

def save_data(
    aqi,
    temperature,
    humidity,
    status
):

    data = {
        "Timestamp":[datetime.now()],
        "AQI":[aqi],
        "Temperature":[temperature],
        "Humidity":[humidity],
        "Status":[status]
    }

    df = pd.DataFrame(data)

    df.to_csv(
        "data/air_quality_data.csv",
        mode="a",
        index=False,
        header=False
    )