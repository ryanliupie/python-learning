import heapq

def topKFrequent(nums, k):
    hashmap = dict()
    for num in nums: 
        hashmap[num] = hashmap.get(num, 0) + 1 

    heap = []

    for key, value in hashmap.items():
        if len(heap) < k or value > heap [0][0]: 
            heapq.heappush(heap, [value, key])
        if len(heap) > k: 
            heapq.heappop(heap)
    
    result = []
    for pair in heap: 
        result.append(pair[1])
    
    return result 

print(topKFrequent([1,1,2,2,2,3,3,3,3], 2))