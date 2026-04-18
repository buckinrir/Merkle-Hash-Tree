# Merkle Hash Tree for Integrity Check of Files

## Description

For this assignment, I created a Python program that computes the Top Hash of a Merkle Hash Tree using multiple input files. The program reads each file and generates a hash value using the SHA1 hashing algorithm. Then it combines the hashes in pairs and continues hashing them until only one final value remains, which is the Top Hash.

The purpose of this program is to demonstrate file integrity checking. If any file is changed, the final Top Hash will also change.

## Files Included

- merkle_tree.py — main program that builds the Merkle Hash Tree  
- file1.txt — sample test file  
- file2.txt — sample test file  
- file3.txt — sample test file  
- file4.txt — sample test file  
- output_before.txt — program output before modifying a file  
- output_after.txt — program output after modifying a file  

## How to Run the Program

Run the program from the command line using:

python merkle_tree.py file1.txt file2.txt file3.txt file4.txt

## Testing

I first ran the program using four files and recorded the Top Hash.  
Then I modified file3.txt by changing the text from:

"This is file three."

to:

"This file has been modified."

After running the program again, the Top Hash changed. This shows that the program can detect when a file has been altered.
