from cryptography.fernet import Fernet

key = Fernet.generate_key()     #Generates random key from Fernet Class - helps to decrypt

msg = "Welcome to channel" . encode()  #to encode into bytes

Obj_1 = Fernet(key)

#ENCRYPTION -->

Encrypt_Msg = Obj_1.encrypt(msg)

print(f"Encrypted Message : {Encrypt_Msg}")

#DECRYPTION -->

Decrypt_Msg = Obj_1.decrypt(Encrypt_Msg)

print(f"Decrypted Message : {Decrypt_Msg}")




