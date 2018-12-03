import sys
import distance # pip install Distance 

def calculate_checksum(input_file):
    two_count = 0
    three_count = 0
    box_candidates = []
    lines = [line.rstrip('\n') for line in open(input_file)]

    for line in lines:
        char_count = {}

        for char in line:
            char_count[char] = char_count.get(char, 0) + 1


        already_collected = False

        for key,value in char_count.items():
            if(value == 3):
                three_count += 1
                box_candidates.append(line)
                already_collected = True
                break

                

        for key, value in char_count.items():
            if(value == 2):
                two_count += 1

                if(not already_collected):
                    box_candidates.append(line)
                break


    onedistance = []
    
    for i in range(len(box_candidates) - 2):
        j = i + 1
        while(j < len(box_candidates) - 1):
            j += 1
            d = distance.levenshtein(box_candidates[i], box_candidates[j])          
            if(d == 1):
                onedistance.append((box_candidates[i], box_candidates[j]))

    print("Solution part 1 =", two_count * three_count)
    print("Solution part 2 = ", onedistance)
    

if __name__ == "__main__":
    calculate_checksum(sys.argv[1])
