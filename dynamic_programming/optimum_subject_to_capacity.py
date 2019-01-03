Item = collections.namedtuple('Item', ('weight', 'value'))

def optimum_subject_to_capacity(items, capacity):
    def optimum_subject_to_item_and_capacity(k, available_capacity):
        if k < 0:
            return 0
        elif V[k][available_capacity] == -1:
            without_curr_item = optimum_subject_to_item_and_capacity(k-1, available_capacity)
            with_curr_item = 0 if available_capacity < items[k].weight else (
                items[k].value + optimum_subject_to_item_and_capacity(k-1, available_capacity - items[k].weight))
            V[k][available_capacity] = max(without_curr_item, with_curr_item)
        return V[k][available_capacity]

    V = [[-1]*(capacity+1) for _ in items]
    return optimum_subject_to_item_and_capacity(len(items)-1, capacity)
