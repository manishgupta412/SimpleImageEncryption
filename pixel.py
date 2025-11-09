from PIL import Image
import argparse
import os
import sys

def encrypt_decrypt_image(input_path, output_path, key, mode):
    print(f"[*] Starting {mode}ion process...")
    print(f"    Input : {input_path}")
    print(f"    Output: {output_path}")
    print(f"    Key   : {key}")

    if not os.path.isfile(input_path):
        print(f"[!] Error: Input file not found at {input_path}")
        return 1

    try:
        # Open and convert image to RGB
        img = Image.open(input_path).convert("RGB")
        pixels = img.load()
        width, height = img.size
        total_pixels = width * height

        print(f"[*] Image size: {width}x{height} ({total_pixels} pixels)")
        print("[*] Processing...")

        count = 0
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)
                count += 1
                # Print progress every 10%
                if count % (total_pixels // 10 or 1) == 0:
                    pct = (count / total_pixels) * 100
                    print(f"    Progress: {pct:.1f}%")

        img.save(output_path)
        print(f"[+] Successfully {mode}ed image!")
        print(f"    Saved to: {output_path}")
        return 0

    except Exception as e:
        print(f"[!] Exception occurred: {e}")
        return 2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Image XOR Encryption Tool")
    parser.add_argument("--mode", required=True, choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("--input", required=True, help="Path to input image")
    parser.add_argument("--output", required=True, help="Path to save output image")
    parser.add_argument("--key", type=int, required=True, help="Numeric key (0–255)")

    args = parser.parse_args()

    if not (0 <= args.key <= 255):
        print("[!] Error: Key must be between 0 and 255.")
        sys.exit(1)

    sys.exit(encrypt_decrypt_image(args.input, args.output, args.key, args.mode))
