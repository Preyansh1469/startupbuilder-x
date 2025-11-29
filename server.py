from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.get("/api/status")
def status():
    return {"status": "running", "message": "StartupBuilder X Backend Active"}
