def loadFile(path):
    vals = []
    with open(path, "r") as data_file:
        data_file.readline() # ignore the first line
        for line in data_file:
            vals_str = line.split(",")[:-1]
            vals_float = list(map(float, vals_str))
            vals.append(vals_float)
    return vals

def parseFileIntoColumns(path):
    frame = loadFile(path)
    columns = []
    for i in range(4):
        column = []
        for row in frame:
            column.append(row[i])
        columns.append(column)
    return columns