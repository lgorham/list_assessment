def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    """

    items.sort()
    print items
    top_items = items[-n:]
    print top_items

largest_n_items([2, 6006, 700, 42, 6, 59], 3)