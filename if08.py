def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    answer=''
    if number==1:
        answer='Monday'
    elif number==2:
        answer='Tuesday'
    elif number==3:
        answer='Wednesday'    
    elif number==4:
        answer='Thursday'
    elif number==5:
        answer='Friday'
    elif number==6:
        answer='Saturday'
    elif number==7:
        answer='Sunday'
    return answer
print(main(4))
