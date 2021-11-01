from collections import defaultdict, OrderedDict, namedtuple, deque


def task1() -> defaultdict:

    ok = defaultdict(lambda: 'unknown')
    ok['Alan'] = 'Manchester'
    return ok



def task2(arg_od: OrderedDict):
    arg_od.popitem()
    arg_od.popitem(False)
    # remember to remove start and end before moving Bob and Dan, otherwise they will be removed instead
    arg_od.move_to_end('Bob')
    arg_od.move_to_end('Dan', False)



def task3(name: str, club: str) -> namedtuple:


    player = namedtuple('Player', ['name', 'club'])
    player = player('name, club')
    return player


def task4(arg_deque: deque):
    """
    - Manipulate the `arg_deque` in any order you preferred to achieve the following effect:
        -- remove last element in `deque`
        -- move the fist (left most) element to the end (right most)
        -- add an element `Zack`, a string, to the start (left)
    """
    arg_deque.pop()
    arg_deque.append(arg_deque.popleft())
    arg_deque.appendleft('Zack')
