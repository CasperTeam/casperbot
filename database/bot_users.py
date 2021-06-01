

from database import db_x

bot = db_x["BOT_USERS"]


async def add_user(user_id):
    await bot.insert_one({"user_id": user_id})


async def check_user(user_id):
    Lol = await bot.find_one({"user_id": user_id})
    if Lol:
        return True
    else:
        return False


async def get_all_users():
    Lol = [s async for s in bot.find()]
    return Lol
