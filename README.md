 Image Encryption & Decryption Tool

    A powerful and lightweight tool that performs image encryption and decryption using pixel manipulation, password-based security, and DSA-inspired Fisher-Yates shuffling. Supports both single image (CLI) and multiple image processing (GUI).

📸 Features

    🔐 Encrypt and Decrypt any image using a password

    🔁 Reversible pixel-level encryption (XOR + shuffle)

    🧠 Uses Data Structures & Algorithms (DSA): Fisher-Yates Shuffle

    🖼️ Supports multiple images at once via GUI file picker

    💻 Clean CLI with colorful interface and ASCII art banner

    💡 Password-based key derivation using SHA-256

    🧠 Reversible encryption logic without saving shuffle data

🧠 How It Works (Concepts Used)
1. 🧬 Pixel Manipulation

    The image is loaded using Pillow (PIL) and RGB values of each pixel are extracted.

    RGB pixels are flattened into a 1D array to simplify processing like an integer array.

2. 🔐 XOR Encryption

    Each RGB value is encrypted using the XOR operation with a key derived from your password.

    XOR is fast, reversible, and commonly used in cryptographic systems.

R' = R ^ key
G' = G ^ key
B' = B ^ key

3. 🔑 Password → Key (SHA-256)

    The password is hashed using SHA-256.

    A numeric key is derived by summing the byte values and taking modulo 256.

key = sum(SHA256(password)) % 256

This ensures:

    Secure and consistent encryption

    Same password = same encryption key

4. 🔀 Fisher-Yates Shuffle (DSA-based Algorithm)

    The pixel array is shuffled using the Fisher-Yates algorithm, seeded by the key.

    This adds a layer of obfuscation and randomness.

Used for:

    Efficient O(n) shuffling

    Reversible encryption using deterministic shuffle with seed

5. 🔁 Reversible Decryption

    To decrypt:

        The shuffle is reversed using an inverse index map

        XOR is applied again using the same key

6. 🖼️ Multiple Image Support with GUI

    For batch processing, a Tkinter GUI lets you select multiple files.

    User-friendly password prompt and real-time decryption/encryption.

🚀 How to Run
✅ CLI Mode (Single Image)

python img_enc_dec.py

Follow prompts to:

    Enter file path

    Enter password

    Choose encrypt or decrypt

✅ GUI Mode (Multiple Images)

When prompted, select multiple files using the file picker.

    Enter password

    Automatically encrypts/decrypts in batch


