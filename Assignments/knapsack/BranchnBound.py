import Queue


# A Branch and Bound based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of certain capacity
class Node:
    def __init__(self, level, value, weight, contains):
        self.level = level
        self.value = value
        self.weight = weight
        self.contains = contains


def upper_bound(node, capacity, n, val, wt):
    # print capacity
    # print val
    # print wt
    # if weight overcomes the knapsack capacity, return
    # 0 as expected bound
    if node.weight >= capacity:
        return 0

    else:
        # initialize bound on profit by current profit
        bound = node.value
        # print "bound1:", bound

        # start including items from index 1 more to current item
        # index
        totalWeight = node.weight
        # print "w:", totalWeight

        j = node.level + 1
        # print "j", j

        # checking  index condition and knapsack capacity condition
        while j < n and totalWeight + wt[j] <= capacity:
            bound = bound + val[j]
            totalWeight = totalWeight + wt[j]
            j = j + 1
        # fill knapsack with fraction of a remaining item
        #  If k is not n, include last item partially
        #  for upper bound on profit
        if j < n:
            bound = bound + (capacity - totalWeight) * (val[j] / wt[j])
    # print "bound:", bound
    return bound


# Returns maximum profit we can get with capacity W
def branch_n_bound(items, capacity):
    item_count = len(items)
    v = [0] * item_count
    w = [0] * item_count
    # print items
    # sort items by value to weight ratio
    items = sorted(items, key=lambda k: float(k.value) / k.weight, reverse=True)
    # print items

    # make a queue for traversing the node
    queue = Queue.Queue()
    root = Node(-1, 0, 0, [])
    queue.put(root)

    for i, item in enumerate(items, 0):
        v[i] = int(item.value)
        w[i] = int(item.weight)


    bound = upper_bound(root, capacity, item_count, v, w)
    # print bound

    # One by one extract an item from decision tree
    # compute profit of all children of extracted item
    # and keep saving maxProfit
    value = 0
    taken = [0] * item_count

    best = set()

    while not queue.empty():
        c = queue.get()  # Get the next item on the queue

        # If it is starting node, assign level 0
        if c.level == -1:
            ulevel = 0

        # If there is nothing on next level
        if c.level == item_count - 1:
            continue
        # Else if not last node, then increment level,
        # and compute profit of children nodes.
        ulevel = c.level + 1

        # Taking current level's item add current
        # level's weight and value to node u's
        # weight and value

        # check 'left' node (if item is added to knapsack)
        # print "**", ulevel, c.value + v[ulevel], c.weight + w[ulevel], c.contains[:]
        left = Node(ulevel, c.value + v[ulevel], c.weight + w[ulevel], c.contains[:])
        left.bound = upper_bound(left, capacity, item_count, v, w)
        left.contains.append(ulevel)

        # If cumulated weight is less thanW and
        # value is greater than previous value,
        # update value
        if left.weight <= capacity and left.value > value:
            value = left.value
            best = set(left.contains)
        # If bound  value is greater than profit,
        # then only push into queue for further consideration
        if bound > value:
            queue.put(left)

        # check 'right' node (if items is not added to knapsack)
        right = Node(ulevel, c.value, c.weight, c.contains[:])
        bound = upper_bound(right, capacity, item_count, v, w)
        if bound > value:
            value = right.value
            best = set(right.contains)
            queue.put(right)

    for b in best:
        taken[b] = 1
    value = sum([i * j for (i, j) in zip(v, taken)])

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))

    return output_data
