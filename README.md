
# neue-Datenbankkonzepte
Gruppennummer A1

## PIM System API (Product Information Management)

- Rest-API für ein Product Information Management System

- Entwickelt mit Python (FastAPI) und MongoDB

- Datenbank und API als Docker-Container bereitgestellt

## Voraussetzungen
- gesamtes System dockerisiert, keine lokale Python-Installation nötig

- Docker Desktop muss installiert und im Hintergrund aktiv sein

## Lokales Setup & Startanleitung

### Schritt 1: Umgebungsvariablen (.env) anlegen
- DB passwörter nicht im Code hinterlegt, sondern über .env Datei ( User Story) 
- `.env` im Hauptverzeichnis erstellen mit folgenden Zeilen:

```bash
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=supergeheim123
```

### Schritt 2: Docker-Container für MongoDB starten
- Terminal öffnen, zum Hauptverzeichnis navigieren und folgenden Befehl ausführen:

```bash
docker-compose up -d --build
```

- startet sowohl MongoDB als auch die FastAPI-Anwendung im Hintergrund

### Schritt 3: API & Dokumentation aufrufen

- API ist unter `http://localhost:8000` erreichbar nach aktivierung der Container

- interaktive Dokumentation (Swagger UI) unter `http://localhost:8000/docs` aufrufbar

## Daten-Seed ausführen
- Seed.py ausführen im venv

```bash
docker exec -it pim_api python seed.py
```

- mögl. URLS zum testen nach seed datei
```bash
http://localhost:8000/produkte?q=Kaffee

http://localhost:8000/produkte?kategorie=Technik&limit=2

http://localhost:8000/produkte?felder=name,preis

http://localhost:8000/statistiken/kategorien
```

## Hinweise
- alle User Stories wurde implementiert aber es besteht Möglichkeit, dass nicht alle gekenzeichnet wurde