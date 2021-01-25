
def division(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as messageError:
        print('Log:', messageError)
        raise

try:
    answer = division(4,0)
    print(answer)
except ZeroDivisionError as messageError:
    print(messageError)
