from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend to call backend from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, put only your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HouseDesignRequest(BaseModel):
    plotSize: str
    location: str
    bhk: int

@app.post("/design")
async def generate_house_design(request: HouseDesignRequest):
    return {
        "model_link_3d": "http://localhost:3000/house_model.jpg"

    }
