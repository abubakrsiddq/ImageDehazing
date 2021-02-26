# [Dark channel Prior](https://sci-hub.se/10.1109/CVPR.2009.5206515)
## [NOTEBOOK](https://nbviewer.jupyter.org/github/abubakrsiddq/ImageDehazing/blob/main/models/DCP/darkChannelPrior.ipynb)
### Transmission map
I(x)=J(X).t(x)+A(1-t(x))

### Main Points
* The dark channel of the haze image will have higher intensity in regions with denser haze
* Intensity of dark channel intensity of haze

### Implementation details
* assume transmission in local patch omega(x) is constant
* Not good prior for sky regions but transmission is zero so no need explicit subtraction( as its same as atmospheric light)
* haze required to percieve depth(aerial perspective) w =0.95 intoduced for this purpose
* J(x).t(x) close to 0 when t(x)->0
* A is most haze opaqe iamge estamated as 0.1% of the brightest pixel in dark prior , which has highest intensity in image I
* To compact blocking effects soft matting





