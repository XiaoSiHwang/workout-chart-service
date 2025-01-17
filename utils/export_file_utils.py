import os
import uuid
from datetime import datetime

import cairosvg

def export(file_type, svg_file_path):
  output_file = ""
  output = None
  if file_type == "svg":
    output_file = svg_file_path
  elif file_type == "png":
    # 判断文件夹是否存在
    if not os.path.exists("assets/png"):
        # 如果文件夹不存在，创建文件夹
        os.makedirs("assets/png")
    timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    unique_id = str(uuid.uuid4())
    output_file = f"assets/png/{timestamp}-{unique_id}.png"
    cairosvg.svg2png(url=svg_file_path, write_to=output_file, dpi=200)
    output =  open(output_file, mode="rb")
    # os.remove(svg_file_path)
    # os.remove(output_file)
    return output
  else:
    output_file = svg_file_path
  output =  open(output_file, mode="rb")
  # os.remove(svg_file_path)
  return output