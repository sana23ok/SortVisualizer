import os


def convert(int_array):
    return [str(element) for element in int_array]


def saveInTxtFile(array, mode):
    with open('temp.txt', mode) as file:
        if mode == 'w':
            state = "Unsorted array:\n"
        else:
            state = "Sorted array:\n"
        file.write(state)
        elements_per_line = 20
        elements = convert(array)

        for i in range(0, len(elements), elements_per_line):
            line = ', '.join(map(str, elements[i:i + elements_per_line])) + '\n'
            file.write(line)


def appendOperations(swap, comp, rec, max):
    with open('temp.txt', 'a') as file:
        file.write("Number of swaps: {}\n".format(swap))
        file.write("Number of comparisons: {}\n".format(comp))
        file.write("Recursion depth: {}\n".format(rec))
        file.write("Max depth: {}\n".format(max))

@staticmethod
def deleteFile(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' has been deleted.")
    except OSError as e:
        print(f"Error deleting the file: {e}")
