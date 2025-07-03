# from PIL import Image
# import hashlib
# import random
# import os
# from pyfiglet import Figlet
# from termcolor import colored
# from colorama import init
# import time
# # Initialize colorama for Windows compatibility
# init()

# # ===================== DSA Banner =====================

# def print_banner():
#     f = Figlet(font='slant')  # Try "slant", "block", "standard"
#     banner = f.renderText('Image Encryptor')
#     print(colored(banner, 'cyan'))
#     print(colored("Task-02 | Prodigy Infotech 🔐\n", "green"))

# # ===================== Key Generation =====================

# def derive_key(password):
#     """Convert password to numeric key using SHA-256"""
#     hashed = hashlib.sha256(password.encode()).digest()
#     return sum(hashed) % 256

# # ===================== Pixel Utils =====================

# def flatten_pixels(img):
#     """Convert 2D pixels to 1D list"""
#     w, h = img.size
#     flat = []
#     for y in range(h):
#         for x in range(w):
#             flat.append(img.getpixel((x, y)))
#     return flat

# def reshape_pixels(flat_pixels, size):
#     """Convert 1D pixels back to 2D image"""
#     w, h = size
#     new_img = Image.new("RGB", (w, h))
#     index = 0
#     for y in range(h):
#         for x in range(w):
#             new_img.putpixel((x, y), flat_pixels[index])
#             index += 1
#     return new_img

# # ===================== DSA-Based Shuffling =====================

# def fisher_yates_shuffle(pixels, seed):
#     """Shuffle pixels using Fisher–Yates with fixed seed"""
#     random.seed(seed)
#     n = len(pixels)
#     for i in range(n - 1, 0, -1):
#         j = random.randint(0, i)
#         pixels[i], pixels[j] = pixels[j], pixels[i]
#     return pixels

# # ===================== Encryption Core =====================

# def xor_pixels(pixels, key):
#     """Encrypt/decrypt using XOR operation"""
#     return [((r ^ key), (g ^ key), (b ^ key)) for r, g, b in pixels]

# def encrypt_image(input_path, output_path, password):
#     img = Image.open(input_path).convert("RGB")
#     key = derive_key(password)

#     flat_pixels = flatten_pixels(img)
#     shuffled = fisher_yates_shuffle(flat_pixels.copy(), seed=key)
#     xored = xor_pixels(shuffled, key)

#     encrypted_img = reshape_pixels(xored, img.size)
#     encrypted_img.save(output_path)

#     print(colored(f"[+] Encrypted image saved as: {output_path}", "green"))

# def decrypt_image(input_path, output_path, password):
#     img = Image.open(input_path).convert("RGB")
#     key = derive_key(password)

#     flat_pixels = flatten_pixels(img)
#     xored = xor_pixels(flat_pixels, key)

#     # Rebuild original pixel order
#     index_order = list(range(len(xored)))
#     shuffled_indices = fisher_yates_shuffle(index_order.copy(), seed=key)
#     inverse_indices = [0] * len(shuffled_indices)
#     for i, si in enumerate(shuffled_indices):
#         inverse_indices[si] = i
#     unshuffled = [xored[inverse_indices[i]] for i in range(len(xored))]

#     decrypted_img = reshape_pixels(unshuffled, img.size)
#     decrypted_img.save(output_path)

#     print(colored(f"[+] Decrypted image saved as: {output_path}", "green"))

# # ===================== Main CLI =====================

# def main():
#     print_banner()

#     print(colored("=== DSA-Based Image Encryptor Menu ===", "yellow"))
#     print(colored("1. Encrypt Image", "magenta"))
#     print(colored("2. Decrypt Image", "magenta"))
#     choice = input(colored("Choose (1 or 2): ", "blue")).strip()

#     path = input(colored("Enter image path: ", "cyan")).strip()
#     if not os.path.exists(path):
#         print(colored("[-] File does not exist!", "red"))
#         return

#     password = input(colored("Enter password: ", "cyan")).strip()
#     output = input(colored("Enter output image filename (e.g., out.png): ", "cyan")).strip()

#     if choice == '1':
#         encrypt_image(path, output, password)
#     elif choice == '2':
#         decrypt_image(path, output, password)
#     else:
#         print(colored("[-] Invalid choice!", "red"))

# import time

# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print(colored("\n[!] Encrypter Terminated by User. Goodbye! 👋", "red"))
#         time.sleep(1)


from PIL import Image
import hashlib
import random
import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from pyfiglet import Figlet
from termcolor import colored
from colorama import init
import time

# Init colorama
init()

# ===== Banner =====
def print_banner():
    f = Figlet(font='slant')
    banner = f.renderText('Image Encryptor')
    print(colored(banner, 'cyan'))
    print(colored("By: Your_Name_Here | CLI+GUI Powered 🔐\n", "green"))

# ===== Key Derivation =====
def derive_key(password):
    hashed = hashlib.sha256(password.encode()).digest()
    return sum(hashed) % 256

# ===== Pixel Utils =====
def flatten_pixels(img):
    w, h = img.size
    return [img.getpixel((x, y)) for y in range(h) for x in range(w)]

def reshape_pixels(flat_pixels, size):
    w, h = size
    new_img = Image.new("RGB", (w, h))
    i = 0
    for y in range(h):
        for x in range(w):
            new_img.putpixel((x, y), flat_pixels[i])
            i += 1
    return new_img

# ===== DSA Shuffle =====
def fisher_yates_shuffle(pixels, seed):
    random.seed(seed)
    for i in range(len(pixels) - 1, 0, -1):
        j = random.randint(0, i)
        pixels[i], pixels[j] = pixels[j], pixels[i]
    return pixels

# ===== XOR Encrypt/Decrypt =====
def xor_pixels(pixels, key):
    return [((r ^ key), (g ^ key), (b ^ key)) for r, g, b in pixels]

# ===== Single Image Mode (CLI) =====
def encrypt_image(path, output_path, password):
    img = Image.open(path).convert("RGB")
    key = derive_key(password)
    flat = flatten_pixels(img)
    shuffled = fisher_yates_shuffle(flat.copy(), key)
    xored = xor_pixels(shuffled, key)
    enc_img = reshape_pixels(xored, img.size)
    enc_img.save(output_path)
    print(colored(f"[+] Encrypted: {output_path}", "green"))

def decrypt_image(path, output_path, password):
    img = Image.open(path).convert("RGB")
    key = derive_key(password)
    flat = flatten_pixels(img)
    xored = xor_pixels(flat, key)

    idx = list(range(len(xored)))
    shuffled = fisher_yates_shuffle(idx.copy(), key)
    inverse = [0] * len(shuffled)
    for i, s in enumerate(shuffled):
        inverse[s] = i
    unshuffled = [xored[inverse[i]] for i in range(len(xored))]
    dec_img = reshape_pixels(unshuffled, img.size)
    dec_img.save(output_path)
    print(colored(f"[+] Decrypted: {output_path}", "green"))

# ===== GUI Multiple File Support =====
def gui_batch_process(encrypt=True):
    root = tk.Tk()
    root.withdraw()  # Hide main window

    # Select multiple images
    files = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if not files:
        messagebox.showinfo("Cancelled", "No files selected.")
        return

    # Ask for password
    password = simpledialog.askstring("Password", "Enter password:", show="*")
    if not password:
        messagebox.showwarning("Missing", "No password provided.")
        return

    for path in files:
        base = os.path.basename(path)
        name, ext = os.path.splitext(base)
        out_file = f"{name}_{'enc' if encrypt else 'dec'}{ext}"

        try:
            if encrypt:
                encrypt_image(path, out_file, password)
            else:
                decrypt_image(path, out_file, password)
        except Exception as e:
            print(colored(f"[!] Error with {base}: {e}", "red"))

    messagebox.showinfo("Done", f"{'Encryption' if encrypt else 'Decryption'} complete for {len(files)} file(s).")

# ===== Main Entry =====
def main():
    print_banner()
    print(colored("1. Encrypt Single Image (CLI)", "magenta"))
    print(colored("2. Decrypt Single Image (CLI)", "magenta"))
    print(colored("3. Encrypt Multiple Images (GUI)", "cyan"))
    print(colored("4. Decrypt Multiple Images (GUI)", "cyan"))
    choice = input(colored("Choose an option (1-4): ", "yellow")).strip()

    if choice == "1":
        path = input(colored("Enter image path: ", "cyan")).strip()
        if not os.path.exists(path):
            print(colored("[-] File not found!", "red"))
            return
        password = input(colored("Enter password: ", "cyan")).strip()
        out = input(colored("Output filename: ", "cyan")).strip()
        encrypt_image(path, out, password)

    elif choice == "2":
        path = input(colored("Enter encrypted image path: ", "cyan")).strip()
        if not os.path.exists(path):
            print(colored("[-] File not found!", "red"))
            return
        password = input(colored("Enter password: ", "cyan")).strip()
        out = input(colored("Output filename: ", "cyan")).strip()
        decrypt_image(path, out, password)

    elif choice == "3":
        gui_batch_process(encrypt=True)

    elif choice == "4":
        gui_batch_process(encrypt=False)

    else:
        print(colored("[-] Invalid choice!", "red"))

# ===== Handle Ctrl+C Gracefully =====
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colored("\n[!] Encrypter Terminated by User. Goodbye! 👋", "red"))
        time.sleep(1)
