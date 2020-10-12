def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_dict = {}
    for i in range(length):
        item = limit - weights[i]
        if weight_dict.get(item):
            return (i, weights.index(item))

        weight_dict[weights[i]] = weights[i]
        
    return None


print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 16))