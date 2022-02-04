

def view():

    with open("Passwords.txt", "r+") as pw:
        for line in pw.readlines():
            data=line.rstrip()
            Usm,Psw = data.split("||")
            print(f"{Usm} \n {Psw}")


def add():
    User_Name = input("Enter Your Name : ")
    Password = input("Enter Your New Password : ")

    with open("Passwords.txt", "a") as pw:
        # pw.write("User Name : "+ User_Name + "||" + "Password : "+ Password + "\n")
        pw.write(f"User Name : {User_Name}" + "||" + f"Password : {Password}")

    # print(f" User Name is {User_Name} \n Password is {Password}")


while(True):

    Stats = input(
        "Welcome to Password Manager.\n What Do You Want To Do ? \n 1. View \n 2. Add New \n 3. Press 'q' To Quit \n").lower()
    if Stats == "q":
        break

    if Stats == "view":
        view()

    elif Stats == "add":
        add()
    else:
        print("Try Again")
        continue
