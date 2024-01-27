from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}


@app.get("/")
def root():
    return {"message": "Hello, User!"}


@app.post('/post', response_model=List[Dog])
def get_post():
    return dogs_db.values()

@app.get('/dog', response_model=List[Dog])
def get_dogs(kind: DogType = None):
    final_dogs = []
    if kind:
        for i in dogs_db.values():
            if i.kind == kind:
                final_dogs.append(i)
        return final_dogs
    else:
        return list(dogs_db.values())

@app.post('/dog', response_model=Dog)
def create_dog(dog: Dog):
    pk = max(dogs_db.keys()) + 1
    dog.pk = pk
    dogs_db[pk] = dog
    return dog

@app.get('/dog/{pk}', response_model=Dog)
def get_dog_by_pk(pk: int):
    return dogs_db[pk]

@app.patch('/dog/{pk}', response_model=Dog)
def update_dog(pk: int, new_dog: Dog):
    dogs_db[pk].name = new_dog.name
    dogs_db[pk].kind = new_dog.kind
    return dogs_db[pk]

