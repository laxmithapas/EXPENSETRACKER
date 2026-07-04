from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


class Expense(BaseModel):
    food: int
    travel: int
    shopping: int



@app.post("/calculate")
def calculate(expense: Expense):

    total = (
        expense.food
        +
        expense.travel
        +
        expense.shopping
    )


    return {
        "total": total
    }