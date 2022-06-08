to_do = input('What would you like to do? ')
#reading file
with open('toDo.txt', 'r') as toDo_file:
    contents = toDo_file.read()

#adding contents to file
contents = contents+to_do + "\n"

#writing to file
with open('toDo.txt', 'w+') as toDo_file:
    toDo_file.write(contents)
    print(contents)