import sys
import re

def calculate_shared_surface(input_file):

    lines = [line.rstrip('\n') for line in open(input_file)]
    w, h = 1000, 1000
    rectangle = [["." for x in range(w)] for y in range(h)]
    regex = "#(\d+)\s@\s(\d+)\,(\d+)\:\s(\d+)x(\d+)"
    total_surface = 0
    no_overlap_claim = 0
    
    no_overlap_claims = []

    for line in lines:
        m = re.match(regex, line)
        claim_id = m.group(1)
        left_padding = int(m.group(2))
        top_padding = int(m.group(3))
        width = int(m.group(4))
        height = int(m.group(5))

        has_overlap = False


        for i in range(height):
            for j in range(width):
                value = rectangle[i + top_padding + 1][j + left_padding + 1]


                if(value == "."):
                    rectangle[i + top_padding + 1][j + left_padding + 1] = claim_id

                elif(value != "."):
                    has_overlap = True
                    total_surface += 1
                    rectangle[i + top_padding + 1][j + left_padding + 1] = value + "," + claim_id
                    
                    for claim in no_overlap_claims:
                        if(check_included(claim, value + "," + claim_id)):
                            no_overlap_claims.remove(claim)

        if(not has_overlap):
            no_overlap_claims.append(claim_id)

    print(total_surface, no_overlap_claims)

def check_included(value, l):
    if value in l.split(","):
        return True
    return False

if __name__ == "__main__":
    calculate_shared_surface(sys.argv[1])

