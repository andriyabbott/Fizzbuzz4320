#Getting Fizzbuzz to be more efficient

#creating a list- avoids concatenation of large strings
fizzbuzz=[]
#Initializing range as a seperate variable
fizzbuzzRange = range(101)

#Fizzbuzz loop with the above range
for n in fizzbuzzRange:
    
    output =''
    
    if n%3 ==0:
        output += "Fizz"
    if (n % 3 !=0 and n % 5 !=0):
        output = n
    if n%5 == 0:
        output += "Buzz"

    fizzbuzz.append(output)

for n in fizzbuzz:
    print(n)

    
