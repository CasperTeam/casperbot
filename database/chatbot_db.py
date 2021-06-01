

from database import db_x

chatbot_user_db = db_x["chatbotuserdb"]
cbb = db_x["blacklisted_users"]


async def add_chatbotuser(user_id):
    await chatbot_user_db.insert_one({"user_id": user_id})


async def rmchatbotuser(user_id):
    await chatbot_user_db.delete_one({"user_id": user_id})


async def get_all_chatbotusers():
    lol = [ko async for ko in chatbot_user_db.find()]
    return lol


async def is_chatbotuser_in_db(user_id):
    k = await chatbot_user_db.find_one({"user_id": user_id})
    if k:
        return True
    else:
        return False


async def add_blacklisted_user(user_id):
    await cbb.insert_one({"user_id": user_id})


async def rm_blacklisted_user(user_id):
    await cbb.delete_one({"user_id": user_id})


async def is_user_blacklisted(user_id):
    b = await cbb.find_one({"user_id": user_id})
    if b:
        return True
    else:
        return False
