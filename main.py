from fastapi import FastAPI, Depends, HTTPException, Query, status


app = FastAPI()

@app.get("/Heater/Ping", status_code=status.HTTP_200_OK)
def ping():
    return {}

@app.get("/Heater/Request/{card_id}", status_code=status.HTTP_200_OK)
def request(card_id: str):
    print(card_id)
    return {}
