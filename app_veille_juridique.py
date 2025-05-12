from fastapi import FastAPI
from fastapi.responses import FileResponse
from veille_generator import generer_veille
import datetime

app = FastAPI()

@app.get("/generer")
def generer():
    date_str = datetime.date.today().strftime("%B_%Y")
    pptx_file, script_file = generer_veille(date_str)
    return {"pptx": f"/telecharger/{pptx_file}", "script": f"/telecharger/{script_file}"}

@app.get("/telecharger/{filename}")
def telecharger(filename: str):
    return FileResponse(f"outputs/{filename}")
from pptx import Presentation
from pptx.util import Inches, Pt
from datetime import datetime
