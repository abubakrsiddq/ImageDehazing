# ImageDehazing
## MIT Final Year project



<table style="width:100%">
  <tr>
    <th>Metrics</th>
     <th>LCA</th>
    <th>DehazeNet(40)</th>
    <th>Dhz_Att</th>
    <th>DCP</th>
    <th>GMAN</th>
    <th>GCA</th>
  </tr>
  <tr>
    <td>PSNR</td>
      <td>17.072</td>
    <td>17.23</td>
    <td>17.00</td>
    <td>12.21</td>
    <td>14.8</td>
    <td><b>20.13</b></td>
   </tr>
    <tr>
    <td>SSIM</td>
     <td>0.65</td>
    <td>0.66</td>
  <td>0.67</td>
    <td>0.61</td>
  <td>0.64</td>
     <td><b>0.77</b><td>
    
   </tr>
   
  <tr>
    <td>FADE</td>
       <td>0.9542</td>
    <td>0.500</td>
  <td>0.87</td>
  <td><b>0.3883</b></td>
    <td>0.645</td>
  <td>0.91</td>
  </tr>
  <tr>
    <td>NQIE</td>
       <td>4.42</td>
    <td>2.93</td>
  <td>3.12</td>
    <td>2.847</td>
  <td><b>2.70</b></td>
  <td><b>2.7</b></td>
  </tr>
  
  <tr>
    <td>CEIQ</td>
       <td>3.27</td>
    <td><b> 3.33</b></td>
  <td>3.25</td>
    <td>3.19</td>
  <td>3.22</td>
  <td>3.22</td>
  
  </tr>
  <tr>
    <td>BLIINDS2</td>
       <td>49.69</td>
    <td>23.5</td>
  <td>35.5</td>
    <td><b>17.39</b></td>
  <td>26.42</td>
  <td>27.5</td>
  </tr>
  </table>

<div class="timeline">
  <div class="container left">
    <div class="content">
       <h1>TIMELINE</h1>
        </div>
  </div>
  <div class="container left">
    <div class="content">
      <h2>WEEK 1</h2>
      <p>Studied literature of dehazing, paper on DCP, dehazenet, BPP, GCA, FFA,etc</p>
    </div>
  </div>
  <div class="container right">
    <div class="content">
      <h2>WEEK 2</h2>
      <p>Implemented a dataset loader and implemented some preprocessing technique.
       Wrote code for DCP and dehaze net from research paper.</p>
    </div>
  </div>
  <div class="container left">
    <div class="content">
      <h2>WEEK 3</h2>
      <p>Started developing basic architecture based on simple networks such as LCA and wrote code for GCA, GMAN, dehazenet.</p>
    </div>
  </div>
 
</div>

<div class="container left">
    <div class="content">
      <h2>WEEK 4</h2>
      <p>Compare different models based on NR IQA methods such as FADE, NQIE, BLIINDS, CEIQ. Wrote code in matlab to generate the output of the models on ohaze  dataset.</p>
    </div>
  </div>
 
</div>

#### Tasks
- [x] DCP 
- [x] Dehazenet model
- [x] GCA code
- [x] Dataset Loader script
- [x] DeHazeNet Training
- [x] [Make Presentation](https://docs.google.com/presentation/d/183MUhIXfW0YKWMM8UqMhUjYGpJbU1W6hkctT-o8tyxo/edit?usp=sharing)
- [x] Metrics compare
- [ ] choose base model

