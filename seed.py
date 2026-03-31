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

    # --- Kategorie: Technik ---
    {
        "name": "Gaming Laptop Pro",
        "kategorie": "Technik",
        "preis": 1299.00,
        "beschreibung": "Hochleistungs-Gaming-Laptop mit RTX 4070 und 144Hz Display",
        "grafikkarte": "RTX 4070",
        "ram_gb": 32,
        "festplatte": "1TB SSD",
        "display_hz": 144,
        "display_zoll": 15.6,
        "betriebssystem": "Windows 11",
        "farben": ["Schwarz", "Grau"],
        "abmessungen": {"breite_cm": 36, "tiefe_cm": 25, "hoehe_cm": 2.3},
        "gewicht_kg": 2.1,
        "garantie_jahre": 2
    },
    {
        "name": "Ultrabook Business S14",
        "kategorie": "Technik",
        "preis": 999.00,
        "beschreibung": "Schlankes Business-Notebook für unterwegs",
        "prozessor": "Intel Core i7-1355U",
        "ram_gb": 16,
        "festplatte": "512GB SSD",
        "display_zoll": 14.0,
        "display_hz": 60,
        "akku_stunden": 12,
        "gewicht_kg": 1.3,
        "farben": ["Silber"],
        "abmessungen": {"breite_cm": 32, "tiefe_cm": 22, "hoehe_cm": 1.6},
        "garantie_jahre": 2
    },
    {
        "name": "Smartphone Nova 15",
        "kategorie": "Technik",
        "preis": 799.00,
        "beschreibung": "Flaggschiff-Smartphone mit 200MP Kamera",
        "speicher_gb": 256,
        "ram_gb": 12,
        "kamera_mp": 200,
        "akku_mah": 5000,
        "display_zoll": 6.7,
        "farben": ["Midnight Black", "Pearl White", "Ocean Blue"],
        "5g_faehig": True,
        "garantie_jahre": 2
    },
    {
        "name": "Kabellose Maus ErgoClick",
        "kategorie": "Technik",
        "preis": 59.99,
        "beschreibung": "Ergonomische Bluetooth-Maus für ganztägiges Arbeiten",
        "verbindung": ["Bluetooth 5.0", "USB-Dongle"],
        "akku_typ": "AA Batterie",
        "dpi_max": 4000,
        "farben": ["Schwarz", "Weiß"],
        "gewicht_kg": 0.09,
        "garantie_jahre": 1
    },
    {
        "name": "4K Monitor ProView 27",
        "kategorie": "Technik",
        "preis": 449.00,
        "beschreibung": "27 Zoll 4K IPS Monitor mit USB-C",
        "display_zoll": 27,
        "aufloesung": "3840x2160",
        "panel_typ": "IPS",
        "anschluesse": ["HDMI 2.1", "DisplayPort 1.4", "USB-C 90W"],
        "display_hz": 60,
        "abmessungen": {"breite_cm": 61, "tiefe_cm": 18, "hoehe_cm": 52},
        "garantie_jahre": 3
    },

    # --- Kategorie: Küche ---
    {
        "name": "Kaffeevollautomat X500",
        "kategorie": "Küche",
        "preis": 450.00,
        "beschreibung": "Vollautomatische Kaffeemaschine mit App-Steuerung",
        "mahlwerk": "Keramik",
        "wassertank_liter": 1.8,
        "smart_home_faehig": True,
        "zubereitungen": ["Espresso", "Cappuccino", "Latte Macchiato", "Americano"],
        "farben": ["Schwarz", "Silber", "Rot"],
        "abmessungen": {"breite_cm": 24, "tiefe_cm": 43, "hoehe_cm": 34},
        "gewicht_kg": 8.5,
        "garantie_jahre": 2
    },
    {
        "name": "Standmixer PowerBlend 1200",
        "kategorie": "Küche",
        "preis": 129.99,
        "beschreibung": "Hochleistungsmixer für Smoothies und Suppen",
        "leistung_watt": 1200,
        "behaelter_liter": 2.0,
        "geschwindigkeitsstufen": 10,
        "material_behaelter": "BPA-freies Tritan",
        "farben": ["Schwarz", "Rot"],
        "garantie_jahre": 3,
        "spuelmaschinengeeignet": True
    },
    {
        "name": "Küchenwaage DigiPrecise",
        "kategorie": "Küche",
        "preis": 24.99,
        "beschreibung": "Digitale Präzisionswaage bis 10kg",
        "max_gewicht_kg": 10,
        "genauigkeit_g": 1,
        "einheiten": ["g", "kg", "oz", "lb"],
        "farben": ["Weiß", "Schwarz"],
        "garantie_jahre": 1
    },

    # --- Kategorie: Möbel ---
    {
        "name": "Ergonomischer Bürostuhl ErgoFlex",
        "kategorie": "Möbel",
        "preis": 199.99,
        "beschreibung": "Atmungsaktiver Netzstoff-Bürostuhl mit Lordosenstütze",
        "farbe": "Schwarz",
        "belastbarkeit_kg": 150,
        "material": "Netzstoff",
        "verstellbar": {
            "sitzhoehe_cm": {"min": 42, "max": 52},
            "armlehnen": True,
            "lordosenstuetze": True,
            "kopfstuetze": False
        },
        "rollen_geeignet_fuer": ["Hartboden", "Teppich"],
        "garantie_jahre": 5
    },
    {
        "name": "Höhenverstellbarer Schreibtisch Flex Pro",
        "kategorie": "Möbel",
        "preis": 349.00,
        "beschreibung": "Elektrisch höhenverstellbarer Schreibtisch mit Memory-Funktion",
        "tischplatte_material": "MDF mit Echtholzfurnier",
        "hoehe_cm": {"min": 68, "max": 118},
        "tischplatte_cm": {"breite": 140, "tiefe": 70},
        "motor": "Dual-Motor",
        "memory_positionen": 4,
        "farben_gestell": ["Weiß", "Schwarz"],
        "farben_platte": ["Eiche", "Weiß", "Schwarz"],
        "belastbarkeit_kg": 80,
        "garantie_jahre": 5
    },
    {
        "name": "Bücherregal Oslo 5-fach",
        "kategorie": "Möbel",
        "preis": 89.99,
        "beschreibung": "Schlichtes Standregal im skandinavischen Stil",
        "abmessungen": {"breite_cm": 80, "tiefe_cm": 30, "hoehe_cm": 180},
        "material": "Spanplatte",
        "farben": ["Weiß", "Eiche Sonoma", "Schwarz"],
        "anzahl_faeden": 5,
        "belastbarkeit_pro_fach_kg": 25,
        "garantie_jahre": 1
    },

    # --- Kategorie: Bücher ---
    {
        "name": "Python für Dummies",
        "kategorie": "Bücher",
        "preis": 25.00,
        "beschreibung": "Einsteigerfreundlicher Python-Kurs für absolute Anfänger",
        "autor": {"vorname": "John", "nachname": "Doe"},
        "isbn": "978-3-16-148410-0",
        "seiten": 450,
        "sprache": "Deutsch",
        "auflage": 3,
        "verlag": "Wiley",
        "themen": ["Python", "Programmierung", "Einsteiger"],
        "erscheinungsjahr": 2022
    },
    {
        "name": "Clean Code",
        "kategorie": "Bücher",
        "preis": 34.99,
        "beschreibung": "Das Standardwerk für sauberen, wartbaren Code",
        "autor": {"vorname": "Robert C.", "nachname": "Martin"},
        "isbn": "978-0-13-235088-4",
        "seiten": 431,
        "sprache": "Englisch",
        "auflage": 1,
        "verlag": "Prentice Hall",
        "themen": ["Software Engineering", "Best Practices", "Refactoring"],
        "erscheinungsjahr": 2008
    },
    {
        "name": "NoSQL Distilled",
        "kategorie": "Bücher",
        "preis": 29.99,
        "beschreibung": "Überblick über NoSQL-Datenbankkonzepte und Einsatzszenarien",
        "autor": {"vorname": "Martin", "nachname": "Fowler"},
        "isbn": "978-0-321-82662-6",
        "seiten": 192,
        "sprache": "Englisch",
        "auflage": 1,
        "verlag": "Addison-Wesley",
        "themen": ["NoSQL", "Datenbanken", "Architektur"],
        "erscheinungsjahr": 2012
    },

    # --- Kategorie: Sport ---
    {
        "name": "Laufschuhe AeroRun Pro",
        "kategorie": "Sport",
        "preis": 119.99,
        "beschreibung": "Leichter Laufschuh mit Carbonplatte für lange Distanzen",
        "groessen": [38, 39, 40, 41, 42, 43, 44, 45, 46],
        "farben": ["Blau/Weiß", "Schwarz/Neon", "Grau/Orange"],
        "gewicht_g": 210,
        "sohle": "Carbonplatte + EVA-Schaum",
        "sprengung_mm": 8,
        "einsatzbereich": ["Straße", "Wettkampf"],
        "garantie_jahre": 1
    },
    {
        "name": "Yoga-Matte ComfortFlow 6mm",
        "kategorie": "Sport",
        "preis": 39.99,
        "beschreibung": "Rutschfeste TPE-Yogamatte mit Ausrichtungslinien",
        "material": "TPE",
        "dicke_mm": 6,
        "abmessungen": {"laenge_cm": 183, "breite_cm": 61},
        "farben": ["Lila", "Blau", "Schwarz", "Grün"],
        "gewicht_kg": 1.1,
        "tragegurt_enthalten": True,
        "garantie_jahre": 1
    },
    {
        "name": "Hantelset Gusseisen 20kg",
        "kategorie": "Sport",
        "preis": 79.99,
        "beschreibung": "Variables Hantelset aus Gusseisen mit Abstandshaltern",
        "gesamtgewicht_kg": 20,
        "scheiben": [
            {"gewicht_kg": 0.5, "anzahl": 4},
            {"gewicht_kg": 1.25, "anzahl": 4},
            {"gewicht_kg": 2.5, "anzahl": 4}
        ],
        "stangen_laenge_cm": 40,
        "material": "Gusseisen",
        "garantie_jahre": 2
    },

    # --- Kategorie: Kleidung ---
    {
        "name": "Merino Wanderhemd HikePro",
        "kategorie": "Kleidung",
        "preis": 79.99,
        "beschreibung": "Atmungsaktives Merinowolle-Hemd für Outdoor-Aktivitäten",
        "material": "100% Merinowolle",
        "groessen": ["XS", "S", "M", "L", "XL", "XXL"],
        "farben": ["Waldgrün", "Steingrau", "Navy"],
        "pflegehinweise": ["Schonwäsche 30°C", "Nicht tumbler", "Liegend trocknen"],
        "zertifizierungen": ["OEKO-TEX Standard 100"],
        "garantie_jahre": 1
    },
    {
        "name": "Regenjacke AquaShield Ultralight",
        "kategorie": "Kleidung",
        "preis": 149.00,
        "beschreibung": "Ultraleichte 3-Lagen-Regenjacke, packbar auf Faustgröße",
        "material_aussen": "Ripstop Nylon",
        "wassersaeule_mm": 20000,
        "atmungsaktivitaet": "15000 g/m²/24h",
        "groessen": ["XS", "S", "M", "L", "XL"],
        "farben": ["Signalrot", "Blau", "Oliv"],
        "packbar": True,
        "gewicht_g": 280,
        "garantie_jahre": 2
    },

    # --- Archiviertes Produkt als Beispiel ---
    {
        "name": "Altes Testprodukt (archiviert)",
        "kategorie": "Technik",
        "preis": 9.99,
        "beschreibung": "Dieses Produkt ist nicht mehr im Sortiment",
        "archiviert": True,
        "grund_archivierung": "Eingestellt"
    }
]

def seed_datenbank():
    print("Überprüfe Datenbank...")
    
    anzahl = db["produkte"].count_documents({})
    
    if anzahl == 0:
        print("Datenbank ist leer. Fülle Testdaten ein...")
        db["produkte"].insert_many(test_produkte)
        print(f"{len(test_produkte)} heterogene Testprodukte erfolgreich angelegt!")
        print("Kategorien: Technik, Küche, Möbel, Bücher, Sport, Kleidung")
        print("Darunter 1 archiviertes Produkt als Beispiel für Soft-Delete.")
    else:
        print(f"Datenbank ist nicht leer. Es gibt bereits {anzahl} Produkte.")
        print("Tipp: Nutze DELETE /produkte um alle zu löschen, dann erneut ausführen.")

if __name__ == "__main__":
    seed_datenbank()