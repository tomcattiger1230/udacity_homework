import os
import shutil
train_filenames1 = os.listdir('cattesting')
train_filenames2 = os.listdir('dogtesting')
train_cat = filter(lambda x:x[:3] == 'cat', train_filenames1)
train_dog = filter(lambda x:x[:3] == 'dog', train_filenames2)


for filename in train_cat:
    os.symlink('../../cattesting/'+filename, 'train2/cat/'+filename)

for filename in train_dog:
    os.symlink('../../dogtesting/'+filename, 'train2/dog/'+filename)
