
try:
    file = open('abc2.txt', 'w+')
    file.write('Linha')
    file.seek(0, 0)
    print(file.readline())
finally:
    file.close()
