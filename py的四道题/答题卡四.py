# 导入PIL模块
import PIL
from PIL import Image 
# 打开论文图片
img = Image.open("R-C.gif")
# 利用convert函数将图片转化为RGB模式
rgb_img = img.convert('RGB')

# 利用size()方法获取图片的宽度和高度
# 将宽度、高度分别赋值给变量width，height

width, height = rgb_img.size

# for循环遍历图片中每个像素点
for i in range(width):
    for j in range(height):
        # 这是坐标
        pos = (i,j)
        if sum(rgb_img.getpixel(pos)) >= 540:
            # 设置此点像素值为(255,255,255)
            rgb_img.putpixel(pos, (255,255,255))
            
# 将图片保存下来
rgb_img.save("R-C2.gif")

