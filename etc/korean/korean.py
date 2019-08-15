# 국어 수능특강 지문 중 스택을 이용한 중위표기법 > 후위표기법으로 변환해보기

def jung2hu(equation):
    sig = ['*','/','-','+','(',')']
    output = []
    stack = []
    for a in equation:
        if a in sig:
            
            
            if len(stack) == 0:
                stack.append(a)
            elif a=='+' or a=='-':

                if not stack[-1]=='(':
                    output.append(stack.pop())
                stack.append(a)
            elif a=='*' or a=='/':
                #print(stack,a)
                if stack[-1] == '*' or stack[-1]=='/':

                    output.append(stack.pop())
                    stack.append(a)
                else:
                    stack.append(a)
            elif a=='(':
                stack.append(a)
            elif a==')':

                asdf =True
                while(asdf):
                    pop_data = stack.pop()
                    if pop_data=='(':
                        asdf=False
                    else:
                        output.append(pop_data)

        else:
            output.append(a)
    [output.append(stack.pop())  for _ in range(len(stack))]
    print(stack)
    print(''.join(output))
jung2hu(input())
