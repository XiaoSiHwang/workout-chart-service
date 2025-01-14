import cairosvg
import os
from html2image import Html2Image


def ImportImageFromExecl(filepath, outputPNGImage):
    hti = Html2Image( size=(1574, 2362))
    hti.screenshot(
        other_file=filepath,
        # css_str=[' body {zoom: 4;}'],
        save_as=outputPNGImage
    )
    
filepath = "/Users/leslie/Desktop/Python-Project/workout-chart-service/assets/grid/2025-01-12-21:58:44-0e3f1ad1-11cb-4fd9-b4e4-2f9967b6569d.svg"
outputPNGImage = 'test.png'

ImportImageFromExecl(filepath, outputPNGImage) 
 
# svg_path = 'assets/test_grid.svg'
# png_path = 'assets/test_grid.png'
# cairosvg.svg2png(url=svg_path, write_to=png_path, dpi=200)


# from PIL import Image
# from io import BytesIO
# def convert_svg_to_image(svg_path, output_path, format='PNG'):
# # 打开SVG文件并读取内容
#   with open(svg_path, 'r') as file:
#     svg_content = file.read()
#   # 将SVG内容转换为Pillow图像对象
#   image = Image.open(BytesIO(svg_content.encode()))
#   # 保存为指定格式
#   image.save(output_path, format=format)
#   # 使用示例

# convert_svg_to_image('/Users/leslie/Desktop/Python-Project/workout-chart-service/assets/test_grid.svg', 'assets/test_grid2.png')
