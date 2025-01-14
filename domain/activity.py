from pydantic import BaseModel
from typing import Optional


class Activity(BaseModel):
  activityName: Optional[str] = None
  polyline: Optional[str] = None
  averageHeartrate: Optional[float] = None
  startDateLocal: Optional[str] = None
  elapsedTime: Optional[int] = 0
  distance: Optional[float] = 0
  workoutType: Optional[int] = None