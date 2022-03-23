# A simple script to calculate BMI
import pywebio
from pywebio.input import input, FLOAT, file_upload
from pywebio.output import put_text, put_image
from pathlib import Path

def bmi():
    height = input("Input your height(cm)：", type=FLOAT)
    weight = input("Input your weight(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
            break

def input_image():
    # Upload a file and save to server
    f = pywebio.input.file_upload("Upload a file")

    open(f['filename'], 'wb').write(f['content'])
    # open('asset/' + f['filename'], 'wb').write(f['content'])

    imgs = pywebio.file_upload("Select some pictures:", accept="image/*", multiple=True)
    for img in imgs:
        put_image(img['content'])

if __name__ == '__main__':
    input_image()
    # bmi()
