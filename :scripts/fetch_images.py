import csv
import json
import time
import requests
from io import StringIO
from ddgs import DDGS

SPREADSHEET_CSV = "https://docs.google.com/spreadsheets/d/1meud5tcE8JCNIfu5nHkaexqyHtUc61w7orIMY05nors/export?format=csv&gid=2099863132"

response = requests.get(SPREADSHEET_CSV)
csv_text = response.text

reader = csv.DictReader(StringIO(csv_text))

results = {}

with DDGS() as ddgs:

    for row in reader:

        item_id = row["id"]
        query = row["image_query"]

        print(f"Fetching: {query}")

        images = ddgs.images(

    query,

    max_results=10

)

        urls = []

        try:
            for image in images:
                if "image" in image:
                    urls.append(image["image"])

        except Exception as e:
            print("Error:", e)

        results[item_id] = urls

        time.sleep(1.5)

with open("images.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Done!")