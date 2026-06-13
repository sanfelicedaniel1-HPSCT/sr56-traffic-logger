import csv
import os
import requests
from datetime import datetime

API_KEY = "<insert API key>"

HEADERS = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": API_KEY,
    "X-Goog-FieldMask": "routes.duration,routes.staticDuration"
}

def get_data(origin, destination):
    """Executes an authenticated JSON POST request to Google Routes API v2"""
    COORDS_I5 = {"latitude": 32.9373, "longitude": -117.2346}   # West End (Del Mar)
    COORDS_I15 = {"latitude": 32.9467, "longitude": -117.1035}  # East End (Rancho Peñasquitos)
    
    payload = {
        "origin": {"latLng": origin},
        "destination": {"latLng": destination},
        "travelMode": "DRIVE",
        "routingPreference": "TRAFFIC_AWARE_OPTIMAL"
    }
    
    try:
        response = requests.post(URL, json=payload, headers=HEADERS)

        # Boundary Coordinates for SR-56


def main():
    data = get_data(COORDS_I15, COORDS_I5)

