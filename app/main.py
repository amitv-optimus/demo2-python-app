from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Serve static files (Frontend)
app.mount("/static", StaticFiles(directory="."), name="static")


@app.get("/")
async def serve_frontend():
    """ Serve index.html when visiting the root URL """
    return FileResponse("index.html")

