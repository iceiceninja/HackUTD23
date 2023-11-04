from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#   uvicorn main:app --reload

app = FastAPI()

# Configure CORS settings
origins = [
    "http://127.0.0.1:3000",  # Replace with the actual address of your JavaScript code
    "http://localhost:3000",  # Add any other origins you want to allow
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    # Add any other origins you want to allow
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # You can specify specific HTTP methods (e.g., ["GET", "POST"])
    allow_methods=["*"],
    allow_headers=["*"],  # You can specify specific headers
)
total = 0

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
async def hello():
    global total
    total += 1
    return {"message": str(total) + " hello"}
