from keras.applications import * #.xception import Xception
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img


import numpy as np
import argparse

# the summary of dogs and cats in Imagenet
dogs = [
 'n02085620','n02085782','n02085936','n02086079'
,'n02086240','n02086646','n02086910','n02087046'
,'n02087394','n02088094','n02088238','n02088364'
,'n02088466','n02088632','n02089078','n02089867'
,'n02089973','n02090379','n02090622','n02090721'
,'n02091032','n02091134','n02091244','n02091467'
,'n02091635','n02091831','n02092002','n02092339'
,'n02093256','n02093428','n02093647','n02093754'
,'n02093859','n02093991','n02094114','n02094258'
,'n02094433','n02095314','n02095570','n02095889'
,'n02096051','n02096177','n02096294','n02096437'
,'n02096585','n02097047','n02097130','n02097209'
,'n02097298','n02097474','n02097658','n02098105'
,'n02098286','n02098413','n02099267','n02099429'
,'n02099601','n02099712','n02099849','n02100236'
,'n02100583','n02100735','n02100877','n02101006'
,'n02101388','n02101556','n02102040','n02102177'
,'n02102318','n02102480','n02102973','n02104029'
,'n02104365','n02105056','n02105162','n02105251'
,'n02105412','n02105505','n02105641','n02105855'
,'n02106030','n02106166','n02106382','n02106550'
,'n02106662','n02107142','n02107312','n02107574'
,'n02107683','n02107908','n02108000','n02108089'
,'n02108422','n02108551','n02108915','n02109047'
,'n02109525','n02109961','n02110063','n02110185'
,'n02110341','n02110627','n02110806','n02110958'
,'n02111129','n02111277','n02111500','n02111889'
,'n02112018','n02112137','n02112350','n02112706'
,'n02113023','n02113186','n02113624','n02113712'
,'n02113799','n02113978']

cats=[
'n02123045','n02123159','n02123394','n02123597'
,'n02124075','n02125311','n02127052']


# settign for command line arguments 
ap = argparse.ArgumentParser()
ap.add_argument("-k", "--kind", type=str, default="dog", help="clean dog/cat data")
ap.add_argument("-i", "--image", type=str, default="../train2/", #required=True,
	help="path to the input image")
#ap.add_argument("-model", "--model", type=str, default="resnet",
#	help="name of pre-trained network to use")
args = vars(ap.parse_args())

# define a dictionary that maps model names to their classes
# inside Keras, here I've choosen the following three trained models according to the performance on Imagenet
MODELS = {
        "xception": xception.Xception, # TensorFlow ONLY
	    "resnet": resnet50.ResNet50,
        "inception": inception_resnet_v2.InceptionResNetV2
}

PREPROCESS = {
    "xception": xception.preprocess_input, # TensorFlow ONLY
	    "resnet": resnet50.preprocess_input,
    "inception": inception_resnet_v2.preprocess_input
}

DECODE = {
    "xception": xception.decode_predictions, # TensorFlow ONLY
	    "resnet": resnet50.decode_predictions,
    "inception": inception_resnet_v2.decode_predictions
}


# test each image in the models
sum_result = {}
for i in MODELS.keys():
    print("[INFO] loading {}...".format(i))
    Network = MODELS[i]
    model = Network(weights="imagenet") # load each trained model from Keras
    if i == "resnet":
        inputShape = (224, 224)
    else:
        inputShape = (299, 299)

    print("[INFO] loading and pre-processing {} image...".format(args["kind"]))

    # each catagory has 12500 images
    for j in range(12500):
        image_name = args["image"]+args["kind"]+"/"+args["kind"]+"."+str(j)+".jpg"
        image = load_img(image_name, target_size=inputShape)
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        x = PREPROCESS[i](image)
        preds = model.predict(x)
        # print('Predicted:', DECODE[i](preds, top=3)[0])
        decode_res = DECODE[i](preds, top=10)[0]
        # get all index numbers
        preds_result = list(map(lambda x: decode_res[x][0], range(10)))
        # one hit in the list?
        if args["kind"] == 'dog':
            is_DC = True in list(map(lambda x: x in dogs, preds_result))
        else:
            is_DC = True in list(map(lambda x: x in cats, preds_result))
        if str(j) in sum_result.keys():
            sum_result[str(j)].append(is_DC)
        else:
            sum_result[str(j)]=[is_DC]

remove_list = []
for i in sum_result.keys():
    if True not in sum_result[i]:
        remove_list.append(i)
np.save('remove_list_'+args['kind']+'.npy', remove_list)
f_o = open('./remove_list_'+args['kind']+'.txt', 'w')
if len(remove_list)>0:
    for ele in remove_li=st:
        f_o.write(ele+'\n')
    f_o.close()
else:
    f_o.write('nothing to save')
    f_o.close()

