from typing import List

def groupThePeople(groupSizes: List[int]) -> List[List[int]]:
    groups = []
    map = {}
    # for each person on groupSizes
    # if groupSize on map, add person to map array
    # if the len of the array is equal to key add key to groups
    # empty the key
    # else create a new key and initialze with the person
    for i, p in enumerate(groupSizes):
        if p in map:
            map[p].append(i)
        else:
            map[p] = [i]
        if len(map[p]) == p:
            groups.append(map[p])
            map[p] = []
    return groups

if __name__ == "__main__":
    cases = [
        [[3,3,3,3,3,1,3],[[5],[0,1,2],[3,4,6]]],
        [[2,1,3,3,3,2], [[1],[0,5],[2,3,4]]]
    ]
    for case in cases:
        for g in groupThePeople(case[0]):
            if g not in case[1]:
                print('group {} not in list {} '.format(g,case[1]))
                break
        print("passed")
