from typing import Optional
from fastapi import FastAPI, HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool
    rating: Optional[int] = None


my_post = [
    {"title": "Post 1 title", "content": "This is a text content.", "id": 1},
    {"title": "Post 2 title", "content": "This is another text content.", "id": 2},
]

def get_individual_post(id):
    for post in my_post:
        if post['id'] == id:
            return post
    return None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/posts")
async def get_all_posts():

    return {"all posts": my_post}


@app.get("/posts/{id}")
async def get_post(id: int):
    post = get_individual_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    return {"post": post}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_post.append(post_dict)
    return {"post": post_dict}


@app.put("/posts/:id")
async def update_post(post: Post):
    # print(post)
    return {"post": post}


@app.delete("/posts/:id")
async def delete_post(post: Post):
    # print(post)
    return {"post": post}
