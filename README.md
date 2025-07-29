# 🕵️ stegopy — Terminal-based Image Steganography Tool

**stegopy** is a simple yet powerful command-line steganography tool written in Python by **PULSAR**. It allows you to **hide secret messages inside images** and **reveal them later** using LSB (Least Significant Bit) encoding. Perfect for ethical hacking, privacy enthusiasts, and cybersecurity learners.

> “Steganography is the art of hiding **the existence** of a message — not just encrypting it.”

---

## ✨ Features

- 🔐 Hide messages inside `.png` and `.bmp` images
- 🔍 Reveal hidden messages from stego-images
- 🧠 Uses LSB (Least Significant Bit) encoding
- 💯 Lossless — keeps image quality intact
- 🧰 Minimalist terminal interface (CLI)
- 🐍 100% Python — easy to read, modify, and extend

---

## 📦 Installation

### ✅ Requirements

- Python 3.8 or higher
- `pip` (Python package manager)
- `stegano` Python library (used under the hood)

### 💻 Setup Instructions

<pre>
# Clone the repository
git clone https://github.com/PULSAR-002/stegopy.git
cd stegopy
cd stegopy (see if there is a setup.py file in this directory after spoting it enter the following command)
pip install .
</pre>
##Install the requirements in virtual environment (recommended)
<pre>
  pip install -r requirements.txt
</pre>

## Usage:
## ENCODE:
<pre>
  stegopy encode --image input.png --message "This is a secret" --output secret.png
</pre>
## DECODE:
<pre>
  stegopy decode --image secret.png
</pre>
