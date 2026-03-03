# neue-Datenbankkonzepte
Gruppennummer A1

## PIM System API (Product Information Management)

Dieses Projekt ist eine REST-API für ein Product Information Management System, entwickelt mit **Python (FastAPI)** und **MongoDB**. Die Datenbank wird als Docker-Container bereitgestellt, um eine einheitliche und persistente Entwicklungsumgebung zu garantieren.

## Voraussetzungen
Bevor du das Projekt startest, stelle sicher, dass Folgendes auf deinem Rechner installiert ist:
- **Python 3.10+** (inklusive `pip`)
- **Docker Desktop** (muss im Hintergrund laufen)

---

##  Lokales Setup & Startanleitung

Folge diesen Schritten, um die API und die Datenbank auf deinem lokalen Rechner zu starten:

### Schritt 1: Umgebungsvariablen (.env) anlegen
Aus Sicherheitsgründen sind die Datenbank-Passwörter nicht im Code hinterlegt. Erstelle im Hauptverzeichnis des Projekts eine Datei namens `.env` und füge folgende Zeilen ein:

```env
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=supergeheim123

```

### Schritt 2: Docker-Container für MongoDB starten
Navigiere im Terminal zum Hauptverzeichnis des Projekts und führe den folgenden Befehl aus, um den MongoDB-Container zu starten:

```bash
docker-compose up -d
```
Dieser Befehl startet den MongoDB-Container im Hintergrund. Die Datenbank ist nun unter `mongodb://localhost:27017` erreichbar.
### Schritt 3: Python-Abhängigkeiten installieren
Erstelle ein virtuelles Python-Umfeld und installiere die benötigten Pakete:

```bash
python -m venv venv
source venv/bin/activate  # Für Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Schritt 4: API starten
Starte die FastAPI-Anwendung mit folgendem Befehl:

```bash
uvicorn main:app --reload
```
Die API ist nun unter `http://localhost:8000` erreichbar. Du kannst die interaktive Dokumentation unter `http://localhost:8000/docs` aufrufen.

### Schritt 5: API-Endpunkte testen
Du kannst die API-Endpunkte entweder über die interaktive Dokumentation oder mit Tools wie Postman oder curl testen. Hier sind einige Beispiel-Endpunkte:
- **GET** `/products/` - Alle Produkte abrufen