 	
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
    <th><a href="models/DeHazenet">DehazeNet</a></th>
       <th><a href="models/DCP">DCP</a></th>
    <th><a href="models/GMAN_net">GMAN</a></th>
    <th><a href="models/GCA-net">GCA</a></th>
    <th><a href="models/FFA-net">FFA</a></th>
    <th><a href="models/unet">U-net</a></th>
  <th><a href="models/novel">Novel</a></th>
  
  
  </tr>
   <tr>
    <td>PSNR &#8593</td>
      <td class="hazy">15.66</td>
    <td class="lca">18.32</td>
    <td class="dehazenet"></td>
       <td class="dcp">16.65</td>
    <td class="gman">24.64</td>
    <td class="gca">22.94</td>
    <td class="FFA"></td>
    <td class="unet">24.56</td>
    <td class="novel">31.35</td>
   </tr>
    <tr>
    <td>SSIM &#8593</td>
         <td class="hazy">0.73</td>
    <td class="lca">0.69</td>
    <td class="dehazenet"></td>
        <td class="dcp">0.62</td>
    <td class="gman">0.89</td>
    <td class="gca">0.90</td>
    <td class="FFA"></td>
    <td class="unet">0.86</td>
    <td class="novel">0.95</td>
 </tr>
   
  <tr>
   <td>FADE &#8595</td>
     <td class="hazy">1.12</td>
    <td class="lca">0.63</td>
    <td class="dehazenet"></td>
        <td class="dcp">0.36</td>
    <td class="gman">0.43</td>
    <td class="gca"></td>
    <td class="FFA"></td>
    <td class="unet">0.57</td>
    <td class="novel">0.45</td>
  <tr>
    <td>NQIE &#8595</td>
     <td class="hazy">2.75</td>
    <td class="lca">4.36</td>
    <td class="dehazenet"></td>
        <td class="dcp">2.53</td>
    <td class="gman">3.09</td>
    <td class="gca"></td>
    <td class="FFA"></td>
    <td class="unet">2.73</td>
    <td class="novel">2.79</td>
   
  </tr>
  
  <tr>
    <td>CEIQ &#8593</td>
     <td class="hazy">3.14</td>
    <td class="lca">3.02</td>
    <td class="dehazenet"></td>
       <td class="dcp">2.77</td>
    <td class="gman">3.23</td>
    <td class="gca"></td>
    <td class="FFA"></td>
    <td class="unet">3.19</td>
    <td class="novel">3.27</td>
  </tr>
  <tr>
    <td>BLIINDS2 &#8595</td>
        <td class="hazy">6.23</td>
    <td class="lca">40.80</td>
    <td class="dehazenet"></td>
      <td class="dcp">21.87</td>
    <td class="gman">16.13</td>
    <td class="gca"></td>
    <td class="FFA"></td>
    <td class="unet">8.88</td>
    <td class="novel">11.86</td>
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

