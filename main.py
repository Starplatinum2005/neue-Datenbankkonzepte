from fastapi import FastAPI, Body, HTTPException, Request, Query
from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv
from typing import List

load_dotenv()

app = FastAPI(title="PIM System API", version="1.0")

MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASS = os.getenv("MONGO_INITDB_ROOT_PASSWORD")

MONGO_URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@localhost:27017/"

client = MongoClient(MONGO_URL)
db = client["pim_katalog"] 

# User Story 24

db["produkte"].create_index([("$**", "text")]) # alle vollen Wörter werden indiziert

# index für exakte suche in kategorie, da diese häufig für filterung genutzt wird
db["produkte"].create_index("kategorie")

#index für preis, da dieser häufig für sortierung genutzt wird
db["produkte"].create_index([("preis", 1)]) 

@app.get("/") # User Sory 16
def read_root():
    try:
        client.admin.command('ping')
        return {"status": "API läuft", "datenbank_status": "Erfolgreich mit MongoDB verbunden!"}
    except Exception as e:
        return {"status": "Fehler", "datenbank_status": f"Verbindungsfehler: {e}"}

@app.post("/produkte") # User Story 3 und 22(Bilder links möglich)
def produkt_anlegen(produkt_daten: dict = Body(...)):
    
    if "name" not in produkt_daten or "kategorie" not in produkt_daten: # User Story 13
        raise HTTPException(
            status_code=422, 
            detail="Pflichtfelder fehlen! Ein Produkt muss zwingend 'name' und 'kategorie' enthalten."
        )

    ergebnis = db["produkte"].insert_one(produkt_daten)
    
    return {
        "nachricht": "Produkt erfolgreich angelegt!", # User Story 6
        "generierte_id": str(ergebnis.inserted_id)
    }



 
# User Stories 2, 8, 9, 10, 11, 17

@app.get("/produkte")
def produkte_abrufen(
    request: Request, 
    q: str = Query(None, description="Volltextsuche in allen Textfeldern"),
    felder: str = Query(None, description="Kommagetrennte Felder (z.B. name,preis)"),
    inklusive_archiviert: bool = Query(False, description="Auch archivierte zeigen?"),
    limit: int = Query(10, ge=1, description="Max. Anzahl der Ergebnisse"),
    offset: int = Query(0, ge=0, description="Anzahl der zu überspringenden Ergebnisse"),
    sort_by: str = Query(None, description="Feldname für die Sortierung (z.B. preis)"),
    sort_order: str = Query("asc", description="'asc' für aufsteigend, 'desc' für absteigend")
):
    
    reservierte_parameter = ["limit", "offset", "sort_by", "sort_order", "q", "felder", "inklusive_archiviert"] 
    such_filter = {}
    
    if not inklusive_archiviert:
        such_filter["archiviert"] = {"$ne": True}
        
    if q:
        such_filter["$text"] = {"$search": q}
    
    for key, value in request.query_params.items():
        if key not in reservierte_parameter:
            try:
                if "." in value:
                    such_filter[key] = float(value)
                else:
                    such_filter[key] = int(value)
            except ValueError:
                such_filter[key] = value 

    projektion = None
    if felder:
        projektion = {feld.strip(): 1 for feld in felder.split(",")}

    cursor = db["produkte"].find(such_filter, projektion)

    if sort_by:
        richtung = 1 if sort_order == "asc" else -1
        cursor = cursor.sort(sort_by, richtung)

    cursor = cursor.skip(offset).limit(limit)

    produkte_liste = []
    for produkt in cursor:
        produkt["_id"] = str(produkt["_id"])
        produkte_liste.append(produkt)

    return produkte_liste


#User Story 21
@app.patch("/produkte/{produkt_id}/archivieren")
def produkt_archivieren(produkt_id: str, archivieren: bool = Query(True)):
    if not ObjectId.is_valid(produkt_id):
        raise HTTPException(status_code=400, detail="Ungültiges ID-Format")
    
    ergebnis = db["produkte"].update_one(
        {"_id": ObjectId(produkt_id)},
        {"$set": {"archiviert": archivieren}}
    )
    
    if ergebnis.matched_count == 0:
        raise HTTPException(status_code=404, detail="Produkt nicht gefunden")
        
    status_text = "archiviert" if archivieren else "wiederhergestellt"
    return {"nachricht": f"Produkt erfolgreich {status_text}!"}

@app.get("/produkte/{produkt_id}") # User Story 1
def einzelnes_produkt_abrufen(produkt_id: str):
    if not ObjectId.is_valid(produkt_id):
        raise HTTPException(status_code=400, detail="Ungültiges ID-Format")
    
    produkt = db["produkte"].find_one({"_id": ObjectId(produkt_id)})
    
    if produkt is None:
        raise HTTPException(status_code=404, detail="Produkt nicht gefunden")
    
    produkt["_id"] = str(produkt["_id"])
    return produkt

@app.delete("/produkte/{produkt_id}") # User Story 4
def produkt_loeschen(produkt_id: str):
    if not ObjectId.is_valid(produkt_id):
        raise HTTPException(status_code=400, detail="Ungültiges ID-Format") # user story 16
    
    ergebnis = db["produkte"].delete_one({"_id": ObjectId(produkt_id)})
    
    if ergebnis.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Produkt zum Löschen nicht gefunden")
        
    return {"nachricht": "Produkt erfolgreich gelöscht!"}

# User Story 12
@app.patch("/produkte/{produkt_id}")
def produkt_aktualisieren(produkt_id: str, update_daten: dict = Body(...)):
    if not ObjectId.is_valid(produkt_id):
        raise HTTPException(status_code=400, detail="Ungültiges ID-Format")
    
    if not update_daten:
        raise HTTPException(status_code=400, detail="Keine Daten zum Aktualisieren übergeben")

    # Das "$set" aktualisiert nur die angegebenen Felder oder fügt  neu hinzu ohne bestehende Felder zu löschen geht nicht relational
    ergebnis = db["produkte"].update_one(
        {"_id": ObjectId(produkt_id)},
        {"$set": update_daten}
    )
    
    if ergebnis.matched_count == 0:
        raise HTTPException(status_code=404, detail="Produkt zum Aktualisieren nicht gefunden")
        
    return {"nachricht": "Produkt erfolgreich aktualisiert!"}


# User Story 18
@app.get("/statistiken/kategorien")
def statistiken_kategorien():
    pipeline = [
        {
            "$group": {
                "_id": "$kategorie", 
                "anzahl_produkte": {"$sum": 1}
            }
        },
        {
            "$sort": {"anzahl_produkte": -1}
        }
    ]

    cursor = db["produkte"].aggregate(pipeline)

    statistik_liste = []
    for eintrag in cursor:
        kategorie_name = eintrag["_id"] if eintrag["_id"] else "Unkategorisiert"
        
        statistik_liste.append({
            "kategorie": kategorie_name,
            "anzahl": eintrag["anzahl_produkte"]
        })
        
    return statistik_liste

# User Story 20
@app.post("/produkte/bulk")
def produkte_bulk_anlegen(produkte_liste: List[dict] = Body(...)):
    for produkt in produkte_liste:
        if "name" not in produkt or "kategorie" not in produkt:
            raise HTTPException(
                status_code=422, 
                detail="Fehler! Jedes Produkt in der Liste muss 'name' und 'kategorie' enthalten."
            )
    
    ergebnis = db["produkte"].insert_many(produkte_liste)
    
    return {
        "nachricht": f"{len(ergebnis.inserted_ids)} Produkte erfolgreich angelegt!",
        "generierte_ids": [str(id) for id in ergebnis.inserted_ids]
    }

# User Story 23
@app.post("/produkte/{produkt_id}/duplizieren")
def produkt_duplizieren(produkt_id: str):
    if not ObjectId.is_valid(produkt_id):
        raise HTTPException(status_code=400, detail="Ungültiges ID-Format")
    
    original_produkt = db["produkte"].find_one({"_id": ObjectId(produkt_id)})
    
    if not original_produkt:
        raise HTTPException(status_code=404, detail="Original-Produkt nicht gefunden")
    
    del original_produkt["_id"]
    
    original_produkt["name"] = original_produkt["name"] + " (Kopie)"
    
    ergebnis = db["produkte"].insert_one(original_produkt)
    
    return {
        "nachricht": "Produkt erfolgreich dupliziert!",
        "neue_id": str(ergebnis.inserted_id)
    }