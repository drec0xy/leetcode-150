"""
20. Valid Parentheses
Easy
19.6K
1.1K
Companies
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

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
        
