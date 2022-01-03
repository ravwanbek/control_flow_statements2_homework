def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    answer=''

    
    
    

    if a>=b>=c or a<=b<=c:
        answer=b
    elif b>=a>=c or b<=a<=c:
        answer=a
    else:
        answer=c
    

    return answer
answer=main(1,2,3)
print(answer)