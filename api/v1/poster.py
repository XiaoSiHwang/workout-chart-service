from fastapi import APIRouter
from fastapi.responses import StreamingResponse, JSONResponse

from utils.export_file_utils import export
from chart.track import Track
from domain.generate_poster import GeneratePoster
from chart import (
    poster,
)
from strategy.drawer import (
   grid_drawer_strategy,
   drawer_strategy_context
)
from logger.log import logger

router = APIRouter()

@router.post("/v1/poster", summary='运动绘图',description='运动绘图',tags=['V1运动绘图'])
def read_root(generate_poster: GeneratePoster):
    p = poster.Poster()
    tracks = []
    for activity in generate_poster.activitys:
      t = Track()
      if t.load_from_activity(activity, generate_poster.type) is not None:
        tracks.append(t)
    if len(tracks) == 0:
      logger.error("[V1运动绘图]-运动绘图为空无法绘图！！")
      return  JSONResponse(status_code=500, content={"message": "drawer tracks is empty!"})
    p.set_tracks(tracks)
    p.title =generate_poster.title
    p.colors = {
            "background": generate_poster.backgroundColor,
            "track":generate_poster.trackColor,
            "track2":generate_poster.trackColor2,
            "special": generate_poster.specialColor,
            "special2":generate_poster.specialColor2,
            "text": generate_poster.textColor,
            "race": generate_poster.raceColor,
        }
    p.special_distance = {"special_distance": generate_poster.specialDistance, "special_distance2": generate_poster.specialDistance2}
    p.athlete = generate_poster.athlete

    drawer_type = {
       "grid": grid_drawer_strategy.GridDrawerStrategy()
    }
    
    context = drawer_strategy_context.DrawerStrategyContext(drawer_type[generate_poster.type])
    output = context.draw(poster=p)
    chart_file = export(generate_poster.fileType, output)
    return StreamingResponse(chart_file)
