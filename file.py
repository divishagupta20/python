with open('example.txt','r') as file:
    content = file.read()
    print(content)
 
with open('dest.txt','w') as file:
    file.write(content)

    with open('example.txt','r') as file:
        for line in file:
            print(line.strip())

    
    with open('example.txt','w') as file:
     file.write('hello \n')
     file.write("world \n")
     #overrides

    with open('example.txt','a') as file:
       file.write("text is appended")

    
    lines = ["there are \n","infinte stars \n","in universe"]

    with open('example.txt','a') as file:
       file.writelines(lines)

    
    with open('source.txt','w+') as file:
       file.write("hiii my name is divisha gupta \n")
       file.write("hiii my name is divisha gupta \n")

    #file.seek(0)

    with open('source.txt','r') as file:
       cont = file.read()
       print(cont)