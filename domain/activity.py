from pydantic import BaseModel, Field
from typing import Optional


class Activity(BaseModel):
  activityName: Optional[str] = Field(default=None, title="运动名称", description="运动名称", example="晨间运动")
  polyline: Optional[str] = Field(default=None, title="运动轨迹", description="运动轨迹", example="mtjlCegcsTKGq@I_@C[@w@F]FOHOTG\BJVXXPRFrABn@El@?XEVMFGJO?SGe@MYGG[GeAI[@y@C[@QB[TQh@BZJ^ZRl@FrBCZCn@OJKF]?MI_@[_@KC_A?s@GaA?c@LIFUt@@VLXRRJBl@Dx@ENBf@Ah@IVKDELUDUAQM[QWMA}AGo@As@B[LIDKNILCh@BNNTXNH@\DbBIN?ZFJALEh@g@DG@[CQW_@g@Ss@Hq@@YE[DY?YJSRI\?R@HLZNHb@JP?t@Ld@CdAAPETOPWB]Mi@SWQM_BAcB@KB[PYh@CN@LLXLL^Nh@@jC?TE\SLUD]C[EKSSWK]GWB}@@kABWHKLOZEZDXNXZLXB\?^B`@EjAGPCTON]@MASQ_@GI")
  averageHeartrate: Optional[float] = Field(default=None, title="平均心率", description="平均心率", example="140")
  startDateLocal: Optional[str] = Field(default=None, title="开始时间", description="开始时间", example="2023-07-20 13:12:33")
  elapsedTime: Optional[int] = Field(default=0, title="运动时长", description="运动时长", example="100")
  distance: Optional[float] = Field(default=0, title="运动距离", description="运动距离", example="1000")
  workoutType: Optional[int] = Field(default=None, title="活动类型", description="运动类型", example="1 or 11（比赛）其他数字都是普通类型主要是为了兼容Strava平台")
  type: Optional[str]=Field(default=None, title="运动类型", description="运动类型", example="Run")