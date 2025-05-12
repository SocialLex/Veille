from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/generer")
def generer():
    # Simulation de génération de veille juridique
    nom_fichier = "veille_presentation.pptx"
    chemin_sortie = os.path.join("outputs", nom_fichier)

    # Crée le fichier de sortie (simulé ici)
    os.makedirs("outputs", exist_ok=True)
    with open(chemin_sortie, "w") as f:
        f.write("Fichier PowerPoint généré")

    return {"pptx": nom_fichier}

@app.get("/telecharger/{filename}")
def telecharger(filename: str):
    chemin = os.path.join("outputs", filename)
    return FileResponse(chemin, media_type="application/octet-stream", filename=filename)
