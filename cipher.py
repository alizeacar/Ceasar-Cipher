def encrypt(text,key):
    encrypt=""

    for c in text:
        if c.isupper():
            index=ord(c)-ord('A')
            shift=(index+key)%26+ord('A')
            new=chr(shift)
            encrypt+=new
        elif c.islower():
            index=ord(c)-ord('a')
            shift=(index+key)%26+ord('a')
            new=chr(shift)
            encrypt+=new
        elif c.isdigit():
            new=(int(c)+key)%10
            encrypt+=str(new)
        else:
            encrypt+=c
    return encrypt


def decrypt(cipher,key):
    decrypt=""
    for x in cipher:
        if x.isupper():
            index=ord(c)-ord('A')
            pos=(index-key)%26+ord('A')
            of=chr(pos)
            decrypt+=of
        elif x.islower():
            index=ord(x)-ord('a')
            pos=(index-key)%26+ord('a')
            of=chr(pos)
            decrypt+=of
        elif x.isdigit():
            of=(int(x)-key)%10
            decrypt+=str(of)
        else:
            decrypt+=x
    return decrypt
def main():
  message = input("Enter your message: ")
  print(message)
  skey=int(input("Enter your key: "))
  print(skey)
  ciphertext=encrypt(message,skey)
  print("Plain text message:\n", message)
  print("Encrypted ciphertext:\n", ciphertext)
  decrypted =decrypt(ciphertext,skey)
  print("The cipher text:\n", ciphertext)
  print("The decrypted message is:\n",decrypted)
main()
