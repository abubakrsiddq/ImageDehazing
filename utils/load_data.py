from utils import imagetoarraypreprocessor,path_list_gen,simple_preprocessor,simple_dataset_loader
import cv2
import numpy as np

class Load_Data:
    def __init__(self,image_width,image_height,GT_DIR_PATH,HAZY_DIR_PATH,verbose=-1):
        """
        :param image_width,image_height: image dimensions required
        :param GT_DIR_PATH: path of ground truth diretory
        :param HAZY_DIR_PATH: path of hazy image directory
        """
        self.width=image_width
        self.height=image_height
        self.GT_PATH=GT_DIR_PATH
        self.HAZY_PATH=HAZY_DIR_PATH
        self.verbose=verbose

    def load_tensor(self):
        '''
        :returns tuple(haze_tensor,gt_tensor)
        '''

        sp=simple_preprocessor.SimplePreprocessor(self.width,self.height)
        iap=imagetoarraypreprocessor.ImageToArrayPreprocessor()
        sdl=simple_dataset_loader.SimpleDatasetLoader([sp,iap])
        pth=path_list_gen.List_gen(self.GT_PATH,self.HAZY_PATH)
        gt_pth,hazy_pth=pth.gen_path()
        #hazy_tensor,gt_tensor=sdl.load(gt)#,hazy)
        #hazy_tensor=hazy_tensor.astype("float")/255.0
        gt_tensor,haze_tensor=sdl.load(gt_pth,hazy_pth,verbose=5)
        gt_tensor=gt_tensor.astype("float")/255.0
        gt_tensor = np.moveaxis(gt_tensor, -1, 1)# change channel ordering


        haze_tensor=haze_tensor.astype("float")/255.0
        haze_tensor = np.moveaxis(haze_tensor, -1, 1)# change channel ordering

        return (haze_tensor,gt_tensor)