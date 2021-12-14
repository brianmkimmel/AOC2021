def pair_insertion(template, pairs):
    i = 1
    while (i != len(template)):
        pair = ''.join([template[i-1],template[i]])
        for rule in pairs:
            if rule[0] == pair:
                element = rule[1]
                break
        else:
            raise Exception
        template.insert(i,element)
        i += 2
    return template

def efficient_pair_insertion(polymer, pairs):
    new_polymer = {}
    for pair in polymer:
        for rule in pairs:
            if rule[0] == pair:
                element = rule[1]
                break
        pair1 = pair[0] + element
        pair2 = element + pair[1]
        if pair1 in new_polymer:
            new_polymer[pair1] += polymer[pair]
        else:
            new_polymer[pair1] = polymer[pair]
        if pair2 in new_polymer:
            new_polymer[pair2] += polymer[pair]
        else:
            new_polymer[pair2] = polymer[pair]
    return new_polymer

if __name__ == "__main__":
    test = False
    inefficient = False
    if test:
        input_file = 'test_input.txt'
    else:
        input_file = 'input.txt'
    with open(input_file) as f:
      template = list(f.readline().strip())
      f.readline()
      pairs = [x.split('->') for x in [x.replace(' ','') for x in [x.strip() for x in f.readlines()]]]

    #print(template,pairs)
    polymer = {}
    for x in range(len(template)-1):
        polymer[''.join([template[x],template[x+1]])] = 1
    print(polymer)
    for x in range(40):
        #template = pair_insertion(template, pairs)
        polymer = efficient_pair_insertion(polymer, pairs)
    #print(template)
    if inefficient:
        element_count = {}
        # count elements:
        for el in template:
            if el in element_count:
                element_count[el] += 1
            else:
                element_count[el] = 1
        print(element_count)
    element_count2 = {}
    for pair in polymer:
        for c in pair:
            if c in element_count2:
                element_count2[c] += polymer[pair]
            else:
                element_count2[c] = polymer[pair]
    #print(polymer,element_count2)
    min = 100000000000000000000000
    max = 0
    for el in element_count2:
        if element_count2[el] < min:
            min = element_count2[el]
        if element_count2[el] > max:
            max = element_count2[el]
    print(f"Max: {max}, Min: {min} Answer: {(max+1)/2 - min/2}")