# Invisibility-Cloak

This [code](main.py) turns a `red` colour cloth into an invisibility cloak.
This project aims to emulate an invisibility cloak like in Harry Potter.

>- It's a fun application which you will enjoy using.
>- You can learn some key functions of opencv from this project. 


## Installation

#### Clone

- Clone this repo to your local machine using `https://github.com/Anmol-Sri/Invisibility-Cloak.git`

#### Setup/Requirements

> The code is written in Python (`Python3`)

#### Dependencies
> - OpenCV
> - numpy
> - time
---

## Procedure : 

### All you need is a red colored cloth and main.py file.

## How does it work ?
The algorithm is very similar in principle to green screening. But unlike green screening where we remove the background, in this application, we remove the foreground!

We are using a red colored cloth as our cloak. Why red? Why not green? Sure, we could have used green, isn’t red the magician’s color? Jokes aside, colors like green or blue will also work fine with a little bit of tweaking.

The basic idea is given below:
1. Capture and store the background frame.
2. Detect the red colored cloth using color detection algorithm.
3. Segment out the red colored cloth by generating a mask.
4. Generate the final augmented output to create the magical effect.

##  Further Explanation / Steps : 
This project aims to emulate an invisibility cloak like in Harry Potter.

1) Clone this project.

2) Run main.py & get away from the screan so that it can record the area. 

3) Now come in front of the screen when the window pop out on your desktop.

4) Grab a red cloth and Let the magic begin !!

5) Congratulations!! You are now a wizard!!

6) Press q to quit on any of the open camera windows.


## Now Lets see the code:

#### Note: Run this before you start

```python
pip install -r preinstall.txt
```

The code has been written to recognize RED color as cloak for now.
```
lower_range = np.array([0,120,50])
higher_range = np.array([10,255,255])
```

You can change the color bound according to yourself.The color range for HSV value are available [here](http://colorizer.org/).Saturation range is [0,255] and Value range is [0,255]. Different softwares use different scales. So if you are comparing OpenCV values with them, you need to normalize these ranges.

- Masking is one of the key features for this project:
```
mask1 = cv2.inRange(hsv,lower_red,upper_red)
```
The above forms a mask of the area we want to make invisible to frame-feed.

- The next task is to extract the above mask from the frame,background and foreground.
```

#segmenting out cloth color
mask2 = cv2.inRange(hsv,lower_red,upper_red)

Addition of the two masks to generate the final mask.
mask = mask1+mask2
# first we will do EROSION then followed by dilation 
# we can do both this step by MORPH_OPEN or by mophologyEx
# purpose being to remove white noise and to mask the red color from cloak  
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))

```
- This is now where the magic happens:
```
- Run code:- main.py
```
