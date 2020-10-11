import easygui

class bubble_sort():

    def bubbleSort(self,arg):
        self.n = len(arg)
        for i in range(self.n - 1):
            for x in range(0, self.n - i - 1):
                if arg[x] > arg[x + 1]:
                    arg[x], arg[x + 1] = arg[x + 1], arg[x]