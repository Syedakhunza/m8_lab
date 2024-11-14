#syeda khunza fatima
#nov 14th,2024

#in this program it shows True if the year is a leap year, False if it is otherwise.

def is_leap_year(year):
    
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return True
    else:
        return False


print(is_leap_year(2024))  # Expected output: True
print(is_leap_year(1900))  # Expected output: False
print(is_leap_year(2000))  # Expected output: True
print(is_leap_year(2023))  # Expected output: False
