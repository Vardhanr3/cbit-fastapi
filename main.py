from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# Allow CORS for ESP32
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/notifications")
def get_marquee():
    url = "https://www.cbit.ac.in"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    marquee = soup.find("marquee")
    return marquee.text.strip() if marquee else "No notifications found"

@app.get("/notifications_2")
def get_extra():
    return "Class timings updated for semester VI."  # Or scrape from a different section
