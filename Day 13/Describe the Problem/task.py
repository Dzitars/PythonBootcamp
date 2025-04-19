def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# The for loop is running 19 times, looking to see if the number is 20 and when it is, it prints out "you got it"
# 2. When is the function meant to print "You got it"?
# When i = 20, the 20th iteration of the loop
# 3. What are your assumptions about the value of i?
# range() doesn't include the max value in the range, so it goes between 1-19
