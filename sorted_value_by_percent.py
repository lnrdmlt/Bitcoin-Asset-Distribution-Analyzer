import csv

def sort():
    with open("data/addresses.csv", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return sorted(csv_reader, key=lambda row:int(row["value_satoshi"]) , reverse=True)   
    
def output(data):
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
    total = 0
    for row in sorted_data:
        total += 1
    return total

def get_num_wallets_by_percent(sorted_data, percent):
    total = get_total_num_wallets(sorted_data)
    return total * percent /100

def get_total_value_wallets_by_percent(sorted_data, start_percent, end_percent):
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
            
       
sorted_data = sort()   
print(get_total_value_wallets_by_percent(sorted_data,0,1))
print(get_total_value_wallets_by_percent(sorted_data,1,10))
