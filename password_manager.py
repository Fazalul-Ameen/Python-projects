from cryptography.fernet import Fernet

def add():
    username = input("Username : ")
    pwd = input("Password : ")
    with open("passwords.txt", "a") as f:
        f.write(username + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        f.close()

def view():
    with open("passwords.txt", "r") as f:
        for ln in f.readlines():
            data = ln.rstrip()
            user, passwd = data.split("|")
            print("Username : " + user +" || Password : " + fer.decrypt(passwd.encode()).decode())

'''def generatekey():
    key = Fernet.generate_key()
    with open("Key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("Key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Master password : ")
key = load_key()+master_pwd.encode()
fer = Fernet(key)


while True:
    mode = input("Add (add)/View (view)/quit (q) : ").lower()
    if mode == "q":
        break
    
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid choice!")