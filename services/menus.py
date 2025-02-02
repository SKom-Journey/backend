from utils.mongodb import db
from models.Menu import Menu
from bson import ObjectId
from utils.construct_menu_entity import construct_menu_entity

tb_name = 'menus'

def update_menu_by_id(id: str, menu: dict):
    db.get_collection(tb_name).update_one(
        {
            "_id": ObjectId(id)
        }, 
        {
            "$set": {
                "title": menu['title'],
                "description": menu['description'],
                "price": int(str(menu['price'])),
                "img": menu['img']
            }
        }
    )
    return menu_by_id(id)

def menus(keyword: str):
    result = []
    data =  db.get_collection(tb_name).find({
        "$or": [
            {
                "title": {
                    "$regex": keyword, 
                    "$options": "i"
                }
            },
            {
                "description": {
                    "$regex": keyword, 
                    "$options": "i"
                }
            }
        ]
    })

    for menu in data:
        result.append(
            Menu(
                id=str(menu['_id']),
                title=menu['title'],
                description=menu['description'],
                price=int(str(menu['price'])),
                img=menu['img']
            )
            .model_dump()
        )
    return result

def find_by_entities(entities: dict):
    result = []
    for menu in db.get_collection(tb_name).find(entities).limit(5):
        result.append(
            Menu(
                id=str(menu['_id']),
                title=menu['title'],
                description=menu['description'],
                price=int(str(menu['price'])),
                img=menu['img']
            )
            .model_dump()
        )
    return result

def create_menu(title: str, description: str, img: str, price: int):
    entities = construct_menu_entity(title, description)
    menu_id = db.get_collection(tb_name).insert_one({"title": title, "description": description, "img": img, "price": int(price), **entities}).inserted_id
    menu = db.get_collection(tb_name).find_one({"_id": ObjectId(menu_id)})
    return Menu(
        id=str(menu['_id']),
        title=menu['title'],
        img=menu['img'],
        price=int(str(menu['price'])),
        description=menu['description'],
    ).model_dump() 

def menu_by_id(id: str):
    data = db.get_collection(tb_name).find_one({"_id": ObjectId(id)})
    return Menu(
        id=str(data['_id']),
        title=data['title'],
        description=data['description'],
        price=int(str(data['price'])),
        img=data['img']
    ).model_dump()

def delete_menu(menu_id: str):
    delete = db.get_collection(tb_name).delete_one({"_id": ObjectId(menu_id)})
    return delete.deleted_count

def menus_by_ids(ids: list[str]):
    result = []
    filter_ids = []

    for menu_id in ids:
        filter_ids.append(ObjectId(menu_id))

    for menu in db.get_collection(tb_name).find({"_id": {"$in": filter_ids}}):
        result.append(
            Menu(
                id=str(menu['_id']),
                title=menu['title'],
                description=menu['description'],
                price=int(str(menu['price'])),
                img=menu['img']
            )
            .model_dump()
        )
    return result

def menus_by_not_in_ids(ids: list[str]):
    result = []
    filter_ids = []

    for menu_id in ids:
        filter_ids.append(ObjectId(menu_id))

    for menu in db.get_collection(tb_name).find({"_id": {"$nin": filter_ids}}):
        result.append(
            Menu(
                id=str(menu['_id']),
                title=menu['title'],
                description=menu['description'],
                price=int(str(menu['price'])),
                img=menu['img']
            )
            .model_dump()
        )
    return result