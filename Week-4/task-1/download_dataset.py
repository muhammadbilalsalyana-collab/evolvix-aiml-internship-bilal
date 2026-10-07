import requests

url = "https://raw.githubusercontent.com/sni-gdh/Titanic_dataset/main/train_and_test2.csv"

r = requests.get(url)
r.raise_for_status()

with open("train_and_test2.csv", "wb") as f:
    f.write(r.content)

print("Dataset downloaded successfully.")
