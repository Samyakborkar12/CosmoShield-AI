# 🤖 Model Explanation

## AI Model Used in CosmoShield AI

---

# Overview

CosmoShield AI uses a Long Short-Term Memory (LSTM) neural network to forecast energetic particle radiation levels around geostationary satellites.

LSTM is a deep learning architecture specifically designed for sequential and time-series data. Since space weather measurements are collected continuously over time, LSTM is well suited for learning long-term temporal patterns and predicting future radiation conditions.

---

# Why Time-Series Forecasting?

Radiation measurements are not independent observations.

Current radiation levels depend on previous measurements, solar activity, and changes in the space environment.

Time-series forecasting allows the model to learn these temporal relationships and estimate future radiation conditions using historical observations.

Example:

```
Previous 24 Hours Data
        │
        ▼
     LSTM Model
        │
        ▼
Predicted Radiation Level
```

---

# Why LSTM?

Traditional machine learning models treat each observation independently.

However, radiation forecasting requires remembering patterns over long periods of time.

LSTM networks solve this problem by maintaining an internal memory that stores useful historical information while discarding irrelevant data.

Advantages of LSTM include:

- Learns long-term dependencies
- Handles sequential data effectively
- Captures nonlinear relationships
- Produces stable forecasts
- Suitable for continuously changing environments

---

# Why Not Traditional Machine Learning?

## Linear Regression

- Assumes linear relationships
- Cannot model complex temporal dependencies
- Poor performance on sequential space weather data

---

## Decision Trees

- Good for classification
- Limited capability for sequence prediction
- Does not retain historical memory

---

## Random Forest

- Strong general-purpose model
- Cannot naturally learn sequential patterns
- Requires manual feature engineering

---

## LSTM

- Designed specifically for sequential data
- Maintains memory of previous observations
- Better suited for radiation forecasting

---

# LSTM Architecture

The prediction model consists of the following layers:

```
Input Sequence
       │
       ▼

LSTM Layer

       │
       ▼

Dropout Layer

       │
       ▼

Dense Layer

       │
       ▼

Radiation Prediction
```

---

# Working of LSTM

LSTM manages information using three gates.

## Forget Gate

Removes information that is no longer useful for prediction.

Example:

Older radiation conditions that have little influence on the current environment.

---

## Input Gate

Stores important new information such as sudden increases in solar activity or energetic particle flux.

---

## Output Gate

Uses the retained information to generate the final prediction.

---

# Input Features

The model may use features such as:

- Electron Flux
- Solar Wind Speed
- Solar Wind Density
- Magnetic Field Parameters
- Timestamp
- Solar Event Indicators

These features are converted into time sequences before training.

---

# Model Input

Example:

```
Past 24 Observations
        │
        ▼
Input Tensor
        │
        ▼
LSTM
```

---

# Model Output

The model predicts:

- Future Electron Flux
- Radiation Risk Level (derived from prediction)

Example:

```
Predicted Electron Flux

↓

Risk Level

Low

Moderate

High
```

---

# Training Process

The training pipeline consists of the following steps:

1. Load processed dataset

2. Normalize numerical features

3. Create sequential training windows

4. Split into training and validation datasets

5. Train the LSTM network

6. Evaluate model performance

7. Save the trained model

---

# Loss Function

For regression-based forecasting, common loss functions include:

- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)

The selected loss function measures the difference between predicted and actual radiation values.

---

# Optimizer

The model uses the Adam optimizer.

Advantages:

- Fast convergence
- Stable learning
- Efficient gradient updates

---

# Evaluation Metrics

Model performance can be evaluated using:

| Metric | Purpose |
|---------|----------|
| MAE | Average prediction error |
| RMSE | Penalizes larger errors |
| MAPE | Percentage prediction error |

---

# Prediction Pipeline

```
Historical Dataset
        │
        ▼

Preprocessing

        │
        ▼

Sequence Generation

        │
        ▼

LSTM Prediction

        │
        ▼

Predicted Electron Flux

        │
        ▼

Risk Assessment

        │
        ▼

Dashboard & Alerts
```

---

# Future Improvements

Future versions of CosmoShield AI may include:

- Transformer-based forecasting models
- Physics-informed neural networks
- Ensemble learning approaches
- Explainable AI (XAI)
- Real-time online learning
- Multi-satellite prediction models

---

# Conclusion

The LSTM model forms the core intelligence of CosmoShield AI.

By learning temporal relationships from historical space weather observations, it enables early prediction of hazardous radiation conditions and supports proactive protection of ISRO's geostationary satellites.
