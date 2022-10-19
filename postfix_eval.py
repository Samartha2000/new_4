import infix_postfix
import mystack
def cal(char,op2,op1):
    if char=="+":
        return int(op2)+int(op1)
    elif char=="-":
        return int(op2)-int(op1)
    elif char=="*":
        return int(op2)*int(op1)
    elif char=="/":
        return int(op2)/int(op1)        

def postfix_eval(postfix):
    for i in postfix:
        if i.isdigit():
            mystack.push(i)
        else:
            op1=mystack.pop()
            op2=mystack.pop()
            expr=cal(i,op2,op1) 
            mystack.push(expr)
    return mystack.pop()           

expr = input('Enter infix expression:\n')
print('infix notation: ',expr)
postfix=infix_postfix.infx_postfx(expr)
print('postfix notation: ',postfix) 
print("Postfix Evalaution:",postfix_eval(postfix))