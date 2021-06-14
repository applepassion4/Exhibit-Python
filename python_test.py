your_first_name = input("What is your name?")
neighbor_first_name = input("What's your neighbor's name?")

months_you_coded = input("How many months you have been coding?")
months_neighbor_coded = input("How many months your neighbor has been coding?")

total_months_coded = int(months_you_coded + int(months_neighbor))

print("I am" + your_first_name + and my neighbor is" + neighbor_first_name)
print("Together we have been coding for" + str(total_months_coded + "months!"))