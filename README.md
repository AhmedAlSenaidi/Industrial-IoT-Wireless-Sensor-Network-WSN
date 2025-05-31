# Industrial IoT Wireless Sensor Network (WSN)

This project implements a simulated WSN for environmental monitoring using Docker, MQTT, InfluxDB, and Grafana. It simulates sensor data for multiple zones and provides real-time dashboards with alerting capabilities.
!(https://github.com/AhmedAlSenaidi/Industrial-IoT-Wireless-Sensor-Network-WSN/blob/main/wsn_diagram.jpg)
## 📦 Technologies
- Docker & Docker Compose
- Eclipse Mosquitto MQTT Broker
- InfluxDB (Time-series DB)
- Grafana (Dashboard & Alerts)
- Python (Sensor simulation & ingestion)

## 🧱 Project Structure

- `docker-compose.yml` — Container orchestration
- `mqtt_listener.py` — Subscribes to MQTT and writes to InfluxDB
- `simulate_zone1.py`, `simulate_zone2.py` — Sensor data simulation
- `grafana/` — Includes dashboard and alert JSONs
- `provisioning/datasources/influxdb.yaml` — Preconfigures Grafana data source

## 🚀 Getting Started

```bash
# Build and run the stack
docker-compose up --build
