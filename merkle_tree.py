import hashlib
import sys
import os

def hash_file(filepath):
    hasher = hashlib.sha1()

    with open(filepath, "rb") as f:
        chunk = f.read(8192)
        while chunk:
            hasher.update(chunk)
            chunk = f.read(8192)

    return hasher.hexdigest()

def hash_pair(left, right):
    hasher = hashlib.sha1()
    hasher.update((left + right).encode())
    return hasher.hexdigest()

def build_tree(files):
    hashes = []

    for file in files:
        if not os.path.exists(file):
            print("File not found:", file)
            sys.exit()

        hashes.append(hash_file(file))

    while len(hashes) > 1:
        new_level = []

        for i in range(0, len(hashes), 2):
            left = hashes[i]

            if i + 1 < len(hashes):
                right = hashes[i + 1]
            else:
                right = left

            new_level.append(hash_pair(left, right))

        hashes = new_level

    return hashes[0]

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("python merkle_tree.py file1 file2 file3")
        return

    files = sys.argv[1:]
    top_hash = build_tree(files)

    print()
    print("Top Hash:")
    print(top_hash)

if __name__ == "__main__":
    main()