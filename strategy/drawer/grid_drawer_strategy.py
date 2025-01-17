
import os
import uuid
from datetime import datetime


from chart import (
    grid_drawer,
    poster,
)

from .drawer_strategy import DrawerStrategy

class GridDrawerStrategy(DrawerStrategy):
  def draw(self, poster: poster.Poster):
    # 判断文件夹是否存在
    if not os.path.exists("assets/grid"):
        # 如果文件夹不存在，创建文件夹
        os.makedirs("assets/grid")
    poster.drawer_type = "title"
    drawers = grid_drawer.GridDrawer(poster)
    timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    unique_id = str(uuid.uuid4())
    output = f"assets/grid/{timestamp}-{unique_id}.svg"
    poster.draw(drawers, output)
    return output