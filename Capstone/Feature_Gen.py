import h5py
from keras.models import Model
from keras.layers import Input, Lambda, GlobalAveragePooling2D
from keras.applications import xception, resnet50, inception_resnet_v2
from keras.preprocessing.image import ImageDataGenerator

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

SHAPE = {
    "xception": (299, 299), # TensorFlow ONLY
	    "resnet": (224, 224),
    "inception": (299, 299)
}

def write_gap(MODEL, image_size, func_name, lambda_func=None, B_size=16):
    width = image_size[0]
    height = image_size[1]
    input_tensor = Input((height, width, 3))
    x = input_tensor
    if lambda_func:
        x = Lambda(lambda_func)(x)

    base_model = MODEL(input_tensor=x, weights='imagenet', include_top=False)
    model = Model(base_model.input, GlobalAveragePooling2D()(base_model.output))

    gen = ImageDataGenerator()
    train_generator = gen.flow_from_directory("train2", image_size, shuffle=False, batch_size=B_size)
    test_generator = gen.flow_from_directory("test2", image_size, shuffle=False,
                                             batch_size=B_size, class_mode=None)

    train = model.predict_generator(train_generator) #, int(train_generator.samples/B_size))
    test = model.predict_generator(test_generator) #, int(test_generator.samples/B_size))
    with h5py.File("gap_%s.h5"%func_name) as h:
        h.create_dataset("train", data=train)
        h.create_dataset("test", data=test)
        h.create_dataset("label", data=train_generator.classes)


if __name__ == '__main__':
    # load three different model and save the feature vectors in the '.h5' file
    for i in MODELS.keys():
        write_gap(MODELS[i], SHAPE[i], i, PREPROCESS[i], B_size=64)
