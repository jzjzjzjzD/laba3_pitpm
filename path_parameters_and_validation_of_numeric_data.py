#Импорт Path
#from typing import Annotated

#from fastapi import FastAPI, Path, Query

#app = FastAPI()

#@app.get("/items/{item_id}")
#async def read_items(
#    item_id: Annotated[int, Path(title="The ID of the item to get")],
#    q: Annotated[str | None, Query(alias="item-query")] = None,):
#    results = {"item_id": item_id}
#    if q:
#        results.update({"q": q})
#    return results
#Определите метаданные
#from typing import Annotated

#from fastapi import FastAPI, Path, Query

#app = FastAPI()

#@app.get("/items/{item_id}")
#async def read_items(
#    item_id: Annotated[int, Path(title="The ID of the item to get")],
#    q: Annotated[str | None, Query(alias="item-query")] = None,):
#    results = {"item_id": item_id}
#    if q:
#        results.update({"q": q})
#    return results
#Задайте нужный вам порядок параметров
#from fastapi import FastAPI, Path

#app = FastAPI()

#@app.get("/items/{item_id}")
#async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
#    results = {"item_id": item_id}
#    if q:
#        results.update({"q": q})
#    return results
#Валидация числовых данных: больше или равно
#from typing import Annotated

#from fastapi import FastAPI, Path

#app = FastAPI()


#@app.get("/items/{item_id}")
#async def read_items(
#    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str):
#    results = {"item_id": item_id}
#    if q:
#        results.update({"q": q})
#     return results
