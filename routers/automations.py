from typing import List, Optional
from pathlib import Path

from fastapi import APIRouter, Depends, Form
from fastapi.responses import FileResponse
from instagrapi import Client
from instagrapi.types import Story, UserShort, StoryAutomation

from dependencies import ClientStorage, get_clients
from pydantic import BaseModel


router = APIRouter(
    prefix="/automations",
    tags=["automations"],
    responses={404: {"description": "Not found"}},
)

# get list of user stories and their viewers
@router.post("/stories", response_model=List[StoryAutomation])
async def story_user_stories(sessionid: str = Form(...), 
                            user_id: str = Form(...), 
                            amount: Optional[int] = Form(None), 
                            clients: ClientStorage = Depends(get_clients)) -> List[Story]:
    """Get a user's stories
    """
    cl = clients.get(sessionid)
    stories = cl.user_stories(user_id, amount)
    ret = []
    for story in stories:
        data = StoryAutomation()
        data.story = story
        data.viewers = cl.story_viewers(story.pk)
        ret.append(data)
    return ret
    
