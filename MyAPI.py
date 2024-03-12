from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS para permitir acceso desde todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/nombres")
async def obtener_nombres():
    return ["Juan", "María", "Pedro"]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
