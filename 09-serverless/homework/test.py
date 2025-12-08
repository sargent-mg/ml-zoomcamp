import requests

url = "http://localhost:8080/2015-03-31/functions/function/invocations"
data = {"url": "https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"}

try:
    response = requests.post(url, json=data)
    print("Response status:", response.status_code)
    print("Response text:", response.text)
    print(f"\n--- Question 6 Answer ---")
    print(f"Model output: {response.text}")
except Exception as e:
    print("Error: Could not connect to Docker. Make sure the container is running in your terminal!")
    print(e)
