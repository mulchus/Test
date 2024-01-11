from collections import deque


graph = dict()
graph['you'] = ['alice',  'bob',  'carol', ]
graph['bob'] = ['zaram', 'peggy']


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                print(search_queue)
                print(searched)
                return True
            else:
                search_queue += graph[person] if graph.get(person) else ''
                searched.append(person)
    print("No a mango seller in this network!")
    print(search_queue)
    print(searched)
    return False


search("you")
