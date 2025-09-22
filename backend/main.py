from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Coucou"}

# get /todos (liste toute les todos)
# post /todo (creer une todo)
# put /todo (fait ou non)

