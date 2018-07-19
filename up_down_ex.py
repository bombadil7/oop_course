def main():
    salary = calculate_salary()
    print(salary)

    
def calculate_salary():
    """
    Calculate the officer's salary using keyboard input.

    :returns: officer's salary
    """
    sum_of_fines = 0
    speed_of_auto, number_of_auto = read_data()
    while not detect_chief(number_of_auto):
        if int(speed_of_auto) > 60:
            sum_of_fines += calculate_fine(number_of_auto)
        speed_of_auto, number_of_auto = read_data()
    return sum_of_fines


def read_data():
    """
    Reads next line of user input.
    
    :returns: tuple(int, str) - speed, license plate number
    """
    data = input().split()
    return data


def detect_chief(number_of_auto):
    """
    Checks whether this car belongs to the super.
    
    :param number_of_auto: license plate number 
    :returns: True if this is the chief, else False
    """
    return number_of_auto == "A999AA"


def calculate_fine(number_of_auto):
    """
    Calculates the amount of fine based on the license plate
    
    :param number_of_auto: license plate 
    :returns: Fine amount 
    """
    if is_super_number(number_of_auto):
        return 1000
    elif is_good_number(number_of_auto):
        return 500
    else:
        return 100


def is_super_number(number_of_auto):
    """
    Checks if the number is "cool" (three digits match)
    
    :param number_of_auto: license plate 
    :returns: True, if "cool", else False
    """
    return number_of_auto[1] == number_of_auto[2] == number_of_auto[3]


def is_good_number(number_of_auto):
    """
    Checks if number is "good" (two digits match)
    
    :param number_of_auto: license plate 
    :returns: True, if two digits match, else False
    """
    return number_of_auto[1] == number_of_auto[2] or \
           number_of_auto[1] == number_of_auto[3] or \
           number_of_auto[2] == number_of_auto[3]


if __name__ == "__main__":
    main()
