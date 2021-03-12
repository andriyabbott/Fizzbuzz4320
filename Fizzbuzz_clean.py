#Getting Fizzbuzz to be clean

#creating a list named "fizzbuzz" as it potentially avoids concatenation of large strings

fizzbuzz=[]

#Initializing the range as a seperate variable "fizzbuzzRange"

fizzbuzzRange = range(101)

#Instantiating the for loop that utilizes the variable "fizzbuzzRange" above as its range

for n in fizzbuzzRange:
    
    #initializing an empty string "output" that is used to insert "Fizz", "Buzz" and "FizzBuzz.
    output =''
    
    #Checks if the number is a multiple of three, and if it is, there is an output of "Fizz"
    if n%3 ==0:
        output += "Fizz"
        
    #Checks if the number is a multiple of both three as well as five and if not, it outputs the number.
    if (n % 3 !=0 and n % 5 !=0):
        output = n
        
    #Checks if the number is a multiple of five, and if it is, there is an output of "Buzz"   
    if n%5 == 0:
        output += "Buzz"
    
    #Appends the data inserted into the empty string "output" into the dictionary "FizzBuzz"
    fizzbuzz.append(output)
    
#Displays the dictionary fizzbuzz after output is appended and prints the numbers
for n in fizzbuzz:
    print(n)

    
