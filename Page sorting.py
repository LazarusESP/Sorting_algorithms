from collections import OrderedDict
from collections import Counter
import random
import csv
def lru_page_sort(pages, capacity):
    cache = OrderedDict()
    hits = 0
    miss = 0

    for page in pages:
        if page not in cache:
            miss += 1
            if len(cache) == capacity:
                cache.popitem(last=False)
        else:
            hits += 1
            cache.move_to_end(page)
        cache[page] = None

    hit_rate = (hits / (hits + miss)) * 100
    return {'hit_rate' : hit_rate,'cache': list(cache.keys())}

def lfu_page_sort(pages, capacity):
    cache = {}
    frequency = Counter()
    hits = 0
    miss = 0

    for page in pages:
        if page not in cache:
            miss += 1
            if len(cache) == capacity:
                # usuwamy najrzadziej używany element
                least_frequent = min(cache, key=frequency.get)
                del cache[least_frequent]
                del frequency[least_frequent]
        else:
            hits += 1
        # dodajemy nowy element do pamięci i inkrementujemy jego częstotliwość
        cache[page] = None
        frequency[page] += 1

    hit_rate = (hits / (hits + miss)) * 100
    return {'hit_rate' : hit_rate,'cache': list(cache.keys())}

def generate_pages(page_amount, mean, std_dev, min_value=0, max_value=9, isRand = False):
    pages = []
    for i in range(page_amount):
        if isRand:
            rand_num = random.randint(min_value, max_value)
        else:
            rand_num = int(random.normalvariate(mean,std_dev))
            while not (min_value <= rand_num <= max_value):
                rand_num = int(random.normalvariate(mean, std_dev))
        pages.append(rand_num)
    return pages

page_amount = 10
page_mean = 10
page_std_dev = 5
min_value = 0
max_value = 9
isRand = True
pages = generate_pages(page_amount, page_mean, page_std_dev, min_value, max_value, isRand)
#pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 6]
capacity = 3

#LRU
for page in pages:
    print(page, end=' ')
print()
result_lru = lru_page_sort(pages, capacity)
print(f"Hit rate: {result_lru['hit_rate']:.2f}%") 
print(result_lru['cache'])
#LFU
result_lfu = lfu_page_sort(pages, capacity)
print(f"Hit rate: {result_lfu['hit_rate']:.2f}%") 
print(result_lfu['cache'])
#dzien doberek
str_lru_result = str(result_lru['hit_rate']) + '%'
str_lru_cache = str(result_lru['cache'])
str_lfu_result = str(result_lfu['hit_rate']) + '%'
str_lfu_cache = str(result_lfu['cache'])

with open(r'C:\Users\Piotr\Documents\data_page.csv', "a", newline = '') as csvfile:
    thewriter = csv.writer(csvfile)
    data = [page_amount,capacity, round(result_lru['hit_rate'],2), round(result_lfu['hit_rate'],2)]
    thewriter.writerow(data)