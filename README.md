 	
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/lca-net-light-convolutional-autoencoder-for/image-dehazing-on-reside)](https://paperswithcode.com/sota/image-dehazing-on-reside?p=lca-net-light-convolutional-autoencoder-for)
# ImageDehazing
 MIT Final Year project

[NoteBook's Link](https://nbviewer.jupyter.org/github/abubakrsiddq/ImageDehazing/tree/main/)

##### Comparision on KITTI
<table>
 <tr>
  <th>Metrics</th>
  <th><a >Hazy</a></th>
   <th><a href="models/LCA-net">LCA</a></th>
    <th><a href="models/DeHazenet">DehazeNet(40)</a></th>
    <th><a href="models/dehazenet_attention">Dhz_Att</a></th>
    <th><a href="models/DCP">DCP</a></th>
    <th><a href="models/GMAN_net">GMAN</a></th>
    <th><a href="models/GCA-net">GCA(30)</a></th>
    <th><a href="models/FFA-net">FFA(10)</a></th>
    <th><a href="models/unet">U-net</a></th>
  <th><a href="models/novel">Novel</a></th>
  
  
  </tr>
   <tr>
    <td>PSNR</td>
      <td>15.66</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
   </tr>
    <tr>
    <td>SSIM</td>
       <td>0.7349</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>   
     <td></td>
 </tr>
   
  <tr>
    <td>FADE</td>
             <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
   <td></td>
  </tr>
  <tr>
    <td>NQIE</td>
             <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
   <td></td>
  </tr>
  
  <tr>
    <td>CEIQ</td>
             <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
   <td></td>
  </tr>
  <tr>
    <td>BLIINDS2</td>
             <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
   <td></td>
  </tr>
 </table>
 
 
 
 
 
 
 
 
 
 
 
 
 
 

##### Comparision of present models on RESIDE

<table style="width:100%">
  <tr>
    <th>Metrics</th>
     <th><a href="models/LCA-net">LCA</a></th>
    <th><a href="models/DeHazenet">DehazeNet(40)</a></th>
    <th><a href="models/dehazenet_attention">Dhz_Att</a></th>
    <th><a href="models/DCP">DCP</a></th>
    <th><a href="models/GMAN_net">GMAN</a></th>
    <th><a href="models/GCA-net">GCA(30)</a></th>
    <th><a href="models/FFA-net">FFA(10)</a></th>
    <th><a href="models/unet">U-net</a></th>
   
  </tr>
  <tr>
    <td>PSNR</td>
      <td>17.072</td>
    <td>17.23</td>
    <td>17.00</td>
    <td>12.21</td>
    <td>14.8</td>
    <td>20.13</td>
    <td><b>20.67</b></td>
    <td>19.38</td>
   </tr>
    <tr>
    <td>SSIM</td>
     <td>0.65</td>
    <td>0.66</td>
  <td>0.67</td>
    <td>0.61</td>
  <td>0.64</td>
     <td>0.77</td>
      <td><b>0.79</b></td>
      <td>0.73</td>
   </tr>
   
  <tr>
    <td>FADE</td>
       <td>0.9542</td>
    <td>0.500</td>
  <td>0.87</td>
  <td><b>0.3883</b></td>
    <td>0.645</td>
  <td>0.91</td>
  <td>1.24</td>
  <td>0.68</td>
  </tr>
  <tr>
    <td>NQIE</td>
       <td>4.42</td>
    <td>2.93</td>
  <td>3.12</td>
    <td>2.847</td>
  <td>2.70</td>
  <td>2.7</td>
  <td><b>2.67</b></td>
  <td>3.71</td>
  </tr>
  
  <tr>
    <td>CEIQ</td>
       <td>3.27</td>
    <td>3.33</td>
  <td>3.25</td>
    <td>3.19</td>
  <td>3.22</td>
  <td>3.22</td>
  <td><b>3.42</b></td>
  <td>3.4</td>
  </tr>
  <tr>
    <td>BLIINDS2</td>
       <td>49.69</td>
    <td>23.5</td>
  <td>35.5</td>
    <td><b>17.39</b></td>
  <td>26.42</td>
  <td>27.5</td>
  <td>24.4</td>
  <td>39.11</td>
  </tr>
  </table>

