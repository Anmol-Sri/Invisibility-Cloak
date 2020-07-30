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
Dependencies
> - OpenCV
> - numpy
> - time
---

> Note: Run this before you start
```python
pip install -r preinstall.txt
```

##Procedure : 

### All you need is a red colored cloth and invi.py file.

## How does it work ?
The algorithm is very similar in principle to green screening. But unlike green screening where we remove the background, in this application, we remove the foreground!

We are using a red colored cloth as our cloak. Why red? Why not green? Sure, we could have used green, isn’t red the magician’s color? Jokes aside, colors like green or blue will also work fine with a little bit of tweaking.

The basic idea is given below:
1. Capture and store the background frame.
2. Detect the red colored cloth using color detection algorithm.
3. Segment out the red colored cloth by generating a mask.
4. Generate the final augmented output to create the magical effect.


