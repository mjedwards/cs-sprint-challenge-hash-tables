def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    num_dict = {}
    stored = []
    for i in a:
        num_dict[i] = i
       
        if i and -i in num_dict:
            item = abs(i)
            stored.append(item)   

    return stored


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
