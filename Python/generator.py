# _*_ coding : UTF-8 _*_
# author : cfl
# time   : 2020/2/16 下午7:08
"""
替换图片为指定文字
"""
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def generate_new_image(origin_path, new_path, font_path, text, font_size):
    img_origin = Image.open(origin_path)
    # 加载图片像素矩阵，获取像素点颜色
    img_array = img_origin.load()

    img_new = Image.new("RGB", img_origin.size, (0, 0, 0))
    draw = ImageDraw.Draw(img_new)
    font = ImageFont.truetype(font_path, font_size)

    index = 0
    # 以font_size大小为间隔，遍历图片矩阵
    for y in range(0, img_origin.size[1], font_size):
        for x in range(0, img_origin.size[0], font_size):
            index = index % len(text)
            # 在(x, y)像素位置，填充文字text[index]，字体为font，填充位于原图片矩阵img_array[x, y]的颜色，文字方向为默认
            draw.text((x, y), text[index], font=font, fill=img_array[x, y], direction=None)
            index = index + 1

    img_new.convert("RGB").save(new_path)


if __name__ == '__main__':
    # 原始图片路径
    my_origin_image_path = "../Image/msc.jpeg"
    # 新图片路径
    my_new_image_path = "../Image/msc_new.jpeg"
    # 字体路径
    my_font_path = "../Font/wqy-microhei.ttc"
    # 填充文字
    my_text = "马思纯"
    # 填充文字像素大小
    my_font_size = 10

    generate_new_image(my_origin_image_path, my_new_image_path, my_font_path, my_text, my_font_size)
