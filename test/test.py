from chart.track import Track

from chart import (
    grid_drawer,
    poster,
)

from domain.activity import Activity
from domain.generate_poster import GeneratePoster

generatePposter = GeneratePoster()
tracks = []
for i in range(1):
  a = Activity()
  a.polyline = "qjwsF{jwdUNlBr@Shl@s`@`BzEhgCclBhO_HzQ}Pd{@uj@nQkQ`LkEvjAox@p|AqiA`Eq@vKtB|JeWhGeGn^qWpJwDnIiI|H`AbFyMb|A_fArNsFvIzAdDiF|H}Ak@bDqAmAeAgjA^gMbAeBl{@iCrIwB~dDsFV|Hxr@s@jDuJbh@mBLwx@de@oBKyPq@xB"
  a.startDateLocal = "2024-02-10 15:19:38"
  a.distance = 100000
  t = Track()
  t.load_from_activity(a)
  tracks.append(t)

generatePposter.activitys = tracks
generatePposter.title = "Leslie Running"
generatePposter.athlete = "Leslie"

p = poster.Poster()
drawers = grid_drawer.GridDrawer(p)
p.set_tracks(generatePposter.activitys)
p.drawer_type = "title"
p.title =generatePposter.title
p.colors = {
        "background": generatePposter.backgroundColor,
        "track":generatePposter.trackColor,
        "track2":generatePposter.trackColor2,
        "special": generatePposter.specialColor,
        "special2":generatePposter.specialColor2,
        "text": generatePposter.textColor,
    }

p.athlete = generatePposter.athlete
output =  "assets/test_grid.svg"
p.draw(drawers, output)


