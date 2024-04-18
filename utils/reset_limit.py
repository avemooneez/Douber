from db import Database
import apscheduler

db = Database("./database.db")

async def reset():
    db.reset_limit()
