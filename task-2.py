import random

def get_numbers_ticket(min:int, max:int, quantity:int) -> list:
    if min < 1 or max > 1000 or quantity > (max - min + 1) or min > max:
        return []
    
    numbers = random.sample(range(min, max + 1), quantity)
    
    numbers.sort()
    
    return numbers


print(get_numbers_ticket(1, 49, 6))

# invalid input
print(get_numbers_ticket(49, 4, 2))
print(get_numbers_ticket(1, 4, 20))
print(get_numbers_ticket("1", "4", "20"))