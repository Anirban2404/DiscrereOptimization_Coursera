#!/usr/bin/python
# -*- coding: utf-8 -*-

import greedy_algo as greedy
import dynamic_prog as dp
import BranchnBound as bb
from collections import namedtuple
import timeit

Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    #output_data = greedy.greedyAlgo(items,capacity)
    # start = timeit.default_timer()
    if capacity <= 400000:
        #print "dp"
        output_data = dp.dynamicProg(items,capacity)
        return output_data
    # stop = timeit.default_timer()
    # print stop - start

    else:
        #print "bb"
        output_data = bb.branch_n_bound(items, capacity)
        return output_data


if __name__ == '__main__':
    import sys
    # if len(sys.argv) > 0:
    if len(sys.argv) > 1:
        # file_location = ".//data//ks_200_0"
        file_location =  sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

