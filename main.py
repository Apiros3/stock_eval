import stock_value 
import individual_value

if __name__ == '__main__':
    
    stock_value.get_vals()

    # idv_f = open('watchlist.txt', 'r')
    individual_code = open('watchlist.txt').readlines()

    for line in individual_code :
        # print(f"\"{line.strip()}\"")
        individual_value.get_vals(line.strip())


# lines = map(str.split, open('testFile.txt'))