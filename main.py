from fastapi import FastAPI, Body, HTTPException
from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="PIM System API", version="1.0")

MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASS = os.getenv("MONGO_INITDB_ROOT_PASSWORD")

MONGO_URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@localhost:27017/"

client = MongoClient(MONGO_URL)
db = client["pim_katalog"]

@app.get("/")
def read_root():
    try:
        client.admin.command('ping')
        return {"status": "API läuft", "datenbank_status": "Erfolgreich mit MongoDB verbunden! 🚀"}
    except Exception as e:
        return {"status": "Fehler", "datenbank_status": f"Verbindungsfehler: {e}"}

@app.post("/produkte")
def produkt_anlegen(produkt_daten: dict = Body(...)):

    ergebnis = db["produkte"].insert_one(produkt_daten)
    

    return {
        "nachricht": "Produkt erfolgreich angelegt!",
        "generierte_id": str(ergebnis.inserted_id)
    }

@app.get("/produkte")
def alle_produkte_abrufen():
    produkte_cursor = db["produkte"].find()
    

    produkte_liste = []
    for produkt in produkte_cursor:
        produkt["_id"] = str(produkt["_id"]) 
        produkte_liste.append(produkt)
        
    return produkte_liste

@app.get("/produkte/{produkt_id}")
def einzelnes_produkt_abrufen(produkt_id: str):
    if not ObjectId.is_valid(produkt_id):
        raise HTTPException(status_code=400, detail="Ungültiges ID-Format")
    
    produkt = db["produkte"].find_one({"_id": ObjectId(produkt_id)})
    
    if produkt is None:
        raise HTTPException(status_code=404, detail="Produkt nicht gefunden")
    
    produkt["_id"] = str(produkt["_id"])
    return produkt

@app.delete("/produkte/{produkt_id}")
def produkt_loeschen(produkt_id: str):
    if not ObjectId.is_valid(produkt_id):
        raise HTTPException(status_code=400, detail="Ungültiges ID-Format")
    
    ergebnis = db["produkte"].delete_one({"_id": ObjectId(produkt_id)})
    
    if ergebnis.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Produkt zum Löschen nicht gefunden")
        
    return {"nachricht": "Produkt erfolgreich gelöscht!"}

