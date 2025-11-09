Simple Image Encryption Tool
Overview
This project is a Python-based image encryption tool that uses pixel-wise XOR manipulation to encrypt and decrypt images.
By applying a numeric key to each pixel's RGB values, the tool obscures the image, and then restores it using the same key.
It serves as a simple demonstration of basic image cryptography for learning and project purposes.

Features


Encrypts images using pixel-wise XOR operation


Decrypts images back to their original form


Works with common formats (PNG, JPEG)


Command-line interface for easy operation


Sample images provided for demonstration



How It Works


Loads the input image using the Pillow library


Applies XOR operation with a key to each pixel’s RGB channels


Saves the result as an encrypted image


Decryption is done by repeating XOR with the same key, restoring the original image



Installation
Make sure Python 3.6+ is installed. Then install dependencies using:
pip install pillow


Usage
Encrypt:
python pixel.py --mode encrypt --input images/image.jpg --output images/encrypted_image.jpg --key 123

Decrypt:
python pixel.py --mode decrypt --input images/encrypted_image.jpg --output images/decrypted_image.jpg --key 123


Folder Structure
pixel.py                      # Main Python script  
requirements.txt              # Dependencies list  
images/  
    image.jpg            # Original sample image  
    encrypted_image.jpg  # Encrypted output  
    decrypted_image.jpg  # Decrypted output  
LICENSE                       # License file  


Example Images
Original: image.jpg
Encrypted: encrypted_image.jpg
Decrypted: decrypted_image.jpg

License
MIT License

References


Pixel manipulation for image encryption


Sample Python cryptography project templates



This README provides all necessary details for users and contributors.
Feel free to personalize the author/contact section or add more references!
