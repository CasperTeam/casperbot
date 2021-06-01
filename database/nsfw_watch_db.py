

from database import db_x

nsfw = db_x["NSFW_WATCH"]


async def add_chat(chat_id):
    await nsfw.insert_one({"chat_id": chat_id})


async def rm_chat(chat_id):
    await nsfw.delete_one({"chat_id": chat_id})


async def get_all_nsfw_chats():
    lol = [kek async for kek in nsfw.find({})]
    return lol


async def is_chat_in_db(chat_id):
    k = await nsfw.find_one({"chat_id": chat_id})
    if k:
        return True
    else:
        return False
