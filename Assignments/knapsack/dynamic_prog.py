# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of certain capacity W
def dynamicProg(items, capacity):
    optimal_val = 0
    # Number of elements
    n = len(items)

    # Optimal path initialization
    taken = [0] * len(items)

    # Create an (N+1) by (W+1) 2-d list to contain the running values
    # which are to be filled by the dynamic programming routine.
    #
    # There are N+1 rows because we need to account for the possibility
    # of choosing from 0 up to and including N possible items.
    # There are W+1 columns because we need to account for possible
    # "running capacities" from 0 up to and including the maximum weight W.
    # print capacity
    K = [[0 for x in xrange(capacity + 1)] for x in xrange(n + 1)]
    # print len(K)
    #print K
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        # Increment i, because the first row (0) is the case where no items
        # are chosen, and is already initialized as 0
        for w in range(capacity + 1):
            # Base Case
            if i == 0 or w == 0:
                K[i][capacity] = 0
            elif items[i - 1].weight <= w:
                # Otherwise, we must choose between two possible candidate values:
                # 1) the value of "running capacity" as it stands with the last item
                #    that was computed; if this is larger, then we skip the current item
                # 2) the value of the current item plus the value of a previously computed
                #    set of items, constrained by the amount of capacity that would be left
                #    in the knapsack (running capacity - item's weight)
                candidate1 = items[i - 1].value + K[i - 1][w - items[i - 1].weight]
                candidate2 = K[i - 1][w]

                # Just take the maximum of the two candidates; by doing this, we are
                # in effect "setting in stone" the best value so far for a particular
                # prefix of the items, and for a particular "prefix" of knapsack capacities
                K[i][w] = max(candidate1, candidate2)

            else:
                K[i][w] = K[i - 1][w]
        optimal_val= K[i][w]

    # Reconstruction
    # Iterate through the values table, and check
    # to see which of the two candidates were chosen. We can do this by simply
    # checking if the value is the same as the value of the previous row. If so, then
    # we say that the item was not included in the knapsack (this is how we arbitrarily
    # break ties) and simply move the pointer to the previous row. Otherwise, we add
    # the item to the reconstruction list and subtract the item's weight from the
    # remaining capacity of the knapsack. Once we reach row 0, we're done

    # print taken
    while n > 0:
        # print K[n]
        # print K[n][capacity], K[n - 1][capacity]
        if K[n][capacity] != K[n - 1][capacity]:
            taken[n - 1] = 1
            capacity = capacity - items[n - 1].weight
        n = n - 1

        # Reverse the reconstruction list, so that it is presented
        # in the order that it was given
        # taken.reverse()
    #print taken
    #print K[n][capacity]

    # prepare the solution in the specified output format
    output_data = str(optimal_val) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

