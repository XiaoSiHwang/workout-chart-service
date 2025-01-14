from .drawer_strategy import DrawerStrategy
from chart.poster import Poster


class DrawerStrategyContext:
  def __init__(self, strategy: DrawerStrategy):
    self.strategy = strategy
  
  def set_strategy(self, strategy: DrawerStrategy):
    self.strategy = strategy

  def draw(self, poster: Poster):
    return self.strategy.draw(poster=poster)