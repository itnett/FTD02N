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

def read_hash(hash_file_path):
    """
    Reads the stored hash from the hash file.
    """
    try:
        with open(hash_file_path, 'r') as hash_file:
            return hash_file.read().strip()
    except IOError as e:
        print(f"Error reading hash file {hash_file_path}: {e}")
        sys.exit(1)

def compare_hashes(file_path, hash_file_path):
    """
    Compares the hash of a file to a stored hash.
    """
    file_content = read_file(file_path)
    stored_hash = read_hash(hash_file_path)
    
    file_hash = hashlib.sha256(file_content).hexdigest()
    
    if file_hash == stored_hash:
        print("The file has not been changed.")
    else:
        print("The file has been changed.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python hash-comparator.py <file_path> <hash_file_path>")
        sys.exit(1)
    compare_hashes(sys.argv[1], sys.argv[2])