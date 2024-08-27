python
import hashlib
import sys

def generate_hash(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
            file_hash = hashlib.sha256(file_content).hexdigest()
            with open(f"{file_path}.sha256", 'w') as hash_file:
                hash_file.write(file_hash)
            print(f"Hash for {file_path} generated and saved as {file_path}.sha256")
    except IOError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hash-generator3.py <file_path>")
        sys.exit(1)
    generate_hash(sys.argv[1])