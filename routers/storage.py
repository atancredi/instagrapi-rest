import mysql.connector as msc
from os import environ as env

from typing import List, Optional
from pathlib import Path

from fastapi import APIRouter, Depends, Form
from fastapi.responses import FileResponse
from instagrapi import Client
from instagrapi.types import Story, UserShort

from dependencies import ClientStorage, get_clients
from pydantic import BaseModel


router = APIRouter(
    prefix="/storage",
    tags=["storage"],
    responses={404: {"description": "Not found"}},
)

class MysqlConfig:
    host = env.get("MYSQL_HOST")
    user = env.get("MYSQL_USER")
    password = env.get("MYSQL_PASSWORD")
    db = env.get("MYSQL_DATABASE")

############## UPDATE USER FOLLOWERS


# ritorna il risultato della scansione con followers presi e persi
@router.post("/update_user_followers", response_model=int)
async def update_user_followers(user_id: int = Form(...),
                                followers_ids: List[int] = Form(...)):
    """Update the stored list of followers for an user after a scan
    """
    conf = MysqlConfig()
    msc.connect(
      host=conf.host,
      user=conf.user,
      password=conf.password,
      db=conf.db
    )

    #qui devo vedere prima i followers persi (sono nel db ma non sono in lista)
    #e poi i followers guadagnati (sono in lista ma non sono nel db)

    for follower in followers_ids:
      #query: where user_id=user_id && follower_id=follower
      pass
    


############## GET STORED USER FOLLOWERS