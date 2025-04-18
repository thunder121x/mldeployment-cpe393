# mldeployment-cpe393

### model export
Run train.py. (model.pkl will be saved in app folder)

### Go to the directory in terminal
cd "project folder directory"

# How to Run

## Build Docker image
```bash
docker build -t housing-model .
```
## Run Docker container
```bash
docker run -p 9000:9000 housing-model
```

# Test the API in new terminal

curl -X POST http://localhost:9000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [7420, 4, 2, 3, "yes", "no", "no", "no", "yes", 2, "yes", "furnished"]}'

expected output

{"prediction": 0}

# 🏠 Housing Price Predictor – CPE393

## Description
Predict house prices using a regression model trained on housing features such as area, bedrooms, location, and amenities.

## How to Run

### 1. Build Docker image
```bash
docker build -t housing-model .
```

### 2. Run Docker container
docker run -p 9000:9000 housing-model

### 3. Test API
```bash
curl http://localhost:9000/health
```

### 4. Prediction
- Predict Price (Single)\
```bash
curl -X POST http://localhost:9000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [7420, 4, 2, 3, "yes", "no", "no", "no", "yes", 2, "yes", "furnished"]}'
```
Expected Output: {"predicted_price":11181018.8}
- Predict Price (Multiple)\
```bash
curl -X POST http://localhost:9000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [
          [7420, 4, 2, 3, "yes", "no", "no", "no", "yes", 2, "yes", "furnished"],
          [8960, 4, 4, 4, "yes", "no", "no", "no", "yes", 3, "no", "furnished"]
     ]}'
```
Expected Output:{"predicted_prices":[11181018.8,11269959.4]}

### Input Format
[area, bedrooms, bathrooms, stories,
 mainroad, guestroom, basement, hotwaterheating,
 airconditioning, parking, prefarea, furnishingstatus]



