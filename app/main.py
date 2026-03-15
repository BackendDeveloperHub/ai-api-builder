from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import router

app = FastAPI(
    title= "AI API BUILDER",
    description= "GENERATE AI APIS USING  AI",
    version= "1.0"
)
app.include_router(router)
# Static files — LAST la mount pannu
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")
