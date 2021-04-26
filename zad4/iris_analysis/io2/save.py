def saveResults(path, vals_table):
    with open(path, "w") as output_file:
        for row in vals_table:
            vals_str = list(map(str, row))
            res = ",".join(vals_str)
            output_file.write(res)
            output_file.write("\n")