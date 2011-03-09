INPUT_FILE = 'A-small-practice.in'
OUTPUT_FILE = 'A-small-practice.txt'

def find(credit, number_of_items, item_prices):
    """Returns two items from item_prices which add up exactly to credit"""
    for i in range(number_of_items):
        for j in range(i+1, number_of_items):
            if item_prices[i] + item_prices[j] == credit:
                return i+1, j+1
    return None, None

def read_input():
    fIn = open(INPUT_FILE, 'r')
    number_of_cases = int(fIn.readline())
    
    inputs = []
    for i in range(number_of_cases):
        credit = int(fIn.readline())
        number_of_items = int(fIn.readline())
        item_prices = [int(ip) for ip in fIn.readline().split()]
        inputs.append([i, credit, number_of_items, item_prices])
    fIn.close()
        
    return inputs

def get_output(inputs):
    outputs = []
    for i, credit, number_of_items, item_prices in inputs:
        index1, index2 = find(credit, number_of_items, item_prices)
        outputs.append('Case #%d: %d %d\n' % (i+1, index1, index2))
    
    return outputs

def write_output(outputs):
    fOut = open(OUTPUT_FILE, 'w')
    for line in outputs:
        fOut.write(line)
    fOut.close()

def main():
    inputs = read_input()
    outputs = get_output(inputs)
    write_output(outputs)
    
if __name__ == "__main__":
    main()