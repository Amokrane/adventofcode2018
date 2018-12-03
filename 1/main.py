import sys

def calculate_freq(input_file):
    freq = 0
    memo = {0 : 1}
    first_repeated_freq_found = False 
    
    lines = [line.rstrip('\n') for line in open(input_file)]

    while(not first_repeated_freq_found):
        for line in lines:
            freq += int(line)
            if(not first_repeated_freq_found and memo.get(freq, 0) == 1):
                first_repeated_freq_found = True
                print("First repeating freq = ", freq)
                break

            memo[freq] = memo.get(freq, 0) + 1

if __name__ == "__main__":
    calculate_freq(sys.argv[1])
