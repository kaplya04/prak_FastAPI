from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.model.schemas import ComicsShemas, CategoryShemas

app = FastAPI()

comic = []
category = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/comics/")
async def create_comic(comic: ComicsShemas):
    comic.append(comic)
    return {"massage", 'Комикс создан'}


@app.get("/comics/")
async def get_comic():
    return {"comics": comic}


@app.get("/comics/{comics_id}")
async def get_comics(comics_id: int):
    if comics_id < len(comic):
        return {"comics": comic[comics_id]}
    else:
        return {"error": "Комикс не найден"}


@app.delete("/comics/{comics_id}")
async def delete_comics(comics_id: int):
    if comics_id < len(comic):
        comic.pop(comics_id)
        return {"message": "Комикс удалён"}
    else:
        return {"error": "Комикс не найден"}


@app.put("/comics/{comics_id}")
async def update_comics(comics_id: int, comic: ComicsShemas):
    if comics_id < len(comic):
        comic[comics_id] = comic
        return {"message": "Информация обновлена"}
    else:
        return {"error": "Комикс не найден"}


@app.post("/category/")
async def create_category(category: CategoryShemas):
    category.append(category)
    return {"message": "Категория создана"}


@app.get("/category/")
async def get_category():
    return {"Category": CategoryShemas}


@app.get("/comics{category_id}")
async def get_comics_by_category(category_id: int):
    category_d = [com for com in comic if com.category_id == category_id]
    return {"Category": category_d}
