# ImageDehazing
## MIT Final Year project



<table style="width:100%">
  <tr>
    <th>Metrics</th>
    <th>GT</th>
    <th>hazy</th>
    <th>LCA</th>
    <th>DehazeNet(40)</th>
    <th>DCP</th>
    <th>GMAN</th>
  </tr>
  
  <tr>
    <td>FADE</td>
    <td>0.3597</td>
    <td>0.7975</td>
    <td>0.8163</td>
    <td>0.5130</td>
  <td><b>0.3482</b></td>
    <td>0.6574</td>
  </tr>
  <tr>
    <td>NQIE</td>
    <td>2.8509</td>
    <td>2.6513</td>
    <td>5.4881</td>
    <td>2.7238</td>
    <td>2.662</td>
  <td><b>2.5453</b></td>
  </tr>
  
  <tr>
    <td>CEIQ</td>
    <td>3.2714</td>
    <td>3.159</td>
    <td>3.0446</td>
    <td> 3.045</td>
    <td>2.7513</td>
  <td><b>3.1598</b></td>
  </tr>
  <tr>
    <td>BLIINDS2</td>
    <td>12.744</td>
    <td>16.2</td>
    <td>53.0667</td>
    <td><b>16.94</b></td>
    <td>17.6778</td>
  <td>17.3222</td>
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

