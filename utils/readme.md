# Utility scripts

### Code required to load dataset as tensors
```
from utils import load_data
loader=load_data.Load_Data(512,512,'../ohaze/GT','../ohaze/hazy',verbose=5)
loader.load_tensor()
