import csv
import os

cache_file = 'data/cache.csv'

def sort():
    print("sorting...")
    with open("data/addresses.csv", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return sorted(csv_reader, key=lambda row:int(row["value_satoshi"]) , reverse=True)   

def create_cache(sorted_data):
    
    os.remove(cache_file)
    with open(cache_file, 'w', newline='') as csv_file:
        cache_writer = csv.writer(csv_file)
        line_count = 0
        for row in sorted_data:
            if line_count == 0:
                cache_writer.writerow(["address", "value_satoshi", "last_height"])
            else:
                cache_writer.writerow([row["address"],row["value_satoshi"],row["last_height"]])
                
            line_count += 1
def get_cache():
    print("getting from cache...")
    with open("data/cache.csv", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return csv_reader
    
def get_data():
    if os.path.isfile(cache_file):
        return get_cache()
    sorted_data = sort()
    create_cache(sorted_data)
    return sorted_data
        
            
def output(data):
    print("outputting...")
    line_count = 0
    for row in data:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(
            f'\tThis address({row["address"]}) has {row["value_satoshi"]} satoshi, at block {row["last_height"]}.'
            )
            line_count += 1
            print(f"Processed {line_count} lines.")

def get_total_num_wallets(sorted_data):
    print("getting total number of wallets...")
    total = 0
    for row in sorted_data:
        total += 1
    return total

def get_num_wallets_by_percent(sorted_data, percent):
    print("getting the number of wallets by percent...")
    total = get_total_num_wallets(sorted_data)
    return total * percent /100

def get_total_value_wallets_by_percent(sorted_data, start_percent, end_percent):
    print("getting total value of wallets by percent...")
    total = 0
    count = 0
    start_count = get_num_wallets_by_percent(sorted_data, start_percent)
    end_count = get_num_wallets_by_percent(sorted_data, end_percent)
    for row in sorted_data:
        count += 1
        if count <= start_count:
            continue
        if count > end_count:
            break
        total += int(row["value_satoshi"])
    return total

 
sorted_data = get_data()
print(get_total_value_wallets_by_percent(sorted_data,0,1))
print(get_total_value_wallets_by_percent(sorted_data,1,10))
