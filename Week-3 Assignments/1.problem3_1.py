def problem3_1(txtfilename):
    """ Opens file and prints its contents line by line. """
    infile = open(txtfilename)

    sum = 0

    for line in infile:
        sum = sum + len(line)
        print(line, end="") # the file has "\n" at the end of each line already

    print("\n\nThere are", sum, "letters in the file.")

    infile.close()