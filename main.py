from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from apps.calculator.route import router as calculator_router
from constants import SERVER_URL, PORT, ENV

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['https://calcai.netlify.app'],  # Allow only your frontend
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Specify allowed methods
    allow_headers=["Content-Type", "Authorization"],  # Allowed headers
)


@app.get('/')
async def root():
    return {"message": "Server is running"}

app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])


if __name__ == "__main__":
    if ENV == "production":
        HOST = SERVER_URL
    else:
        HOST = "127.0.0.1"  # Use localhost in development

    uvicorn.run("main:app", host=HOST, port=int(PORT), reload=(ENV != "production"))

    # uvicorn.run("main:app", host=SERVER_URL, port=int(PORT), reload=(ENV == "production"))
