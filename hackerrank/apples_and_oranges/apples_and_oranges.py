def countApplesAndOranges(s, t, a, b, apples, oranges):
    house_range = set(range(s, t + 1))
    apple_location = a
    orange_location = b
    adjusted_apples = list(map(lambda x: apple_location + x, apples))
    adjusted_oranges = list(map(lambda x: orange_location + x, oranges))
    hit_apples = len(list(filter(lambda x: x in house_range, adjusted_apples)))
    hit_oranges = len(list(filter(lambda x: x in house_range, adjusted_oranges)))
    print(str(hit_apples))
    print(str(hit_oranges))
    #return hit_apples, hit_oranges


result = countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4])
print(result)


result = countApplesAndOranges(7,11,5,15,[-2,2,1], [5,-6])
print(result)
