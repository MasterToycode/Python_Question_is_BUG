import pytesseract
from PIL import Image
image=Image.open('D:\imppic\Camera Roll\微信截图_20230812100801.png')
image=image.convert('L')
threshold=127
table=[]
for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)
image=image.point(table,'1')
result=pytesseract.image_to_string(image)
print(result)