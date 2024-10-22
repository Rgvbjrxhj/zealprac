class num:
    def __init__(self,my_int):
        self.int_input=my_int

    def reverse(self):
        int_to_str=str(self.int_input)
        str_reverse=int_to_str[ : :-1]
        return int(str_reverse)
    
a1=num(12345)
print(a1.reverse())  # Output: 54321