import tensorflow as tf
import random
import glob
import matplotlib.pyplot as plt

class Loader_utils:
    def __init__(self):
        pass


    def load_image(self,img_path):
        img = tf.io.read_file(img_path)
        img = tf.io.decode_jpeg(img, channels = 3)      # Decode a JPEG-encoded image to a uint8 tensor.
        img = tf.image.resize(img, size = (412, 548), antialias = True)
        img = img / 255.0
        return img

    def data_path(self,orig_img_path, hazy_img_path):
        
        train_img = []
        val_img = []
        
        orig_img = glob.glob(orig_img_path + '/*.png')
        n = len(orig_img)
        random.shuffle(orig_img)
        train_keys = orig_img[:int(0.9*n)]        #90% data for train, 10% for test
        val_keys = orig_img[int(0.9*n):]
        
        split_dict = {}
        for key in train_keys:
            split_dict[key] = 'train'
        for key in val_keys:
            split_dict[key] = 'val'
            
        hazy_img = glob.glob(hazy_img_path + '/*.jpg')
        for img in hazy_img:
            img_name = img.split('/')[-1]
            orig_path = orig_img_path + '/' + img_name.split('_')[0] + '.png'
            if (split_dict[orig_path] == 'train'):
                train_img.append([img, orig_path])
            else:
                val_img.append([img, orig_path])
                
        return train_img, val_img

    def dataloader(self,train_data, val_data, batch_size):
        
        train_data_orig = tf.data.Dataset.from_tensor_slices([img[1] for img in train_data]).map(lambda x: load_image(x))
        train_data_haze = tf.data.Dataset.from_tensor_slices([img[0] for img in train_data]).map(lambda x: load_image(x))
        train = tf.data.Dataset.zip((train_data_haze, train_data_orig)).shuffle(buffer_size=100).batch(batch_size)
        
        val_data_orig = tf.data.Dataset.from_tensor_slices([img[1] for img in val_data]).map(lambda x: load_image(x))
        val_data_haze = tf.data.Dataset.from_tensor_slices([img[0] for img in val_data]).map(lambda x: load_image(x))
        val = tf.data.Dataset.zip((val_data_haze, val_data_orig)).shuffle(buffer_size=100).batch(batch_size)
        
        return train, val

    def display_img(self,model, hazy_img, orig_img):
        
        dehazed_img = model(hazy_img, training = True)
        plt.figure(figsize = (15,15))
        
        display_list = [hazy_img[0], orig_img[0], dehazed_img[0]]
        title = ['Hazy Image', 'Ground Truth', 'Dehazed Image']
        
        for i in range(3):
            plt.subplot(1, 3, i+1)
            plt.title(title[i])
            plt.imshow(display_list[i])
            plt.axis('off')
            
        plt.show()