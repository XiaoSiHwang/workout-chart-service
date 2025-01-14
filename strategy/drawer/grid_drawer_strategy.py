
import uuid
from datetime import datetime


from chart import (
    grid_drawer,
    poster,
)

from .drawer_strategy import DrawerStrategy

class GridDrawerStrategy(DrawerStrategy):
  def draw(self, poster: poster.Poster):
    poster.drawer_type = "title"
    drawers = grid_drawer.GridDrawer(poster)
    timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    unique_id = str(uuid.uuid4())
    output = f"assets/grid/{timestamp}-{unique_id}.svg"
    poster.draw(drawers, output)
    return output