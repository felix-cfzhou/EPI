Event = collections.namedtuple('Event', ('start', 'finish'))
Endpoint = collections.nametuple('Endpoint', ('time', 'is_start'))

def find_max_simutaneous_events(A):
    E = [Endpoint(event.start, True) for event in A] + [Endpoint(event.finish, False) for event in A]
    E.sort(key=lambda e: (e.time, not e.is_start))

    max_num_simultaneous_events = num_simultaneous_events = 0
    for e in E:
        if e.is_start:
            num_simultaneous_events += 1
            max_num_simultaneous_events = max(max_num_simultaneous_events, num_simultaneous_events)
        else:
            num_simultaneous_events -= 1
    return max_num_simultaneous_events
