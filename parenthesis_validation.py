import mystack
def balanced_parenthesis(expr):
    opening={"(":1,"[":2,"{":3}
    closing={")":1,"]":2,"}":3}
    for char in expr:
        if char in opening.keys():
            mystack.push(char)
        elif char in closing.keys():
            if mystack.isempty():
                return False
            elif closing.get(char)!=opening.get(mystack.pop()):   #matching with value of opening
                return False                                    #poping out opening bracket
    if mystack.isempty():
        return True                        #after process is stack empty
    else:
        return False

expr=input("Enter an Expression For Parenthesis Checking:")
print("Are the Parenthesis Balanced?",balanced_parenthesis(expr))                    
