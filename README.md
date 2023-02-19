# AdRSCiE
Advanced Random Substitution Cipher Encryption

Video demo: [Watch on YouTube](https://youtu.be/K14FsJDuOeQ)

## Explanation
AdRSCiE is a program that converts any text/code file into a secret code text file with a key. It uses substitution cipher as the base algorithm. You can decrypt the file with and only with the key which was generated during the encryption.

### Usage

#### 1) For encryption:
```
python adrscie.py -e
```
or
```
python adrscie.py --encrypt
```
It will prompt you for a file name. The file to encrypt should be in the root folder. Type the file name and hit enter. File name should not contain any whitespaces. The program will output a text file with encrypted text and a ket.txt file with the key.

#### 2) For decryption
```
python adrscie.py -d
```
or
```
python adrscie.py --decrypt
```
It will prompt you for a text file. The file should be in root folder. Then it will again prompt you for the key file and it should also be in .txt format. There should not be any whitespaces in the file name. The program will output the original file with original name and extension in the `decrypted folder`.
