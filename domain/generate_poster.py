from pydantic import BaseModel
from typing import Optional, Union, List

from .activity import Activity

class GeneratePoster(BaseModel):
  type: Optional[str] = "grid"
  language: Optional[str] = "english"
  year: Optional[str] = "all"
  title: Optional[str] = ""
  athlete: Optional[str] = ""
  backgroundColor: Optional[str] = "#222222"
  trackColor: Optional[str] = "#4DD2FF"
  trackColor2: Optional[str] = "#4DD2FF"
  textColor: Optional[str] = "#FFFFFF"
  specialColor: Optional[str] = "#FFFF00"
  specialColor2: Optional[str] = "#FFFF00"
  units: Optional[str] = "metric"
  specialDistance:  Optional[float] = 0.0
  specialDistance2:  Optional[float] = 0.0
  minDistance: Optional[float] = 0.0
  fileType: Optional[str] = "png"
  raceColor: Optional[str] = "#ef5350"
  activitys: Union[List[Activity], None] = None