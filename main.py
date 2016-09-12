from KnapsackLib import knapsack
from FileReadLib import get_data
# Implementation of dynamic programming algorithm for the Knapsack problem

filename = "knapsack1"
capacity, values, sizes = get_data("knapsack1")
# Determine maximum value in knapsack
max_val = knapsack(values, sizes, capacity)

print("Max value of knapsack: " + str(max_val))