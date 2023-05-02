def isValid(myString):
    parantheses_state = 0 #these are parantheses { and }
    braces_state = 0    #these are braces ( and )
    brackets_state = 0  #these are brackets [ and ]
    for i in myString:
        match i:
            case "{":
                parantheses_state += 1 
            case "}":
                parantheses_state -= 1 
            case "[":
                brackets_state += 1  
            case "]":
                brackets_state -= 1  
            case "(":
                braces_state += 1
            case ")":
                braces_state -= 1

    print("parantheses_state: ",parantheses_state, "braces_state: ",braces_state,"brackets_state: " ,brackets_state)

    if(parantheses_state == 0 and  braces_state == 0 and brackets_state == 0):
        print("True")
        return True
    else:
        print("False")
        return False        

brakets = input("Enter backets: ")
isValid(brakets)
        
