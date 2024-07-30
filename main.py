from fastapi import FastAPI

app = FastAPI(
    title="SHIFTER: Flashcards app"
)

@app.get("/home")
def get_home():
    return "HOMEPAGE"