  

# Change-Background

  

Change background of image using semantic segmentation implemented in Pytorch trained on HRNet ([Link](https://arxiv.org/pdf/1904.04514.pdf))
 
## Steps to run 
 1. Clone this repository
 ```
 git clone https://github.com/Garvit-32/BG-changer.git
``` 
 2. Install all the dependencies
```
pip install -r requirements.txt 
```
3. Download weights from [here](https://drive.google.com/file/d/1zo-eXWyG8-UEz9h_jaOUY-bt2A1ywsPr/view?usp=sharing) 
4.  Run inference 
```
python main.py --image <path to foreground image> --bg_image <path to background image> --weights <path to weights>
```

Example
```
python main.py --image demo_images/image1.jpg --bg_image demo_images/background1.jpg --weights hrnetv2_hrnet18_person_dataset_120.pth
```
## DEMO
  
### Input
Background image 

<img  src="demo_images/background1.jpg"  width="320.0"  height=  "213.3"> 

Foreground image

<img  src=  "demo_images/image1.jpg"  width=  "325"  height=  "487.5">

  
  

## Output

<img  src="final.png"    height=  "487.5">
