#EXERCISE1

#is_even = lambda x: x % 2 == 0
#evens =list(filter(lambda x: x % 2 == 0, numbers))

#num = int(input("Enter a number: "))

#if is_even(num):
#    print("The number is even.")
#else:
#    print("The number is odd.")
    
#exercise2
#using lambda to sort a list of words by their length
words = ['Cherry', 'Banana', 'Date', 'Apple', 'Mango', 'DragonFruit']

sorted_words = sorted(words, key=lambda word: len(word))

print(sorted_words)

#exe3 fibinacci 

#fibonacci < 10
#def fibonacci_range(limit):
#    a, b = 0, 1
#
#   while a <= limit:
#        print(a, end=" ")
#        a, b = b, a + b
#
#fibonacci_range(10)

#first ten fibonacci 
a, b = 0, 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b