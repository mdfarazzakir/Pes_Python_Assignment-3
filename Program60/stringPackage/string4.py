"""
Strings :
Receive the encoded string from your friend & decode it to check the original message. PS: You will receive Encoded string and the Algorithm used for encoding.

"""

"""In this program the encyrption and decryption algorithmis based on Ceaser Cipher encryption where we encrypt a letter by skipping 2 alphabets after the
respective letter and then use the 3 letter to replce it. For example: A-->D, B-->E...."""
"""Code based on the provided algorithm to decrypt the message"""

"""This id the encyption code function just for information of how the message was encrypted"""
# def encrypt():
#     letters = 'abcdefghijklmnopqrstuvwxyzabc'
#     emessage = str()
#     message = input("Enter the string to encrypt and send: ").replace(" ","")
#     for i in message.lower():
#         pos = letters.find(i)
#         emessage = emessage+letters[pos+3]
#     print(emessage)


"""This is the decryption code function to decrypt the encrypted message from friend"""
def decrypt():
    letters = 'abcdefghijklmnopqrstuvwxyzabc'
    dmessage = str()
    emessage = input("Enter the string recieved from your friend: ")
    for i in emessage.lower():
        pos = letters.find(i)
        dmessage = dmessage+letters[pos-3]
    print(dmessage)

# encrypt()

"""Calling the functions"""
decrypt()

# Output:
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>python Program26.py
# Enter the string recieved from your friend: khoorzruog
# helloworld
#
# (base) C:\Users\faraz\Desktop\Python\Pes_Python_Assignment-2>
