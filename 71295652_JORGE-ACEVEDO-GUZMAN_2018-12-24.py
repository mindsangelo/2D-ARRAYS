import cmd
import random
from statistics import mean

# Author : Jorge Acevedo Guzman
# Date: 24-12-2018
# This program allows the user generate a 2D-Array, populate ir automatically with unique random numbers
# and calculate how many odd columns sums are greater than the overall average of the sums of the even columns.


class MyPrompt(cmd.Cmd):
    intro = 'Welcome to the 2D-Arrays operating Shell, type "operate". Type help or ? to list commands. \n'

    def __init__(self):
        super(MyPrompt, self).__init__()

    # Commands
    def do_operate(self, line):
        even_columns_sum = []
        odd_columns_sum = []
        sum = 0
        even_avg = 0
        count = 0
        print("Let's define the size of the Array: \n")
        number_of_columns = int(input("Please type the number of columns N (N >= 2) : \n"))
        number_of_rows = int(input("Please type the number of rows M: ( M>= 2) \n"))
        my_list = random.sample(range(0, 99), number_of_rows*number_of_columns)
        print("The 2D-Array randomly generated is:  \n")
        my_array = [[my_list.pop() for i in range(number_of_columns)] for j in range(number_of_rows)]
        for r in my_array:
            for c in r:
                print(c, end=" ")
            print()
        for i in range(0, number_of_columns, 2):
            for j in range(0, number_of_rows, 1):
                sum += my_array[j][i]
            even_columns_sum.append(sum)
            sum =0
        print("The sums of the even columns are: \n", even_columns_sum)
        even_avg = mean(even_columns_sum)
        print("The average from the even columns is: \n", even_avg)
        for i in range(1, number_of_columns, 2):
            for j in range(0, number_of_rows, 1):
                sum += my_array[j][i]
            odd_columns_sum.append(sum)
            sum =0
        print("The sums of the odd columns are: \n", odd_columns_sum)
        for x in odd_columns_sum:
            if x > even_avg:
                count += 1
        print("The number of columns which sum is greater than the average of even columns is", count)

    def do_quit(self, line):
        print("Quitting..")
        raise SystemExit


if __name__ == '__main__':
    MyPrompt().cmdloop()
