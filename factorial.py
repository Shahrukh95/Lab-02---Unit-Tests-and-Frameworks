class factorial:

    def find_factorial(self, num):
        if isinstance(num, int):                    #Check if input is integer
            if num < 0:                             #Check if Number is Negative
                print "Value is Less Than Zero"
                return None
            if num >= 999:                          #Check to see if the value is greater than or equal to the Maximum Limit of Recursion
                print "Value exceeds the recursion Limit. Use a lower value"
                return None

            if num is 0:                            #If Value is 0
                return 1
            if num is 1:                            #If Value is 1
                return num

        if isinstance(num, str):                    #If the value is a string
            print "Enter a Valid Integer"
            return None


        return num*self.find_factorial(num - 1)     #Recursive to call to calculate factorial