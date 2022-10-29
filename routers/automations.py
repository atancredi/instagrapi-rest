from datetime import datetime
from tokenize import Intnumber
from typing import List, Optional, Tuple
from pathlib import Path
import json

import mysql.connector as msc
from os import environ as env

from fastapi import APIRouter, Depends, Form
from fastapi.responses import FileResponse
from instagrapi import Client
from instagrapi.types import Story, UserShort

from dependencies import ClientStorage, get_clients
from pydantic import BaseModel

class StoryAutomation(BaseModel):

    story: Story = None
    viewers: List[UserShort] = None

    def __init__(self):
        pass


class MysqlConfig:

    def __init__(self):
        
        self.host = env.get("MYSQL_HOST")
        self.user = env.get("MYSQL_USER")
        self.password = env.get("MYSQL_PASSWORD")
        self.db = env.get("MYSQL_DATABASE")

router = APIRouter(
    prefix="/automations",
    tags=["automations"],
    responses={404: {"description": "Not found"}},
)

# get list of followers for an user
class ScanReturnLists:
    gained_followers: List[Tuple]
    lost_followers: List[Tuple]
    total_followers: List[Tuple]
class ScanReturn:
    id: int
    gained_followers: int
    lost_followers: int
    total_followers: int
    lists: ScanReturnLists
    date: datetime


# get list of user stories and their viewers
@router.post("/stories", response_model=List[StoryAutomation])
async def story_user_stories(sessionid: str = Form(...), 
                            user_id: str = Form(...), 
                            amount: Optional[int] = Form(None), 
                            clients: ClientStorage = Depends(get_clients),
                            save_to_db: Optional[bool] = Form(False)) -> List[Story]:
    """Get a user's stories
    """
    # cl = clients.get(sessionid)
    # stories = cl.user_stories(user_id, amount)
    # ret = []
    # for story in stories:
    #     data = StoryAutomation()
    #     data.story = story
    #     data.viewers = cl.story_viewers(story.pk)
    #     ret.append(data)

    # if save_to_db:
        
    #     conf = MysqlConfig()
    #     msc.connect(
    #         host=conf.host,
    #         user=conf.user,
    #         password=conf.password,
    #         db=conf.db
    #     )
    #     return None
    
    # return ret

    pass
    
