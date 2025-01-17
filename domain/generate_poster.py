from pydantic import BaseModel, Field
from typing import Optional, Union, List

from .activity import Activity

class GeneratePoster(BaseModel):
  type: Optional[str] = Field(default="grid", title="绘图类型", description="绘图类型", example="grid")
  language: Optional[str] = Field(default="english", title="语言", description="语言", example="english")
  year: Optional[str] = Field(default="all", title="年份", description="年份", example="all")
  title: Optional[str] = Field(default="", title="标题", description="标题", example="")
  athlete: Optional[str] = Field(default="", title="运动员", description="运动员", example="")
  backgroundColor: Optional[str] = Field(default="#222222", title="背景颜色", description="背景颜色", example="#222222")
  trackColor: Optional[str] = Field(default="#4DD2FF", title="轨迹颜色", description="轨迹颜色", example="#4DD2FF")
  trackColor2: Optional[str] = Field(default="#4DD2FF", title="轨迹颜色2", description="轨迹颜色2", example="#4DD2FF")  
  textColor: Optional[str] = Field(default="#FFFFFF", title="文本颜色", description="文本颜色", example="#FFFFFF")
  specialColor: Optional[str] = Field(default="#FFFF00", title="特殊颜色", description="特殊颜色", example="#FFFF00")
  specialColor2: Optional[str] = Field(default="#FFFF00", title="特殊颜色2", description="特殊颜色2", example="#FFFF00")
  units: Optional[str] = Field(default="metric", title="单位", description="单位", example="metric")
  specialDistance:  Optional[float] = Field(default=0.0, title="特殊距离", description="特殊距离", example=0.0)
  specialDistance2:  Optional[float] = Field(default=0.0, title="特殊距离2", description="特殊距离2", example=0.0)
  minDistance: Optional[float] = Field(default=0.0, title="最小距离", description="最小距离", example=0.0)
  fileType: Optional[str] = Field(default="png", title="文件类型", description="文件类型", example="png")
  raceColor: Optional[str] = Field(default="#ef5350", title="比赛颜色", description="比赛颜色", example="#ef5350")
  activitys: Union[List[Activity], None] 