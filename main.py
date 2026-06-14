from src.sensor import get_air_quality
from src.sensor import get_temperature
from src.sensor import get_humidity

from src.aqi import get_status
from src.alert import get_alert

from src.dashboard import save_data

print("=" * 60)
print(" IOT AIR QUALITY & POLLUTION MONITORING DASHBOARD ")
print("=" * 60)

aqi = get_air_quality()

temperature = get_temperature()

humidity = get_humidity()

status = get_status(aqi)

alert = get_alert(status)

save_data(
    aqi,
    temperature,
    humidity,
    status
)

print("\nAQI          :", aqi)
print("Temperature  :", temperature, "°C")
print("Humidity     :", humidity, "%")
print("Status       :", status)

print("\n" + alert)

print("\nData Logged Successfully")
print("Thank You for Using Air Quality Monitoring System")