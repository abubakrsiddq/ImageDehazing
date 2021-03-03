%==========================================================================
% J. Yan, J. Li, X. Fu, "No-Reference Quality Assessment of Contrast-Distorted Images using Contrast Enhancement"
% 
% Please try your own contrast distorted images with different levels.
% Larger predicted score means better contrast quality.
%==========================================================================

clear;
clc;

%addpath('utils', 'data', 'images');

im0 = imread('01_outdoor_hazy.jpg');
%im1 = imread('2.png');
%im2 = imread('3.png');

pred = CEIQ(im0);
%pred(2) = CEIQ(im1);
%pred(3) = CEIQ(im2);

%pred