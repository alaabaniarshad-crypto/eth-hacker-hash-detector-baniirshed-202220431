# Ethical Hacker Hash Detector 🛡️

> A robust CLI tool for identifying hash algorithms and generating MD5 digests for educational and ethical security testing.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## 📌 Overview
This tool is designed to assist cybersecurity students and ethical hackers in quickly identifying common hash types based on their hexadecimal length. It also provides a utility to generate MD5 hashes from plaintext. The tool operates entirely using Python's standard library, ensuring compatibility and ease of use on Kali Linux.

## ✨ Features
* **Hash Detection:** Automatically identifies the following hash types based on hex string length:
    * MD5 (32 chars)
    * SHA1 (40 chars)
    * SHA256 (64 chars)
    * SHA384 (96 chars)
    * SHA512 (128 chars)
* **MD5 Generator:** Securely converts plaintext strings into MD5 hash digests using UTF-8 encoding.
* **Dual Mode:** Supports both an interactive menu and command-line arguments for quick checks.
* **Input Validation:** Validates hexadecimal format to prevent errors.

## ⚙️ Design & Methodology
The detection logic is built on the principle of **fixed-length output**. Cryptographic hash functions produce digests of specific lengths regardless of input size. This tool analyzes the length of the provided hex string to infer the algorithm used.

## 🚀 Installation
No external libraries are required. Ensure you have Python 3 installed.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/alaabaniarshad-crypto/eth-hacker-hash-detector-baniirshed-202220431.git](https://github.com/alaabaniarshad-crypto/eth-hacker-hash-detector-baniirshed-202220431.git)
    cd eth-hacker-hash-detector-baniirshed-202220431
    ```

2.  **Run the tool:**
    ```bash
    python3 hash_task1.py
    ```

## 📖 Usage

### 1. Interactive Mode (Menu)
Simply run the script without arguments to enter the menu:
```bash
python3 hash_task1.py
