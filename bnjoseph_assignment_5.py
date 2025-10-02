#1
print("=== Challenge 1: Collatz Conjecture ===")
#get number input
current_number = int(input("Enter starting number: "))
#initialize step
step_count = 0
print("Sequence:", current_number, end=" ")
#loop for finding step count and printing the sequence
while current_number != 1:
    if current_number % 2 == 0:
        current_number /= 2
    else:
        current_number *= 3
        current_number += 1
    current_number = int(current_number)
    print(current_number, end=" ")
    step_count += 1
print()
print("Steps:", step_count)
print()

#2
print("=== Challenge 2: Prime Number Checker ===")
#get number
n = int(input("Enter a number: "))
print("Testing divisors from 2 to " + str(n-1) + "...")
#for else loop, if the number is not prime the for loop will break, if it is prime the for loop will complete and the else statement will return that the number is prime
for i in range(2, n):
    if n % i == 0:
        print(n, "is not prime (divisible by " + str(i) + ")")
        break
else:
    print(n, "is prime!")
print()