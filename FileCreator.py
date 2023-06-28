import os


def convert(int_array):
    return [str(element) for element in int_array]


@staticmethod
def deleteFile(filename):
    if os.path.exists(filename):
        os.remove(filename)
        # print(f"File '{filename}' has been deleted.")


class File:
    def __init__(self, tempFile):
        self.__temp = tempFile

    def saveInTxtFile(self, array, mode):
        if array:
            with open(self.__temp, mode) as file:
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

    def appendOperations(self, swap, comp, rec, maximum_depth):
        if os.path.exists(self.__temp):
            with open(self.__temp, 'a') as file:
                file.write("Number of swaps: {}\n".format(swap))
                file.write("Number of comparisons: {}\n".format(comp))
                file.write("Recursion depth: {}\n".format(rec))
                file.write("Maximum depth: {}\n".format(maximum_depth))

    @property
    def fileName(self):
        return self.__temp
