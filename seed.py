
# User Story 15
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASS = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
MONGO_URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@localhost:27017/"

client = MongoClient(MONGO_URL)
db = client["pim_katalog"]

test_produkte = [
    {
        "name": "Kaffeevollautomat X500",
        "kategorie": "Küche",
        "preis": 450.00,
        "mahlwerk": "Keramik",
        "wassertank_liter": 1.8,
        "smart_home_faehig": True
    },
    {
        "name": "Ergonomischer Bürostuhl",
        "kategorie": "Möbel",
        "preis": 199.99,
        "farbe": "Schwarz",
        "belastbarkeit_kg": 150,
        "material": "Netzstoff"
    },
    {
        "name": "Python für Dummies",
        "kategorie": "Bücher",
        "preis": 25.00,
        "autor": "John Doe",
        "isbn": "978-3-16-148410-0",
        "seiten": 450
    },
    {
        "name": "Gaming Laptop Pro",
        "kategorie": "Technik",
        "preis": 1299.00,
        "grafikkarte": "RTX 4070",
        "ram_gb": 32,
        "festplatte": "1TB SSD",
        "display_hz": 144
    }
]

def seed_datenbank():
    print("⏳ Überprüfe Datenbank...")
    
    # Zählen, wie viele Produkte bereits existieren
    anzahl = db["produkte"].count_documents({})
    
    if anzahl == 0:
        print("💡 Datenbank ist leer. Fülle Testdaten ein...")
        db["produkte"].insert_many(test_produkte)
        print("✅ 4 heterogene Testprodukte erfolgreich angelegt!")
    else:
        print(f"⚠️ Datenbank ist nicht leer. Es gibt bereits {anzahl} Produkte.")
        print("Tipp: Lösche die Produkte vorher, wenn du das Skript neu ausführen willst.")

if __name__ == "__main__":
    seed_datenbank()