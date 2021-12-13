from copy import deepcopy

def add_connection(connections: dict, c1: str, c2: str) -> dict:
    if c1 not in connections:
        connections[c1] = [c2]
    else:
        if c2 not in connections[c1]:
            connections[c1].append(c2)
    if c2 not in connections:
        connections[c2] = [c1]
    else:
        if c1 not in connections[c2]:
            connections[c2].append(c1)
    return connections

def find_paths(connections: dict) -> int:
    paths = []
    for c in connections['start']:
        paths.append([c])
    #print(paths)
    i = 0
    finished = False
    while (i < len(paths)):
        x = 0
        while (i < len(paths) and paths[i][len(paths[i])-1] != 'end'):
            old_length = len(paths[i])
            #print(paths,i,len(paths[i])-1)
            next_caverns = connections[paths[i][len(paths[i])-1]]
            #print(f"Next caverns: {next_caverns}")
            # find next for current path
            create_new_path = False
            old_path = deepcopy(paths[i])
            for p in range(len(next_caverns)):
                #print(f"Placing {next_caverns[p]}")
                if next_caverns[p] == 'start':
                    continue
                if next_caverns[p].islower():
                    if next_caverns[p] in paths[i]:
                        continue
                    else:
                        if create_new_path is False:
                            create_new_path = True
                            #print(f"Appending {next_caverns[p]}")
                            paths[i].append(next_caverns[p])
                        else:
                            new_path = deepcopy(old_path)
                            new_path.append(next_caverns[p])
                            #print(f"Inserting {new_path}")
                            paths.insert(i+1,new_path)
                else:
                    if create_new_path is False:
                        create_new_path = True
                        #print(f"Appending: {next_caverns[p]}")
                        paths[i].append(next_caverns[p])
                    else:
                        new_path = deepcopy(old_path)
                        new_path.append(next_caverns[p])
                        #print(f"Inserting: {new_path}")
                        paths.insert(i+1,new_path)
            if len(paths[i]) == old_length:
                break
            else:
                old_length = len(paths[i])
            x += 1
        #print(paths)
        i += 1
    count = 0
    for p in paths:
        if p[len(p)-1] == 'end':
            count += 1
    return count

def find_dups(path: list) -> bool:
    fpath = []
    for x in path:
        if x.islower():
            fpath.append(x)
    #print(fpath)
    seen = []
    for el in fpath:
        if el in seen:
            return True
        else:
            seen.append(el)
    return False

def find_paths2(connections: dict) -> int:
    print(f"Connections: {connections}")
    paths = []
    for c in connections['start']:
        paths.append([c])
    #print(paths)
    i = 0
    finished = False
    while (i < len(paths)):
        x = 0
        while (i < len(paths) and paths[i][len(paths[i])-1] != 'end'):
            old_length = len(paths[i])
            #print(paths,i,len(paths[i])-1)
            #print(paths[i])
            next_caverns = connections[paths[i][len(paths[i])-1]]
            #print(f"Next caverns: {next_caverns}")
            # find next for current path
            create_new_path = False
            old_path = deepcopy(paths[i])
            dup_caverns = find_dups(old_path)
            for p in range(len(next_caverns)):
                #print(f"Placing {next_caverns[p]}")
                if next_caverns[p] == 'start':
                    continue
                if next_caverns[p].islower():
                    if next_caverns[p] in paths[i]:
                        if dup_caverns:
                            continue
                        else:
                            if create_new_path is False:
                                create_new_path = True
                                #print(f"Appending {next_caverns[p]}")
                                paths[i].append(next_caverns[p])
                            else:
                                new_path = deepcopy(old_path)
                                new_path.append(next_caverns[p])
                                #print(f"Inserting {new_path}")
                                paths.insert(i+1,new_path) 
                    else:
                        if create_new_path is False:
                            create_new_path = True
                            #print(f"Appending {next_caverns[p]}")
                            paths[i].append(next_caverns[p])
                        else:
                            new_path = deepcopy(old_path)
                            new_path.append(next_caverns[p])
                            #print(f"Inserting {new_path}")
                            paths.insert(i+1,new_path)
                else:
                    if create_new_path is False:
                        create_new_path = True
                        #print(f"Appending: {next_caverns[p]}")
                        paths[i].append(next_caverns[p])
                    else:
                        new_path = deepcopy(old_path)
                        new_path.append(next_caverns[p])
                        #print(f"Inserting: {new_path}")
                        paths.insert(i+1,new_path)
            if len(paths[i]) == old_length:
                break
            else:
                old_length = len(paths[i])
            x += 1
        #print(paths)
        i += 1
    #print(paths)
    count = 0
    for p in paths:
        if p[len(p)-1] == 'end':
            count += 1
    return count

if __name__ == "__main__":
    test = False
    if test:
        input_file = 'test_input.txt'
    else:
        input_file = 'input.txt'
    with open(input_file) as f:
        pairs = f.readlines()
    connections = {}
    for p in pairs:
        c1,c2 = p.rstrip().split('-')
        connections = add_connection(connections, c1, c2)

    #print(connections)
    path_count = find_paths(connections)
    print(f"Paths found: {path_count}")
    path_count2 = find_paths2(connections)
    print(f"Paths found for part2: {path_count2}")
