🖼️ Simple Image Encryption Tool
🔍 Overview

This project is a Python-based image encryption and decryption tool that secures images using pixel-wise XOR manipulation.
By applying a numeric key to each pixel’s RGB values, the tool scrambles the image into an unreadable form — and then restores it using the same key.

It’s a simple yet powerful demonstration of basic image cryptography, ideal for learning, mini-projects, or research experiments.

✨ Features

🔒 Encrypts images using pixel-wise XOR operation

🔓 Decrypts images back to their original state

🧩 Works with all popular formats — PNG, JPEG, etc.

💻 Simple command-line interface for easy operation

🧠 Lightweight and great for learning cryptography basics

⚙️ How It Works

🖼️ Loads the input image using the Pillow (PIL) library

🔢 Applies an XOR operation using the user-provided numeric key (0–255) to every pixel’s RGB channels

💾 Saves the resulting encrypted image

♻️ Applying the same key again decrypts the image back to its original form

🧩 Installation

Make sure you have Python 3.6+ installed. Then install dependencies with:

pip install pillow

💻 Usage
🔐 Encrypt an Image
python pixel.py --mode encrypt --input images/image.jpg --output images/encrypted_image.jpg --key 123

🔓 Decrypt the Image
python pixel.py --mode decrypt --input images/encrypted_image.jpg --output images/decrypted_image.jpg --key 123


✅ Use the same key for both encryption and decryption.

📁 Folder Structure
pixel.py                      # Main Python script
requirements.txt              # Dependencies list
images/
    image.jpg                 # Original sample image
    encrypted_image.jpg       # Encrypted output
    decrypted_image.jpg       # Decrypted output
LICENSE                       # License file

🖼️ Example Images
Stage	Description
🧩 Original	image.jpg
🔒 Encrypted	encrypted_image.jpg
🔓 Decrypted	decrypted_image.jpg
📜 License

This project is licensed under the MIT License.

📚 References

🧠 Pixel manipulation concepts for image encryption

🧰 Sample Python cryptography project templates

✨ This README provides all necessary details for users and contributors. Feel free to personalize the author or add more references!
