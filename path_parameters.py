#Параметры пути с типами
#from fastapi import FastAPI

#app = FastAPI()


#@app.get("/items/{item_id}")
#async def read_item(item_id):
#    return {"item_id": item_id}
#Преобразование данных 
#Если запустите этот пример и перейдёте по адресу: http://127.0.0.1:8000/items/3, то увидите ответ: {"item_id":3}
# Проверка данных 
#Если откроете браузер по адресу http://127.0.0.1:8000/items/foo, то увидите интересную HTTP-ошибку:
#{
#    "detail": [
#        {
#            "loc": [
#                "path",
#                "item_id"
#            ],
#            "msg": "value is not a valid integer",
#            "type": "type_error.integer"
#        }
#    ]
#}
#из-за того, что параметр пути item_id имеет значение "foo", которое не является типом int.
#Та же ошибка возникнет, если вместо int передать float , например: http://127.0.0.1:8000/items/4.2
#Документация -  http://127.0.0.1:8000/docs
#Порядок имеет значение
#from fastapi import FastAPI

#app = FastAPI()


#@app.get("/users/me")
#async def read_user_me():
#    return {"user_id": "the current user"}


#@app.get("/users/{user_id}")
#async def read_user(user_id: str):
#    return {"user_id": user_id}
#Аналогично, вы не можете переопределить операцию с путем:
#from fastapi import FastAPI

#app = FastAPI()


#@app.get("/users")
#async def read_users():
#    return ["Rick", "Morty"]


#@app.get("/users")
#async def read_users2():
#    return ["Bean", "Elfo"]

#Создание класса Enum
#from enum import Enum

#from fastapi import FastAPI


#class ModelName(str, Enum):
#    alexnet = "alexnet"
#    resnet = "resnet"
#    lenet = "lenet"


#app = FastAPI()


#@app.get("/models/{model_name}")
#async def get_model(model_name: ModelName):
 #   if model_name is ModelName.alexnet:
 #       return {"model_name": model_name, "message": "Deep Learning FTW!"}

 #   if model_name.value == "lenet":
 #       return {"model_name": model_name, "message": "LeCNN all the images"}

 #   return {"model_name": model_name, "message": "Have some residuals"}
#Определение параметра пути
#from enum import Enum

#from fastapi import FastAPI


#class ModelName(str, Enum):
#    alexnet = "alexnet"
#    resnet = "resnet"
#    lenet = "lenet"


#app = FastAPI()


#@app.get("/models/{model_name}")
#async def get_model(model_name: ModelName):
#    if model_name is ModelName.alexnet:
#        return {"model_name": model_name, "message": "Deep Learning FTW!"}

#    if model_name.value == "lenet":
#        return {"model_name": model_name, "message": "LeCNN all the images"}

#    return {"model_name": model_name, "message": "Have some residuals"}
#Работа с перечислениями в Python
#from enum import Enum

#from fastapi import FastAPI


#class ModelName(str, Enum):
#    alexnet = "alexnet"
#    resnet = "resnet"
#    lenet = "lenet"


#app = FastAPI()


#@app.get("/models/{model_name}")
#async def get_model(model_name: ModelName):
#    if model_name is ModelName.alexnet:
#        return {"model_name": model_name, "message": "Deep Learning FTW!"}

#    if model_name.value == "lenet":
#        return {"model_name": model_name, "message": "LeCNN all the images"}

#    return {"model_name": model_name, "message": "Have some residuals"}
#Получение значения перечисления
#from enum import Enum

#from fastapi import FastAPI


#class ModelName(str, Enum):
#    alexnet = "alexnet"
#    resnet = "resnet"
#    lenet = "lenet"


#app = FastAPI()


#@app.get("/models/{model_name}")
#async def get_model(model_name: ModelName):
#    if model_name is ModelName.alexnet:
#        return {"model_name": model_name, "message": "Deep Learning FTW!"}

#    if model_name.value == "lenet":
#        return {"model_name": model_name, "message": "LeCNN all the images"}

#    return {"model_name": model_name, "message": "Have some residuals"}
#Возврат элементов перечисления
#from enum import Enum

#from fastapi import FastAPI


#class ModelName(str, Enum):
#    alexnet = "alexnet"
#    resnet = "resnet"
#    lenet = "lenet"


#app = FastAPI()


#@app.get("/models/{model_name}")
#async def get_model(model_name: ModelName):
#    if model_name is ModelName.alexnet:
#        return {"model_name": model_name, "message": "Deep Learning FTW!"}

#    if model_name.value == "lenet":
#        return {"model_name": model_name, "message": "LeCNN all the images"}

#    return {"model_name": model_name, "message": "Have some residuals"}
#Конвертер пути
#from fastapi import FastAPI

#app = FastAPI()


#@app.get("/files/{file_path:path}")
#async def read_file(file_path: str):
#    return {"file_path": file_path}
