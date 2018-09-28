class Matrix:

    __id = 0

    def __init__(self, str = ''):

        if not str:                  #if the argument "str" is empty (default)
            self.str = ' '
        else:
            self.str = str
        self.id = Matrix.__id
        Matrix.__id += 1

#The rows method
    def rows(self):
        return len(self.str)

#The coloumns method
    def cols(self):
        return len(self.str[0])

#The dimensions method = "rows"x"coloumns"
    def dimensions(self):
        return "{}x{}".format(len(self.str), len(self.str[0]))

#The decription method, lists the entire matrix row by row
    def description(self):
        if self.str == ' ':
            str_def = [0]
            return str_def
        str1 = "["  #output string
        for i2 in range(0, len(self.str)):
            if i2 == len(self.str)-1:
                str1 += "{}".format(self.str[i2])    #A condition for the last iteration to remove '\n' after last row
                break
            else:
                str1 += "{}\n".format(self.str[i2])
        return str1+']'

#Returns the incremental instance id
    def get_id(self):
        return self.id


#Pre-made examples

A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]])

B = Matrix()      #Empty matrix

print(A.rows())
print(A.cols())
print(A.dimensions())
print(A.description())
print(A.get_id())
print("---------------")
print(B.get_id())
print(B.rows())
print(B.cols())
print(B.dimensions())
print(B.description())
print(B.get_id())