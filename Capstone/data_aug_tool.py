from imgaug import augmenters as iaa
import imgaug as ia
import numpy as np
import copy


def aug_mix(image,
            augmenters_param={'Flip':1,
                              'Colorspace':((10,50)),
                              'GaussianBlur':(0.0,3.0),
                              'Dropout':((0,0.2),0.5),
                              'Multiply':((0.5,1.5),0.5),
                              'Crop':(-0.2,-0.1)}):
    images=np.zeros((15,image.shape[0],image.shape[1],image.shape[2]))
    augmenters_param_={'Flip':0,
                      'Colorspace':0,
                      'GaussianBlur':0,
                      'Dropout':(0,1),
                      }
    i=0
    flag=[]
    for aug1 in augmenters_param:
        for aug2 in [x for x in augmenters_param if x!=aug1]:
            if (aug2,aug1) in flag:
                continue
            flag.append((aug1,aug2))
            augmenters_param_copy=copy.deepcopy(augmenters_param_)
            augmenters_param_copy[aug1]=augmenters_param[aug1]
            augmenters_param_copy[aug2]=augmenters_param[aug2]
            seq=iaa.Sequential([
                iaa.Fliplr(augmenters_param_copy['Flip']),
                iaa.WithColorspace(to_colorspace='HSV',from_colorspace='RGB',children=iaa.WithChannels(0,iaa.Add(augmenters_param_copy['Colorspace']))),
                iaa.GaussianBlur(sigma=augmenters_param_copy['GaussianBlur']),
                iaa.Dropout(p=augmenters_param_copy['Dropout'][0],per_channel=augmenters_param_copy['Dropout'][1])
            ])
            seq_det = seq.to_deterministic()
            image_aug = seq_det.augment_images([image])[0]
            images[i] = image_aug
            i += 1
    return images


def select_x(x):
    if x>=640:
        x=635
    elif x<0:
        x=5
    return x


def select_y(y):
    if y>=480:
        y=475
    elif y<0:
        y=5
    return y