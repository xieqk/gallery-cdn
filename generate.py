import os

path = 'gaoliang'
prefix = 'https://cdn.jsdelivr.net/gh/xieqk/gallery-cdn/'
final_str = '<photos>'

img_list = os.listdir(path)

for img_name in img_list:
    img_str = '![](https://cdn.jsdelivr.net/gh/xieqk/gallery-cdn/' + path + '/' + img_name + ')'
    final_str += img_str

final_str += '</photos>'

print(final_str)