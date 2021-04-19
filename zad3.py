from os import chdir, getcwd, listdir, mkdir, path
from random import randint

# part A
dir_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
subdir_names = ['morning', 'evening']
data_file_name = 'Solution.csv'

def createFilesAndDirectories():
    curr_dir = getcwd()
    
    dirs1 = [ path.join(curr_dir, d) for d in dir_names ]
    dirs2 = [ path.join(dir, d) for d in subdir_names for dir in dirs1 ]
    files = [ path.join(dir, data_file_name) for dir in dirs2 ]
    
    for d in dirs1 + dirs2:
        mkdir(d)
    for f in files:
        with open(f, 'w') as file:
            file.write('Model; Output value; Time of computation;\n')
            file.write(createContents())

def createContents():
    letter = ['A', 'B', 'C'][randint(0, 2)]
    output = randint(0, 1000)
    time = randint(0, 1000)

    contents = ' ; '.join((letter, str(output), str(time) + 's', ''))
    return contents

# part B
def countAModels(curr_dir = None):
    if curr_dir == None:
        curr_dir = getcwd()

    total_time = 0

    data_file_path = path.join(curr_dir, data_file_name)
    if path.exists(data_file_path):
        with open(data_file_path) as data_file:
            total_time += extractData(data_file)
    
    for f in listdir(curr_dir):
        absolute_path = path.join(curr_dir, f)
        if path.isdir(absolute_path):
            total_time += countAModels(absolute_path)
    
    return total_time
    
def extractData(file):
    file.readline() # ignore the first line
    data = file.readline()
    split_data = data.split(';')
    
    if len(split_data) != 4:
        raise Exception("Incorrect format of the file!")
    else:
        clean_data = [ str.strip(entry) for entry in split_data ]
        if clean_data[0] == 'A':
            return int(clean_data[2][:-1])
        else:
            return 0

# ******************************************

# part A
createFilesAndDirectories()

# part B
no_of_A_models = countAModels()
print(no_of_A_models)