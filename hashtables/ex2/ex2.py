#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here     
    trip_dict = {}
    route = []
    for ticket in tickets:
        departure, arrival = ticket.source, ticket.destination
        if departure not in trip_dict:
            trip_dict[departure] = arrival

    search = "NONE"
    next_destination = trip_dict[search]

    while next_destination is not "NONE":
        next_destination = trip_dict[search]
        route.append(next_destination)
        search = next_destination
        
    return route