memory = 0

def add(bt):
    global memory
    memory += bt_to_int(bt)
    return

def subtract(bt):
    global memory
    memory -= bt_to_int(bt)
    return

def multiply(bt):
    global memory
    memory = memory * bt_to_int(bt)
    return

def divide(bt):
    global memory
    memory = memory // bt_to_int(bt)
    return

def remainder(bt):
    global memory
    memory = memory % bt_to_int(bt)
    return

def negate():
    global memory
    memory = memory * -1
    return

def store(bt):
    global memory
    memory = bt_to_int(bt)
    return

def bt_to_int(bt):
    a = 0
    for n in range(len(bt)):
        if bt[n] == "N":
            a += (3 ** (len(bt) - 1 - n)) * -1
        else:
            a += (3 ** (len(bt) - 1 - n)) * int(bt[n])
    return a
    
def int_to_btpos(n):
    a = ""
    if n == 0:
        return "0"
    b = n
    while b != 0:
        if b // 3 != 0:         ## when b is bigger than 2
            if b % 3 == 1:
                a = "1" + a
                b = (b - 1) // 3
            elif b % 3 == 2:
                a = "N" + a
                b = (b + 1) // 3
            elif b % 3 == 0:
                a = "0" + a
                b = b // 3
        elif b // 3 == 0:       ##comes here when b = 1, 2
            if b % 3 == 1:
                a = "1" + a
                b = 0
            elif b % 3 == 2:
                a = "1N" + a
                b = 0
    return a

def int_to_bt(n):
    a = ""
    if n >= 0:
        return int_to_btpos(n)
    else:
        for b in range(len(int_to_btpos(-n))):
            if int_to_btpos(-n)[b] == "0":
                a = a + "0"
            elif int_to_btpos(-n)[b] == "1":
                a = a + "N"
            elif int_to_btpos(-n)[b] == "N":
                a = a + "1"
    return a

def memory_as_int():
    return memory

def memory_as_bt():
    return int_to_bt(memory)

def evaluate2(string):
    global memory
    opr = ""
    nmr = ""
    for n in range(len(string)):
        if string[n] == " ":
            pass
        elif string[n] in "+-*/%=":
            opr += string[n]
            if len(opr) == 2:
                return "operator error"
        elif string[n] in "10N":
            if len(opr) == 0:
                return "needs an operator"
            nmr = nmr + string[n]
            if n == len(string) - 1:
                calculate(opr, nmr)
                opr = ""
                nmr = ""
            elif string[n + 1] not in "10N":
                calculate(opr, nmr)
                opr = ""
                nmr = ""
        else:
            return "invalid input"
    return memory_as_bt()
            
def calculate(a, b):
    if a == "+":
        add(b)
    elif a == "-":
        subtract(b)
    elif a == "*":
        multiply(b)
    elif a == "/":
        divide(b)
    elif a == "%":
        remainder(b)
    elif a == "=":
        store(b)

def evaluate(string):
    try:
        return evaluate2(string)
    except ZeroDivisionError:
        return "Division by 0"
    except Exception:
        return "unknown error"
    
def REPL():
    cal = "dog"
    while cal != "quit":
        cal = input("input BT calculation : ")
        if cal == "quit":
            print("Thank you!")
            break
        print(evaluate(cal))

if __name__ == '__main__':
    REPL()
