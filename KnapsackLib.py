import numpy as np

def knapsack(vals, sizes, capacity):
    # returns the maximal value of knapsack with given capacity for items of given value and size

    # Determine number of items
    n_items = len(vals)

    # Initialize array to hold maximal value for subproblems with any prefix-subset of the items,
    # and any capacity up to the full capacity.
    a = np.zeros((n_items+1, capacity+1),dtype=int)

    for a_items in range(1,n_items+1):
        i_new_item = a_items - 1
        for cap in range(1,capacity+1):  # when capacity is zero, maximal value is also zero

            val_if_new_item_not_used = a[a_items-1, cap]

            if sizes[i_new_item]<cap:
                val_if_new_item_used = vals[i_new_item] + a[a_items-1, cap-sizes[i_new_item]]
            else:
                val_if_new_item_used = 0

            a[a_items, cap] = max(val_if_new_item_not_used,
                                              val_if_new_item_used)


    return a[n_items, capacity]
