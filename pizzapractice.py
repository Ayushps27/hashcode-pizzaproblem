def func(in_filename, out_filename):
    input_file = open(in_filename, 'r')
    output_file = open(out_filename, 'w')
    line1 = input_file.readline()

    slices, types = line1.split(" ")
    slices = int(slices)
    arr = [int(i) for i in input_file.readline().split()]

    # print(slices,types,arr)

    arrdec = arr[::-1]
    # print(arrdec)
    # outslices=[]
    outsliceindex = []

    for i in range(len(arrdec)):
        if slices - arrdec[i] >= 0:
            # outslices.append(i)
            outsliceindex.append(len(arrdec) - i - 1)
            slices -= arrdec[i]

    # print(outslices)
    # print(outsliceindex)
    # outsliceindex.reverse()

    output_file.write(str(len(outsliceindex)) + "\n")
    for i in outsliceindex:
        output_file.write(str(i) + " ")


if __name__ == '__main__':
    infiles = ['a_example.in', 'b_small.in', 'c_medium.in', 'd_quite_big.in', 'e_also_big.in']
    outfiles = ['a_example.out', 'b_small.out', 'c_medium.out', 'd_quite_big.out', 'e_also_big.out']
    for i in range(5):
        func(infiles[i], outfiles[i])
