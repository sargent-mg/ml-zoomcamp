import requests

customer = {
  "gender": "female",
  "seniorcitizen": 0,
  "partner": "yes",
  "dependents": "no",
  "phoneservice": "no",
  "multiplelines": "no_phone_service",
  "internetservice": "dsl",
  "onlinesecurity": "no",
  "onlinebackup": "yes",
  "deviceprotection": "no",
  "techsupport": "no",
  "streamingtv": "no",
  "streamingmovies": "no",
  "contract": "month-to-month",
  "paperlessbilling": "yes",
  "paymentmethod": "electronic_check",
  "tenure": 1,
  "monthlycharges": 29.85,
  "totalcharges": 29.85
}

url = 'http://localhost:9696/predict'

response = requests.post(url, json=customer)
churn = response.json()
print('response', churn)
print(f"Churn probability: {churn['churn_probability']}")
print(f"Churn: {churn['churn']}")



if churn['churn_probability'] >= 0.5:
    print('Send email with promo')
else:
    print("Don't do anything")