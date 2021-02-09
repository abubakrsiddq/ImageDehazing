# Dark channel Prior

### Transmission map
I(x)=J(X).t(x)+A(1-t(x))

### Main Points
* The dark channel of the haze image will have higher intensity in regions with denser haze
* Intensity of dark channel intensity of haze

### Implementation details
* assume transmission in local patch omega(x) is constant
* Not good prior for sky regions but transmission is zero so no need explicit subtraction( as its same as atmospheric light)
* haze required to percieve depth(aerial perspective) w =0.95 intoduced for this purpose




