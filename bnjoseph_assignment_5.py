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