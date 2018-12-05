import sys
import re
import functools
from stack import Stack


def count_polymer_unit_size(input_file):

    shortest_polymer_length_1 = apply_reduction(input_file, '')
    print(shortest_polymer_length_1)

    shortest_polymer_length_2 = shortest_polymer_length_1

    for one in range(97,123):
        polymer_length = apply_reduction(input_file, chr(one))
        if(polymer_length < shortest_polymer_length_2):
            shortest_polymer_length_2 = polymer_length
            
    print(shortest_polymer_length_2)


def apply_reduction(input_file, unit):

    stack = Stack()
    with open(input_file) as f:
        f_read_ch = functools.partial(f.read, 1)
        for ch in iter(f_read_ch, ''):
            if(ch.lower() == unit.lower()):
                continue

            if(not stack.isEmpty() and check_polarization(ch, stack.peek())):
                stack.pop()
                continue
            stack.push(ch)

    return stack.size() - 1


def check_polarization(s1, s2):

    if((s1.lower() == s2.lower()) and ((s1.islower() and s2.isupper()) or (s1.isupper() and s2.islower()))):
        return True

    return False

if __name__ == "__main__":
    count_polymer_unit_size(sys.argv[1])

