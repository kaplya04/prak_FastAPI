from typing import Union
from fastapi import FastAPI
from app.model import core
from app.model.database import engine
from app.routers.router import router as comic_router


core.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(
    router=comic_router
)



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/comic/{comic_id}")
def read_comic(comic_id: int, q: Union[str, None] = None):
    return {"comic_id": comic_id, 'q': q}
