password1 = "Chupacabra"

while True:
    password2 = input("Please write your password: ")
    if password2 != password1:
        break 
    elif password2 == password1:
        print("You've succesfully left the loop")
        
    
    