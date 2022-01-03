def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
    """
    answer=''
    if temp<0:
        answer='Freezing'
    elif 0<temp<11:
        answer='Very Cold'
    elif 10<temp<21:
        answer='Cold'
    elif 20<temp<31:
        answer='Normal'
    elif 30<temp<41:
        answer='Hot'
    elif temp>40:
        answer='Very Hot'
    return answer
print(main(40))
