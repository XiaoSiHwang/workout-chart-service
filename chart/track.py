"""Create and maintain info about a given activity track (corresponding to one GPX file)."""

# Copyright 2016-2019 Florian Pigorsch & Contributors. All rights reserved.
# 2019-now yihong0618 Florian Pigorsch & Contributors. All rights reserved.
# Use of this source code is governed by a MIT-style
# license that can be found in the LICENSE file.

import datetime
from datetime import timezone
import os
from collections import namedtuple

import gpxpy as mod_gpxpy
import lxml
import polyline
import s2sphere as s2
from garmin_fit_sdk import Decoder, Stream
from garmin_fit_sdk.util import FIT_EPOCH_S
from polyline_processor import filter_out
from rich import print
from tcxreader.tcxreader import TCXReader

from .exceptions import TrackLoadError
from .utils import parse_datetime_to_local
from domain.activity import Activity

start_point = namedtuple("start_point", "lat lon")
run_map = namedtuple("polyline", "summary_polyline")

IGNORE_BEFORE_SAVING = os.getenv("IGNORE_BEFORE_SAVING", False)

# Garmin stores all latitude and longitude values as 32-bit integer values.
# This unit is called semicircle.
# So that gives 2^32 possible values.
# And to represent values up to 360° (or -180° to 180°), each 'degree' represents 2^32 / 360 = 11930465.
# So dividing latitude and longitude (int32) value by 11930465 will give the decimal value.
SEMICIRCLE = 11930465

class Track:
  def __init__(self):
    ## 文件名
    self.file_names = []
    ## 坐标列表
    self.polylines = []
    ## 坐标压缩转换后的坐标字符串
    self.polyline_str = ""
    ## 运动名称
    self.track_name = None
    ## 运动开始时间
    self.start_time = None
    ## 运动结束时间
    self.end_time = None
    ## 运动开始当地时间
    self.start_time_local = None
    ## 运动结束当地时间
    self.end_time_local = None
    ## 距离长度
    self.length = 0
    self.special = False
    ## 平均心率
    self.average_heartrate = None
    self.moving_dict = {}
    ## 需要重构属性名
    self.run_id = 0
    self.start_latlng = []
    self.type = "Run"
    self.subtype = None  # for fit file
    self.device = ""
    self.workout_type = None


  def load_from_activity(self, activity: Activity):
    # use strava as file name
    self.file_names = [str(activity.activityName)]
    start_time = datetime.datetime.strptime(
        activity.startDateLocal, "%Y-%m-%d %H:%M:%S"
    )
    self.start_time_local = start_time
    self.end_time = start_time + datetime.timedelta(seconds=activity.elapsedTime)
    self.length = float(activity.distance)
    if IGNORE_BEFORE_SAVING:
        summary_polyline = filter_out(activity.polyline)
    else:
        summary_polyline = activity.polyline
    polyline_data = polyline.decode(summary_polyline) if summary_polyline else []
    self.polylines = [[s2.LatLng.from_degrees(p[0], p[1]) for p in polyline_data]]
    self.workout_type = activity.workoutType

  
  def bbox(self):
        """Compute the smallest rectangle that contains the entire track (border box)."""
        bbox = s2.LatLngRect()
        for line in self.polylines:
            for latlng in line:
                bbox = bbox.union(s2.LatLngRect.from_point(latlng.normalized()))
        return bbox
