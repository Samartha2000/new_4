import mystack 

def priority(char):  # check priority of operator
    arith_operator = {"-": 1, "+": 2, "*": 3, "/": 4}
    return arith_operator.get(char)

def infx_postfx(expr):
    output=[]
    expr_str=""
    for i in expr:
        if i.isdigit():  # if operand then direct push
            output.append(i)
        else:
            if i == "(":
                mystack.push(i)
            elif i == ")":  # if ) then empty till opning bracket
                while mystack.isempty() != True and mystack.peak() != "(":
                    temp= mystack.pop()
                    output.append(temp)
                mystack.pop()
            else:                # if operator then
                #higher priority in stack
                while mystack.isempty() != True and mystack.peak() != "(" and  priority(i) <= priority(mystack.peak()):
                    temp= mystack.pop()
                    output.append(temp)
                mystack.push(i)
    while mystack.isempty()!=True:          #emptying stack after operation
        temp= mystack.pop()
        output.append(temp) 
    for i in output:
        expr_str=expr_str+i           
    return expr_str


"""expr = input('Enter infix expression:\n')
print('infix notation: ',expr)
print('postfix notation: ',infx_postfx(expr)) """                     
