def func(in_filename, out_filename):
    input_file = open(in_filename, 'r')
    output_file = open(out_filename, 'w')
    line1 = input_file.readline()
    
    #READING FILES TO RESPECTIVE VARIABLES
    slices, types = line1.split(" ")
    slices = int(slices)#type conversion from str to int
    arr = [int(i) for i in input_file.readline().split()]

    arrdec = arr[::-1]#reversing list to get no. of slices in devreasing order
    outsliceindex = []#new list to store indexes of selected pizza types

    for i in range(len(arrdec)):
        if slices - arrdec[i] >= 0:
            outsliceindex.append(len(arrdec) - i - 1)#storing index of eligible pizza to the list
            slices -= arrdec[i]
    
    #WRITING OUTPUT TO FILE
    output_file.write(str(len(outsliceindex)) + "\n")
    for i in outsliceindex:
        output_file.write(str(i) + " ")


if __name__ == '__main__':
    infiles = ['a_example.in', 'b_small.in', 'c_medium.in', 'd_quite_big.in', 'e_also_big.in']
    outfiles = ['a_example.out', 'b_small.out', 'c_medium.out', 'd_quite_big.out', 'e_also_big.out']
    for i in range(5):
        func(infiles[i], outfiles[i])
