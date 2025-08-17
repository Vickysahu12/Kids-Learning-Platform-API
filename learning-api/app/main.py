from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

class VideoCategory(str, Enum):
    math = "math"
    science = "science"
    english = "english"

class Video(BaseModel):
    title: str
    subject: str
    duration: int

@app.get("/")
async def project_title():
    return {"message": "Kids-Learning-API backend"}

@app.get("/videos")
async def fetch_all_videos():
    return {"response": "Fetching all videos"}

@app.get("/videos/{video_id}")
async def fetch_single_video(video_id: int):
    return {"response": f"Fetching video with id {video_id}"}

@app.post("/videos")
async def insert_video(video: Video):
    return {"response": "Video inserted", "video": video}

@app.put("/videos/{video_id}")
async def update_video(video_id: int, video: Video):
    return {"response": f"Video {video_id} updated", "video": video}

@app.patch("/videos/{video_id}")
async def partial_update_video(video_id: int, updated_video: dict):
    return {"response": f"Video {video_id} partially updated", "update": updated_video}

@app.delete("/videos/{video_id}")
async def video_delete(video_id: int):
    return {"message": f"Video with id {video_id} deleted successfully"}

@app.get("/videos/category/{category}")
async def fetch_video_category(category: VideoCategory):
    return {"message": f"{category.value} videos are awesome"}

@app.get("/videos/student/{student_name}")
async def fetch_student_data(student_name: str):
    return {"message": f"Student name: {student_name}"}
