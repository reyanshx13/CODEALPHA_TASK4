#basic chatbot
with open("chatbot.txt")as f:
    r=f.readlines()
    
    a=input("write anyhting:")    
    for i in r:
        i=i.strip().lower()
        if i=="hello" and a=="hello":
                print("hi")
            
        elif i=="how are you"and a=="how are you":
                print("I m fine")
            
        elif i=="bye" and a=="bye":
                print("Goodbye")
            