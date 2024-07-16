from fastapi import FastAPI
from config import engine
import model
import router
model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def Home():
    return "Welcome Home"
app.include_router(router.router, prefix="/pokemon", tags=['pokemon'])
