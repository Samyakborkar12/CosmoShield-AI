# 🏗️ System Architecture

## CosmoShield AI - High Level Architecture

---

# Architecture Overview

CosmoShield AI follows a modular pipeline that collects space weather data, processes it, predicts future radiation levels using an LSTM model, and presents the results through an interactive dashboard.

The system is designed to support proactive decision-making for ISRO's geostationary satellite operations.

---

# Architecture Flow

```

                     ┌──────────────────────┐
                     │  GOES Electron Data  │
                     └──────────┬───────────┘
                                │

                     ┌──────────────────────┐
                     │ WIND Solar Wind Data │
                     └──────────┬───────────┘
                                │

                     ┌──────────────────────┐
                     │ NOAA Space Weather   │
                     │        API           │
                     └──────────┬───────────┘
                                │

                     ┌──────────────────────┐
                     │ NASA DONKI API       │
                     └──────────┬───────────┘
                                │
                                ▼

                ┌─────────────────────────────┐
                │      Data Collection         │
                └──────────────┬──────────────┘
                               │
                               ▼

                ┌─────────────────────────────┐
                │ Data Cleaning & Processing  │
                └──────────────┬──────────────┘
                               │
                               ▼

                ┌─────────────────────────────┐
                │ Feature Engineering         │
                └──────────────┬──────────────┘
                               │
                               ▼

                ┌─────────────────────────────┐
                │      LSTM Prediction Model  │
                └──────────────┬──────────────┘
                               │
                               ▼

                ┌─────────────────────────────┐
                │ Radiation Risk Assessment   │
                └──────────────┬──────────────┘
                               │
                               ▼

                ┌─────────────────────────────┐
                │ Flask Backend API           │
                └──────────────┬──────────────┘
                               │
                               ▼

                ┌─────────────────────────────┐
                │ Interactive Web Dashboard   │
                └──────────────┬──────────────┘
                               │
                               ▼

                ┌─────────────────────────────┐
                │ Alerts & Decision Support   │
                └─────────────────────────────┘

```

---

# Component Description

## 1. Data Collection

The system gathers historical and real-time space weather data from multiple trusted sources.

### Sources

- GOES Electron Flux
- WIND Solar Wind
- NOAA Space Weather API
- NASA DONKI API

---

## 2. Data Preprocessing

Raw datasets are cleaned before training.

This stage includes:

- Missing value handling
- Timestamp alignment
- Normalization
- Feature selection

The processed data is then converted into sequences suitable for time-series forecasting.

---

## 3. Feature Engineering

Important parameters are extracted from the processed dataset, including:

- Electron Flux
- Solar Wind Speed
- Geomagnetic Activity
- Time Windows

These features become inputs for the prediction model.

---

## 4. LSTM Prediction Model

The LSTM model learns temporal relationships from historical radiation data.

Its objective is to predict future energetic particle flux levels before hazardous conditions occur.

The trained model generates continuous radiation forecasts.

---

## 5. Radiation Risk Assessment

Predicted radiation values are converted into operational risk levels.

Example:

- Low Risk
- Moderate Risk
- High Risk

These risk categories simplify decision-making for satellite operators.

---

## 6. Flask Backend

The Flask backend serves as the communication layer between the machine learning model and the web interface.

Responsibilities include:

- Receiving prediction requests
- Running the AI model
- Returning prediction results
- Managing historical prediction records

---

## 7. Interactive Dashboard

The dashboard displays:

- Current radiation level
- Predicted radiation level
- Historical trends
- Risk status
- Alert notifications

This enables operators to monitor satellite conditions in real time.

---

# System Workflow

1. Collect space weather data.

2. Clean and preprocess the datasets.

3. Generate machine learning features.

4. Run the LSTM prediction model.

5. Calculate satellite radiation risk.

6. Display results on the dashboard.

7. Notify operators if risk exceeds predefined thresholds.

---

# Design Goals

The architecture has been designed with the following objectives:

- Modular structure
- Easy integration of new data sources
- Scalable prediction pipeline
- Real-time monitoring capability
- Future support for multiple satellites
- Lightweight deployment using Flask

---

# Future Architecture Enhancements

Future versions of CosmoShield AI may include:

- Physics-informed AI models
- Transformer-based forecasting
- Cloud-native deployment
- Multi-satellite prediction
- Explainable AI (XAI)
- Real-time streaming pipelines