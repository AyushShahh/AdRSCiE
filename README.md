# AdRSCiE
Advanced Random Substitution Cipher Encryption

Video demo: [Watch on YouTube](https://youtu.be/K14FsJDuOeQ)

## Explanation
AdRSCiE is a program that converts any text/code file into a secret code text file with a key. It uses substitution cipher as the base algorithm. You can decrypt the file with and only with the key which was generated during the encryption.

### Usage

#### 1) For encryption:
```
python project.py -e
```
or
```
python project.py --encrypt
```
It will prompt you for a file name. The file to encrypt should be in the root folder. Type the file name and hit enter. File name should not contain any whitespaces. The program will output a text file with encrypted text and a ket.txt file with the key.

#### 2) For decryption
```
python project.py -d
```
or
```
python project.py --decrypt
```
It will prompt you for a text file. The file should be in root folder. Then it will again prompt you for the key file and it should also be in .txt format. There should not be any whitespaces in the file name. The program will output the original file with original name and extension in the `decrypted folder`.

## Tech Stack
- Python

## Unit Tests
- Used Pytest. `test_project.py` contains four test functions. All functions pass the tests.

## Libraries Used (including built-in)
- os
- random
- pytest
- sys

## Explanation
There is only one file named `project.py` containing a main function with other function named `gen_key()` to generate the key, `encrypt()` to encrypt a string, `decrypt()` to decrypt the string and `decrypt_key()` to decrypt the key for decryption.

1) During Encryption

> When you run the code, the `numbers` and `alphabets` lists are randomly shuffled and the new generated lists are stored in `new_string` and `new_numbers` respectively. The `space` and `newline` strings are randomly chosen from the `spaces` and `newlines` lists. The input file is opened and while reading each line it is passed into the encrypt function and the encrypted text of each line is appended into a list. Then the key is genreated. After that the each item in the list is written into a file appending a newline character in the end. The key is written and outputted in another file.

2) During decryption

> The inputted key is passed into `decrypt_key()` function and it returns as a list the individual elements of the key like `space`, `newline`, etc variables. Each line of the input file is read and passed through the decrypt function with the key and each line of decrypted text is stored in a list. In the end each item of the lost is written to a file with the original name and extension and is saved in a different folder named `decrypted/`.