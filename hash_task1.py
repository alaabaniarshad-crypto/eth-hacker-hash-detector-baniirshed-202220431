import sys
import hashlib
import re

def identify_hash_type(hash_str):
    """
    Detects hash type based on length of the hex string.
    Supported types: MD5, SHA1, SHA256, SHA384, SHA512.
    """
    hash_str = hash_str.strip()
    
    if not re.match(r'^[0-9a-fA-F]+$', hash_str):
        return "Error: Input is not a valid Hexadecimal string."

    length = len(hash_str)
    if length == 32:
        return "Possible Hash Type: MD5"
    elif length == 40:
        return "Possible Hash Type: SHA1"
    elif length == 64:
        return "Possible Hash Type: SHA256"
    elif length == 96:
        return "Possible Hash Type: SHA384"
    elif length == 128:
        return "Possible Hash Type: SHA512"
    else:
        return f"Unknown Hash Type (Length: {length}). Not one of the standard 5 required."

def generate_md5(text):
    """
    Generates an MD5 hash from a plaintext string.
    Uses UTF-8 encoding as required.
    """
    try:
        md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
        return md5_hash
    except Exception as e:
        return f"Error generating hash: {e}"

def print_banner():
    print("-" * 40)
    print("   Ethical Hacker Hash Tool (Task 1)")
    print("-" * 40)

def interactive_mode():
    """
    Runs the tool in interactive menu mode.
    """
    while True:
        print_banner()
        print("1. Detect Hash Type")
        print("2. Generate MD5 Hash")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            user_input = input("Enter the hash string: ").strip()
            if user_input:
                print(f"\nResult: {identify_hash_type(user_input)}\n")
            else:
                print("\n[!] Error: Empty input.\n")
                
        elif choice == '2':
            user_input = input("Enter plaintext to hash: ")
            print(f"\nMD5 Output: {generate_md5(user_input)}\n")
            
        elif choice == '3':
            print("Exiting tool...")
            break
        else:
            print("\n[!] Invalid choice, please try again.\n")

def main():
    if len(sys.argv) > 1:
        input_hash = sys.argv[1]
        print(f"Input: {input_hash}")
        print(f"Result: {identify_hash_type(input_hash)}")
    else:
        interactive_mode()

if __name__ == "__main__":
    main()
