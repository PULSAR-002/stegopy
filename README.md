# stegopy — Terminal-based Image Steganography Tool

**stegopy** is a simple, terminal-based steganography tool written in Python by **PULSAR**. It lets you hide and reveal secret messages inside `.png` or `.bmp` images using LSB (Least Significant Bit) encoding — all from your command line.

>  "Steganography is the art of hiding **the existence** of a message — not just encrypting it."

---

##  Features

-  Hide secret messages in images (`.png`, `.bmp`)
-  Reveal hidden messages from stego-images
-  Simple CLI interface
-  No data loss — uses lossless image formats
-  100% Python — easy to inspect or modify

---

##  Installation

###  Prerequisites

- Python 3.8 or later must be installed on your system
- `pip` must be available (comes with Python)

You can check with:
python --version
pip --version

The next step is to clone the repo and install the tool:
In the terminal type --> git clone https://github.com/PULSAR-002/stegopy.git
cd stegopy
pip install .

after the installation you can use the tool
Usage:
The tool uses stegano library so make sure to install it via --> pip install stegano
####################################################################################
For encoding use the stegano encode command
1. Use --image flag to specify an image (.png only)
2. Use --message flag to specify the text to hide in that image
3. Use --output flag to name the new image that has the hidden text in it.

sample usage --> stegopy encode --image my.png --message "hello" --output secret.png

###################################################################################
For decoding the image use the following command
stegopy decode --image secret.png


Make sure you give the full path of the image if not in the same directory of the tool, if its in the same directory then the name is enough for it.
Contact me for any further queries, I'll be happy to help, Stay safe!
