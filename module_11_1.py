import requests
import numpy
from PIL import Image


response = requests.get('https://www.pypi.org')
print(response.text)

arr = numpy.linspace(1, 10, 100)
print(arr)

a = numpy.array([1, 2, 3, 4, 5])
print(a)
print(a ** 2)

img = Image.open("apples.jpg")

img = Image.open('apples.jpg')
img.save('test_apples.png', 'png')

with Image.open('apples.jpg.') as image:
    width, height = image.size
print((width, height))

img = Image.open('apples.jpg')
width, height = img.size
img = img.resize((width // 3, height // 3))
img.save('resized_apples.jpg')

img = Image.open('apples.jpg')
grayscale_img = img.convert('L')
grayscale_img.save('apples_grayscale.jpg')