def Upper(text):
    z=str(text)
    ciphertext=z.upper()
    return ciphertext

def Lower(text):
    d=str(text)
    ciphertext=d.lower()
    return ciphertext

def Reverse(text):
    s=str(text)
    ciphertext= s[::-1]
    return ciphertext

if __name__=="__main__":
    text= input("Enter the text to operate: ")
    choice = input("Enter your choice (u for uppercase / l for lowercase / r for reverse): ")
    if choice=='u':
        print(Upper(text))
    elif choice=='l':
        print(Lower(text))
    elif choice =='r':
        print(Reverse(text))
    else:
        print("Invalid choice!")
        
