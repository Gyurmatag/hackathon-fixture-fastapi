import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="FastAPI fixture")


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return "<!doctype html><title>FastAPI fixture</title><h1>FastAPI fixture</h1><p>Served by uvicorn.</p>"


@app.get("/api/info")
def info() -> dict:
    return {"ok": True, "commit": os.environ.get("HK_COMMIT")}
