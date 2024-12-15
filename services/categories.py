from utils.mongodb import db
from models.Category import Category
from bson import ObjectId
from datetime import datetime

tb_name = 'categories'

def create_category(name):
    category_id = db.get_collection(tb_name).insert_one({"name": name, "created_at": datetime.now()}).inserted_id
    category = db.get_collection(tb_name).find_one({"_id": ObjectId(category_id)})
    return Category(
        name = str(category['name']),
        id = str(category['_id']),
        created_at = category['created_at'].isoformat(),
    ).model_dump()

def get_category_by_name(name):
    category = db.get_collection(tb_name).find_one({"name": name})
    if category == None:
        return None
    return Category(
        name = str(category['name']),
        id = str(category['_id']),
        created_at = category['created_at'].isoformat(),
    ).model_dump()

def get_category_by_id(id: str):
    category = db.get_collection(tb_name).find_one({"_id": ObjectId(id)})
    if category == None:
        return None
    return Category(
        name = str(category['name']),
        id = str(category['_id']),
        created_at = category['created_at'].isoformat(),
    ).model_dump()

def update_category_by_id(id: str, name: str):
    db.get_collection(tb_name).update_one(
        {
            "_id": ObjectId(id)
        }, 
        {
            "$set": {
                "name": name
            }
        }
    )
    return get_category_by_id(id)

def get_categories():
    result = []
    for category in db.get_collection(tb_name).find():
        result.append(
            Category(
                name = str(category['name']),
                id = str(category['_id']),
                created_at = category['created_at'].isoformat(),
            ).model_dump()
        )
    return result

def delete_category(id: str):
    delete = db.get_collection(tb_name).delete_one({"_id": ObjectId(id)})
    return delete.deleted_count