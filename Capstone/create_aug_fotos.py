import numpy as np
import os
from PIL import Image
import matplotlib.pyplot as plt
from data_aug_tool import *

img_path='./train2/dog/'
img_list = os.listdir(img_path)
img_num = len(img_list)
start_num = 12500
for i in range(img_num):
    img_i_path = os.path.join(img_path, img_list[i])
    image = Image.open(img_i_path)
    image = np.asanyarray(image, dtype = 'uint8')
    image_aug=aug_mix(image)
    for j in range(6):
        plt.imsave(os.path.join('./dogtesting/','dog.'+'{}'.format(str(i*6+j+start_num))+'.jpg'),
                   image_aug[j].astype('uint8'))


img_path='./train2/cat/'
img_list = os.listdir(img_path)
img_num = len(img_list)
start_num = 12500
for i in range(img_num):
    img_i_path = os.path.join(img_path, img_list[i])
    image = Image.open(img_i_path)
    image = np.asanyarray(image, dtype = 'uint8')
    image_aug=aug_mix(image)
    for j in range(6):
        plt.imsave(os.path.join('./cattesting/','cat.'+'{}'.format(str(i*6+j+start_num))+'.jpg'),
                   image_aug[j].astype('uint8'))