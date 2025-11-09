# 🔒 Simple Image Encryption Tool 🖼️

## Overview

This project is a **Python-based image encryption tool** that uses **pixel-wise XOR manipulation** to encrypt and decrypt images. By applying a numeric key to each pixel's RGB values, the tool obscures the image, and then restores it using the same key. It serves as a simple demonstration of basic image cryptography for learning and project purposes. 💡

---

## Features ✨

* **Encrypts images** using pixel-wise XOR operation.
* **Decrypts images** back to their original form (it's reversible!).
* Works with common formats (**PNG, JPEG**).
* **Command-line interface (CLI)** for easy operation.
* Sample images provided for demonstration.

---

## How It Works ⚙️

1.  Loads the input image using the **Pillow** library.
2.  Applies the **XOR operation** ($\oplus$) with a key to each pixel's **RGB channels**.
    * *Encryption/Decryption Formula (Concept):* $Pixel_{new} = Pixel_{original} \oplus Key$
3.  Saves the result as an encrypted image.
4.  Decryption is done by repeating XOR with the **same key**, restoring the original image because $(A \oplus K) \oplus K = A$.

---

## Installation 💻

Make sure **Python 3.6+** is installed. Then install the necessary dependencies:

pip install pillow

---

## Usage 🚀

The main script is pixel.py.

Encrypt:
Use the --mode encrypt flag.


python pixel.py --mode encrypt --input images/image.png --output images/encrypted_image.png --key 123
Decrypt:
Use the --mode decrypt flag with the exact same key.


python pixel.py --mode decrypt --input images/encrypted_image.png --output images/decrypted_image.png --key 123

---

## Folder Structure 📂

pixel.py                      # Main Python script 🐍
requirements.txt              # Dependencies list 📋
images/
    image.png                 # Original sample image 🌟
    encrypted_image.png       # Encrypted output 🚫
    decrypted_image.png       # Decrypted output ✅
LICENSE                       # License file 📜

---

## Example Images

Original: encrypted_image: decrypted_image:

---

## License 📄
MIT License

---

## References 📚
Pixel manipulation for image encryption
Sample Python cryptography project templates
