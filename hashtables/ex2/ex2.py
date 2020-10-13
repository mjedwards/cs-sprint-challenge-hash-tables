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
    print(tickets)
    trip_dict = {}
    route = []
    for i in range(length):
        if tickets[i].source != tickets[i].destination:
            route.append(tickets[i].source)
    trip_dict[tickets[i]] = tickets[i]
    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")

tickets = [ticket_1, ticket_2]
reconstruct_trip(tickets, 2)