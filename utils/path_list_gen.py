import glob
from natsort import natsorted
class List_gen:
    def __init__(self,orig_path,haze_path):
        self.gt_path=orig_path
        self.hazy_path=haze_path

    def gen_path(self):
        train_img_lst=[]
        orig_img_lst=[]
        orig_img= glob.glob(self.gt_path+'/*.jpg')        
        hazy_img= glob.glob(self.hazy_path+'/*.jpg')
        n = len(orig_img)
        for x in range(n):
            train_img_lst.append(hazy_img[x])
            orig_img_lst.append(orig_img[x])
        return natsorted(train_img_lst),natsorted(orig_img_lst)
