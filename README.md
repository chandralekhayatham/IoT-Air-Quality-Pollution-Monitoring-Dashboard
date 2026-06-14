# IoT-Air-Quality-Pollution-Monitoring-Dashboard
IoT-based Air Quality &amp; Pollution Monitoring Dashboard using Python Simulation for AQI monitoring, pollution detection, alert generation, and CSV data logging.
# IoT-Based Air Quality & Pollution Monitoring Dashboard

## Overview

This project is an IoT-inspired Air Quality & Pollution Monitoring Dashboard that monitors air quality parameters such as AQI, temperature, and humidity. The system classifies pollution levels, generates alerts, and stores environmental data for analysis.

---

## Features

- Air Quality Monitoring
- AQI Classification
- Temperature Monitoring
- Humidity Monitoring
- Pollution Alert Generation
- CSV Data Logging
- Python-Based IoT Simulation

---

## Technologies Used

- Python
- IoT Concepts
- Sensor Simulation
- CSV File Handling

---

## Project Structure

IoT-Air-Quality-Pollution-Monitoring-Dashboard

│

├── data

│ └── air_quality_data.csv

│

├── src

│ ├── __init__.py

│ ├── sensor.py

│ ├── aqi.py

│ ├── alert.py

│ └── dashboard.py

│

├── main.py

├── requirements.txt

└── README.md

---

## How to Run

```bash
pip install pandas matplotlib
python main.py
```

## Sample Output

```text
============================================================
 IOT AIR QUALITY & POLLUTION MONITORING DASHBOARD
============================================================

AQI          : 215
Temperature  : 34.2 °C
Humidity     : 65.4 %
Status       : HAZARDOUS

🚨 AIR QUALITY DANGEROUS!

Data Logged Successfully
Thank You for Using Air Quality Monitoring System
```

## Applications

- Smart Cities
- Environmental Monitoring
- Schools and Colleges
- Hospitals
- Smart Homes
- Industrial Pollution Monitoring

## Future Enhancements

- ESP32 Integration
- MQ135 Air Quality Sensor
- DHT11/DHT22 Sensor
- ThingSpeak Dashboard
- Blynk Dashboard
- GPS-Based Pollution Mapping
- AI-Based AQI Prediction
