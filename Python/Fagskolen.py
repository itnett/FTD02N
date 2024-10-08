python
import hashlib
import sys

def read_file(file_path):
    """
    Reads the contents of a file in binary mode.
    """
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        sys.exit(1)

def write_hash(file_path, file_hash):
    """
    Writes the hash to a file.
    """
    try:
        with open(f"{file_path}.sha256", 'w') as hash_file:
            hash_file.write(file_hash)
        print(f"Hash for {file_path} generated and saved as {file_path}.sha256")
    except IOError as e:
        print(f"Error writing hash file for {file_path}: {e}")
        sys.exit(1)

def generate_hash(file_path):
    """
    Generates a SHA256 hash for the given file and saves it.
    """
    file_content = read_file(file_path)
    file_hash = hashlib.sha256(file_content).hexdigest()
    write_hash(file_path, file_hash)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hash-generator3.py <file_path>")
        sys.exit(1)
    generate_hash(sys.argv[1])