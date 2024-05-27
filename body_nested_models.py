#Определение полей содержащих списки
#from fastapi import FastAPI
#from pydantic import BaseModel

#app = FastAPI()

#class Item(BaseModel):
#    name: str
#    description: str | None = None
#    price: float
#    tax: float | None = None
#    tags: list = []

#app.put("/items/{item_id}")
#async def update_item(item_id: int, item: Item):
#    results = {"item_id": item_id, "item": item}
#    return results

#Импортируйте List из модуля typing
#from typing import List, Union
#from fastapi import FastAPI
#from pydantic import BaseModel

#app = FastAPI()

#class Item(BaseModel):
#    name: str
#    description: Union[str, None] = None
#    price: float
#    tax: Union[float, None] = None
#    tags: List[str] = []

#@app.put("/items/{item_id}")
#async def update_item(item_id: int, item: Item):
#    results = {"item_id": item_id, "item": item}
#    return results

#Объявление list с указанием типов для вложенных элементов
#from fastapi import FastAPI
#from pydantic import BaseModel

#app = FastAPI()

#class Item(BaseModel):
#    name: str
#    description: str | None = None
#    price: float
#    tax: float | None = None
#    tags: list[str] = []


#@app.put("/items/{item_id}")
#async def update_item(item_id: int, item: Item):
#    results = {"item_id": item_id, "item": item}
#    return results

#Типы множеств
#from fastapi import FastAPI
#from pydantic import BaseModel

#app = FastAPI()

#class Item(BaseModel):
#    name: str
#    description: str | None = None
#    price: float
#    tax: float | None = None
#    tags: set[str] = set()

#@app.put("/items/{item_id}")
#async def update_item(item_id: int, item: Item):
#    results = {"item_id": item_id, "item": item}
#    return results

#Вложенные Модели
#Определение подмодели
#from fastapi import FastAPI
#from pydantic import BaseModel

#app = FastAPI()

#class Image(BaseModel):
#    url: str
#    name: str

#class Item(BaseModel):
#    name: str
#    description: str | None = None
#    price: float
#    tax: float | None = None
#    tags: set[str] = set()
#    image: Image | None = None

#@app.put("/items/{item_id}")
#async def update_item(item_id: int, item: Item):
#    results = {"item_id": item_id, "item": item}
#    return results

#Использование вложенной модели в качестве типа
#from fastapi import FastAPI
#from pydantic import BaseModel

#app = FastAPI()

#class Image(BaseModel):
#    url: str
#    name: str

#class Item(BaseModel):
#    name: str
#    description: str | None = None
#    price: float
#    tax: float | None = None
#    tags: set[str] = set()
#    image: Image | None = None

#@app.put("/items/{item_id}")
#async def update_item(item_id: int, item: Item):
#    results = {"item_id": item_id, "item": item}
#    return results

#Особые типы и валидация
#from fastapi import FastAPI
#from pydantic import BaseModel, HttpUrl

#app = FastAPI()

#class Image(BaseModel):
#    url: HttpUrl
#    name: str

#class Item(BaseModel):
#    name: str
#    description: str | None = None
#    price: float
#    tax: float | None = None
#    tags: set[str] = set()
#    image: Image | None = None

#@app.put("/items/{item_id}")
#async def update_item(item_id: int, item: Item):
#    results = {"item_id": item_id, "item": item}
#    return results

#Атрибуты, содержащие списки подмоделей
#from fastapi import FastAPI
#from pydantic import BaseModel, HttpUrl

#app = FastAPI()

#class Image(BaseModel):
#    url: HttpUrl
#    name: str

#class Item(BaseModel):
#    name: str
#    description: str | None = None
#    price: float
#    tax: float | None = None
#    tags: set[str] = set()
#    images: list[Image] | None = None

#@app.put("/items/{item_id}")
#async def update_item(item_id: int, item: Item):
#    results = {"item_id": item_id, "item": item}
#    return results

#Глубоко вложенные модели
#from typing import Union

#from fastapi import FastAPI
#from pydantic import BaseModel, HttpUrl

#app = FastAPI()

#class Image(BaseModel):
#    url: HttpUrl
#    name: str

#class Item(BaseModel):
#    name: str
#    description: Union[str, None] = None
#    price: float
#    tax: Union[float, None] = None
#    tags: set[str] = set()
#    images: Union[list[Image], None] = None

#class Offer(BaseModel):
#    name: str
#    description: Union[str, None] = None
#    price: float
#    items: list[Item]

#@app.post("/offers/")
#async def create_offer(offer: Offer):
#    return offer

#Тела с чистыми списками элементов
#from fastapi import FastAPI
#from pydantic import BaseModel, HttpUrl

#app = FastAPI()

#class Image(BaseModel):
#    url: HttpUrl
#    name: str

#@app.post("/images/multiple/")
#async def create_multiple_images(images: list[Image]):
#    return images

#Тела запросов с произвольными словарями (dict)
#from fastapi import FastAPI

#app = FastAPI()

#@app.post("/index-weights/")
#async def create_index_weights(weights: dict[int, float]):
#    return weights

