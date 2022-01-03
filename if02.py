def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """

    answer=''
    if a<b and a<c:
        answer=a
    elif b<a and b<c:
        answer=b
    elif c<a and c<b:
        answer=c 

    return answer
answer=main(3,4,5)
print(answer)