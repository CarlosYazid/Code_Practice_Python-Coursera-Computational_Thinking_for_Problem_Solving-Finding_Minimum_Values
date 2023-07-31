#This is an algorithm to find the 2 smallest numbers in a list of n numbers

def enter_numbers():
     numbers = input("Enter a list of numbers separated by commas: ")
     numbers_list = [float(number) for number in numbers.replace(' ', '').split(',')]
     return numbers_list

while True:
     numbers = enter_numbers()

     while len(numbers) < 2:
         print("Please enter at least two numbers.")
         numbers = enter_numbers()

     arranged_numbers = sorted(numbers)
     min1, min2 = arranged_numbers[:2]

     print("The two smallest numbers in ascending order are:", min1, " and ", min2)

     response = input("Do you want to continue? (Yes or No): ").lower()

     while response not in("yes", "no"):
         print("Please type 'Yes' or 'No':")
         response = input().lower()

     if response == "no":
         break