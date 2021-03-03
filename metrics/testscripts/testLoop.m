function testLoop(pth)
    %addpath('D:\blind_image_quality_toolbox-master\blind_image_quality_toolbox-master\+bliinds2');
    flder=strcat(pth,'*.jpg');
    
    imagefiles = dir(flder);  
    nfiles = length(imagefiles);    % Number of files found
    %disp(nfiles);
    d=0;k=0;r=0;s=0;y=0;
    for ii=1:nfiles
       currentfilename = imagefiles(ii).name;
       pp=strcat(pth,currentfilename);
       %disp(pp);
       currentimage = imread(pp);
       d=d+FADE(currentimage);
       k=k+niqe(currentimage);
       r=r+CEIQ(currentimage);
       features = bliinds2_feature_extraction(currentimage);
       s=s+bliinds_prediction(features);
       %y=y+divine(currentimage)
       disp(ii);
    end
    fprintf('FADE = %.4f',d/nfiles)
    fprintf('NIQE = %.4f',k/nfiles)
    fprintf('CEIQ = %.4f',r/nfiles)
    fprintf('BLIINDS 2 = %.4f',s/nfiles)
    %fprintf('DIVINE = %.4f',y/nfiles)
end