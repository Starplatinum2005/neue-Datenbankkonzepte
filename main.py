from fastapi import FastAPI

# Hier startet die API
app = FastAPI(title="PIM System API", version="1.0")

# Ein erster Test-Endpunkt
@app.get("/")
def read_root():
    return {"status": "Erfolgreich", "message": "Die PIM-API läuft!"}