# create all possible letter combinations
# create their respective unique code
#
#
#

print("---------WELCOME TO MESSAGE ENCODER-DECODER---------")
print("-----AUTHOR : Rajarshi Ray-----")


def workFunc():
    letters = 'abcdefghijklmnopqrstuvwxyz",.\/1234567890 !'
    codes = letters[-1] + letters[0:-1] 

    encryptMode = dict(zip(letters, codes))
    decryptMode = dict(zip(codes, letters))
    while(True):
        chooseMode = input("PRESS [E] TO ENCRYPT AND [D] TO DECRYPT AND [Q] TO QUIT: ")
        if chooseMode.upper() == "Q":
            break
        
        userInput = input("ENTER YOUR MESSAGE HERE : ")

        if chooseMode.upper() == "E":
            finalMessage = ''.join([encryptMode[items]
                                   for items in userInput.lower()])

        elif chooseMode.upper() == "D":
            finalMessage = ''.join([decryptMode[items]
                                   for items in userInput.lower()])

        

        print(finalMessage)


workFunc()
