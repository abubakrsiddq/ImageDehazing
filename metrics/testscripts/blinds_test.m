image = double(imread('D:\MATLAB Drive\testHaze\Hazy\01_outdoor_hazy.jpg'));

features = bliinds2_feature_extraction(image)
score = bliinds_prediction(features)