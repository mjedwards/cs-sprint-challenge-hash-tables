def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    num_dict = {}
    stored = []
    value = []
    for i in range(len(a)):
        if a[i] < 0:
            stored.append(abs(a[i]))
            
            for j in range(len(stored)):
                if stored[j] in a[j]:
                    value.append(stored[j])

                    result = value
            

        num_dict[a[i]] = a[i]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
