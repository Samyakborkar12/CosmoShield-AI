# 🌐 API Documentation

## CosmoShield AI Backend API

---

# Overview

The CosmoShield AI backend is developed using **Flask** and provides REST APIs for radiation prediction, system monitoring, and future dashboard integration.

The backend acts as the communication layer between the machine learning model, database, and frontend dashboard.

**Base URL**

```
http://localhost:5000/
```

---

# Authentication

Currently, the APIs do not require authentication.

Future versions may implement:

- JWT Authentication
- API Keys
- OAuth 2.0

---

# Endpoints

---

## 1. Health Check

Checks whether the backend server is running.

### Endpoint

```
GET /health
```

### Response

```json
{
    "status": "running",
    "message": "CosmoShield AI Backend is operational"
}
```

---

## 2. Predict Radiation

Generates a radiation prediction using the trained LSTM model.

### Endpoint

```
POST /predict
```

### Request Body

```json
{
    "electron_flux": 1250.4,
    "solar_wind_speed": 540,
    "solar_wind_density": 6.2,
    "magnetic_field": -3.4
}
```

### Successful Response

```json
{
    "status": "success",
    "prediction": 1384.27,
    "risk_level": "High"
}
```

### Error Response

```json
{
    "status": "error",
    "message": "Invalid input data"
}
```

---

## 3. Prediction History *(Future Scope)*

Returns previous prediction records.

### Endpoint

```
GET /history
```

### Response

```json
[
    {
        "id": 1,
        "prediction": 1354.3,
        "risk_level": "Moderate",
        "timestamp": "2026-07-07T15:30:00"
    }
]
```

---

## 4. Dashboard Data *(Future Scope)*

Returns summarized data for the dashboard.

### Endpoint

```
GET /dashboard
```

### Response

```json
{
    "current_flux": 1254,
    "predicted_flux": 1378,
    "risk_level": "High",
    "last_updated": "2026-07-07T15:45:00"
}
```

---

# API Workflow

```
Frontend

      │

      ▼

Flask API

      │

      ▼

Input Validation

      │

      ▼

LSTM Prediction Model

      │

      ▼

Risk Assessment

      │

      ▼

SQLite Database

      │

      ▼

JSON Response

      │

      ▼

Frontend Dashboard
```

---

# HTTP Status Codes

| Status Code | Meaning |
|-------------|---------|
| 200 | Request Successful |
| 400 | Invalid Input |
| 404 | Endpoint Not Found |
| 500 | Internal Server Error |

---

# Request Validation

Before prediction, every request is validated.

Validation checks include:

- Required fields
- Numeric values
- Missing parameters
- Invalid data types
- Empty requests

If validation fails, the API immediately returns an error response.

---

# Response Format

Every API follows a consistent JSON structure.

### Success

```json
{
    "status": "success",
    "data": {}
}
```

### Failure

```json
{
    "status": "error",
    "message": "Description of the error"
}
```

---

# Backend Technologies

| Component | Technology |
|-----------|------------|
| Framework | Flask |
| Language | Python |
| Machine Learning | TensorFlow / Keras |
| Database | SQLite |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly |

---

# Future API Enhancements

Planned improvements include:

- JWT Authentication
- Real-Time NOAA API Integration
- NASA DONKI Live Events
- Batch Prediction Endpoint
- Satellite-Specific Prediction
- Alert Notification API
- WebSocket Support for Live Dashboard

---

# Summary

The backend API provides a simple, modular, and scalable interface for integrating machine learning predictions with the frontend dashboard. Its RESTful design allows future expansion while maintaining compatibility with real-time space weather data sources.
