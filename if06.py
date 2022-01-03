def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """

    n1=n//10000
    n2=(n//1000-n1*10)
    n3=n//100-(n2*10)-n1*100
    n5=n%10
    n4=int((n%100-n5)/10)

        
    if n1>n2 and n1>n3 and n1>n4 and n1>n5:
        index=n1
    elif n2>n1 and n2>n3 and n2>n4 and n2>n5:
        index=n2
    elif n3>n1 and n3>n2 and n3>n4 and n3>n5:
        index=n3
    elif n4>n1 and n4>n2 and n4>n3 and n4>n5:
        index=n4
    elif n5>n1 and n5>n2 and n5>n3 and n5>n4:
        index=n5

    if index==n1:
        answer=5
    elif index==n2:
        answer=4
    elif index==n3:
        answer=3
    elif index==n4:
        answer=2
    elif index==n5:
        answer=1    
    



    return answer
print(main(28123))