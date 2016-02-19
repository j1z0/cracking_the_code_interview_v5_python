
#lets make our graph a dictionary of nodes -> adjacent nodes

graph = {'a': ['b','c','d'],
       'b' : ['a','c'],
       'c' : ['a','b'],
       'd' : ['e'],
       'e' : ['d'],
      }

def find_route(start, end, path=[]):
    #be careful here, we need to create a new list
    path = path + [start]

    if start == end:
        return path

    if not graph.has_key(start):
        return None

    for node in graph[start]:
        if node not in path:
            newpath = find_route(node, end, path)
            if newpath: return newpath
   
    return None

def find_route_iterative(start, end):
    '''depth first search'''
    
    if start == end:
        return [start]
    stack = [start]
    visited =[start]

    while stack:
        node = stack.pop()
        if node == end:
            return visited + [node]
        for n in graph.get(node):
            if n not in visited:
                visited.append(n)
                if n == end:
                    return visited
                else:
                    new_nodes = [g for g in graph.get(n) if g not in visited]
                    stack.extend(new_nodes)

    return None


def find_route_iterative(start, end):
    '''depth first search'''
    
    if start == end:
        return [start]
    stack = [start]
    visited =[start]

    while stack:
        node = stack.pop()
        if node == end:
            return visited + [node]
        for n in graph.get(node):
            if n not in visited:
                visited.append(n)
                if n == end:
                    return visited
                else:
                    new_nodes = [g for g in graph.get(n) if g not in visited]
                    stack.extend(new_nodes)

    return None


def find_all_paths(start, end, path=[]):
    #be careful here, we need to create a new list
    path = path + [start]

    if start == end:
        return [path]

    if not graph.has_key(start):
        return [] 

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
   
    return paths 

if __name__ == "__main__":

    print find_route_iterative('a','a')
    print find_route_iterative('a','b')
    print find_route_iterative('a','e')

    print("recursive find_route")
    print find_route('a','a')
    print find_route('a','b')
    print find_route('a','e')
    assert not find_route('x','z')
    assert not find_route('e','a')

    print ("all paths")
    print find_all_paths('a','a')
    print find_all_paths('a','b')
    print find_all_paths('a','e')
