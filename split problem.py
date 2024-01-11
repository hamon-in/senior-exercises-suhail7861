import random

def split(items, ratios):
    total_ratio = sum(ratios)
    
    counts = [round(len(items) * ratio / total_ratio) for ratio in ratios]

    result = []
    start = 0
    for count in counts:
        end = start + count
        result.append(random.sample(items, count))
        start = end

    return result

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ratios = [0.5, 0.4, 0.1]

result = split(items, ratios)
print(result)
