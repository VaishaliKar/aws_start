# Open a file
fo=open('Modules.py', 'w')
print("Modules.py: ", fo.name)
fo.write("print('welcome to the world of Python')");
print("Closed ? :", fo.closed)
print("Opening mode : ", fo.mode)
fo.close()

#readfile.py

f = open('Modules.py', 'r')
for line in f:
    print("Hello\n") ## iterates over the lines of the file
    print(line)
f.close()
