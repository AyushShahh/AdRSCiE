from sys import exit, argv
from random import sample, choice
import os



extensions = ["txt", "py", "c", "cpp", "html", "htm", "css", "js", "csv", "sql", "xml", "eml", "bat", "asp", "aspx", "pl", "jsp", "php", "rss", "xhtml",
              "class", "h", "cs", "java", "sh", "vbs", "swift", "tsx", "jsx", "coffee"]
alphabets = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = ["\\-I", "\\-U", "\\-B", "\\-T", "\\-Q", "\\-P", "\\-H", "\\-D", "\\-N", "\\-O"]
spaces = [":/." + c for c in list("ALYJK")]
newlines = [":/." + c for c in list("MDRGV")]
new_string = []
new_numbers = []
space = ""
newline = ""



def main():
    global space
    global newline
    global new_string
    global new_numbers

    E = False

    if len(argv) != 2:
        exit("Invalid number of arguments.\nUsage: python project.py [(-e / --encrypt) | (-d / --decrypt)]")
    else:
        flag = argv[1]
        if flag in ["-e", "--encrypt"]:
            E = True
        elif flag not in ["-d", "--decrypt"]:
            exit("Invalid argument.\nUsage: python project.py [(-e / --encrypt) | (-d / --decrypt)]")

    print("All files must be in the root folder")

    try:
        name, extension = input("File name: ").strip().split(".")
        if " " in name:
                exit("Please provide a file name that doesn't contain any whitespaces")
        if E:
            if extension not in extensions:
                exit("Currently only readable text files are convertible. Please provide a file with .txt, .py, etc extension")
        else:
            if extension != "txt":
                exit("Encrypted files are always in txt format and decryption only expects a txt file")
            kname, kextension = input("Key file name: ").strip().split(".")
            if " " in kname:
                exit("Please provide a file name that doesn't contain any whitespaces")
            elif kextension != "txt":
                exit("Key file is always a txt file")
    except KeyboardInterrupt:
        exit("\nReturned from program in between with ctrl + c")
    except ValueError:
        exit("please type a valid filename: [name.extension]")

    enc = []
    if E:
        try:
            with open(f"{name}.{extension}") as file:
                space = choice(spaces)
                newline = choice(newlines)
                new_string = sample(alphabets, 52)
                new_numbers = sample(numbers, 10)
                for line in file:
                    enc.append(encrypt(line))
        except FileNotFoundError:
            exit("No such file exists in the root of this directory")

        with open(f"{''.join(sample(alphabets, 9))}.txt", "w") as file:
            file.write("".join(enc))
        with open(f"key.txt", "w") as file:
            file.write(gen_key(name, extension))
            print("File and key generated. Keep the key safe and do not lose the key. It's impossible to decrypt your file without the key. Anyone with the key can decrypt your file")
    else:
        key = {}
        try:
            with open(f"{kname}.txt") as file:
                key = decrypt_key(file.readlines()[0])
            with open(f"{name}.txt") as file:
                for line in file:
                    enc.append(decrypt(line, key))
        except FileNotFoundError:
            exit("No such file exists in the root of this directory")

        if not os.path.exists('decrypted'):
            os.makedirs('decrypted')

        with open(f"./decrypted/{decrypt(key['name'], key)}.{decrypt(key['extension'], key)}", "w") as file:
            file.write("".join(enc))
            print("Decryption successful and file saved in decrypted folder")



def gen_key(n, e):
    n = encrypt(n)
    e = encrypt(e)
    return (
         numbers[len(n)].replace('\\-', '') + n + space + "".join(new_string) + "".join(new_numbers).replace('\\-', '') + newline + e
        )


def decrypt_key(key):
    n = [i.replace("\\-", "") for i in numbers]
    if len(key) < 73:
        exit("Invalid key")
    elif key[0] not in n:
        exit("Invalid key")

    name_length = numbers.index(f"\\-{key[0]}")
    name = key[1:name_length+1]
    space = key[name_length+1:name_length+5]
    new_string = list(key[name_length+5:name_length+57])
    new_numbers = list(key[name_length+57:name_length+67])
    newline = key[name_length+67:name_length+71]
    extension = key[name_length+71:]

    if space not in spaces:
        exit("Invalid key")
    elif newline not in newlines:
        exit("Invalid key")
    elif set(new_string) != set(alphabets):
        exit("Invalid key")
    elif set(new_numbers) != set(n):
        exit("Invalid key")

    for i in range(len(new_numbers)):
        new_numbers[i] = "\\-" + new_numbers[i]

    return {
        'name': name,
        'space': space,
        'new_string': new_string,
        'new_numbers': new_numbers,
        'newline': newline,
        'extension': extension
    }


def encrypt(s):
    s = s.replace(" ", f"{space}").replace("\n", f"{newline}")
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            s[i] = new_string[alphabets.index(s[i])]
        elif s[i].isdigit():
            s[i] = new_numbers[int(s[i])]
    return "".join(s)


def decrypt(s, key):
    s = list(s)
    for i in range(len(s)):
        fir = i + 1
        sec = i + 2
        if s[i] in key['new_string']:
            s[i] = alphabets[key['new_string'].index(s[i])]
        elif sec < len(s) and (s[i] + s[fir] + s[sec]) in key['new_numbers']:
            s[i] = str(key['new_numbers'].index(f"\\-{s[sec]}"))
            s[fir] = s[sec] = ""
    s = "".join(s)
    s = s.replace(f"{key['space']}", " ").replace(f"{key['newline']}", "\n")
    return s



if __name__ == "__main__":
    main()