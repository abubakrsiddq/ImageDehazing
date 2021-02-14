import os
import cv2
import numpy as np


import os
import cv2
import numpy as np


class SimpleDatasetLoader:
    # Method: Constructor
    def __init__(self, preprocessors=None):
        """
        :param preprocessors: List of image preprocessors
        """
        self.preprocessors = preprocessors

        if self.preprocessors is None:
            self.preprocessors = []

    # Method: Used to load a list of images for pre-processing
    def load(self, gt_image_paths,haze_image_paths, verbose=-1):
        """
        :param gt_image_paths: List of  ground image paths
        :param haze_image_paths: List of hazy image paths
    
        :param verbose: Parameter for printing information to console
        :return: Tuple of ground truth and hazy tensors
        """
        gt_data, haze_data = [], []

        for i, image_path in enumerate(gt_image_paths):
            image = cv2.imread(image_path)
            #image = np.moveaxis(image, -1, 0)
            #label = image_path.split(os.path.sep)[-2]

            if self.preprocessors is not None:
                for p in self.preprocessors:
                    image = p.preprocess(image)

            gt_data.append(image)
            #labels.append(label)

            if verbose > 0 and i > 0 and (i+1) % verbose == 0:
                print('[INFO]: Processed {}/{} GT'.format(i+1, len(gt_image_paths)))
        print("-----------------------------------------------------")        
        for i, image_path in enumerate(haze_image_paths):
            image=cv2.imread(image_path)
            if self.preprocessors is not None:
                for p in self.preprocessors:
                    image = p.preprocess(image)
            haze_data.append(image)
            if verbose > 0 and i > 0 and (i+1) % verbose == 0:
                print('[INFO]: Processed {}/{} HAZE'.format(i+1, len(haze_image_paths)))

        return (np.array(gt_data), np.array(haze_data))