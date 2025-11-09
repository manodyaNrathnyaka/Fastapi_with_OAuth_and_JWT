from fastapi import FastAPI
from pydantic import BaseModel

class Profile(BaseModel):
    username: str
    age: int
    email: str
    
    
class Product(BaseModel):
    name:str
    price:int
    discount:int
    discounted_price:int 
    
    
class User(BaseModel):
    username:str
    email:str

app=FastAPI() #creating instance of FastAPI class

@app.post("/purchase")
def purchase(user:User,product:Product):
    return{"user":user,"product":product}


@app.post("/addproduct/{product_id}")
def addproduct(product:Product, product_id:int, category:str):
    product.discounted_price=product.price-(product.discount*product.price)/100
    return {"product_id":product_id,"product":product,'category':category}
        

@app.get('/user/admin')
def admin():
    return{"This is the admin profile"}

@app.get("/user/{username}")
def profile(username: str):
    return{f"This is the {username} profile"}

@app.get('/product')
def products(id:int=1,price:int=None):
    return {f'product with an id:{id} and price :{price}'}

@app.get("/profile/{user_id}/comments")
def profile(user_id:int,commentid:int):
    return {f"This is the profile of user with id:{user_id} and comment id is {commentid}"}

@app.post("/adduser")
def adduser(profile:Profile):
    return profile
