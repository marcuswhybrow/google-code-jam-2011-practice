"""
Problem C. T9 Spelling
======================

Marcus Whybrow's "Google Code Jam Practice 2010" sollutions
http://code.google.com/codejam/contest/dashboard?c=351101#s=p2

Problem
-------

The Latin alphabet contains 26 characters and telephones only have ten digits 
on the keypad. We would like to make it easier to write a message to your 
friend using a sequence of keypresses to indicate the desired characters. The 
letters are mapped onto the digits as shown below. To insert the character B 
for instance, the program would press 22. In order to insert two characters in
sequence from the same key, the user must pause before pressing the key a 
second time. The space character ' ' should be printed to indicate a pause. 
For example, 2 2 indicates AA whereas 22 indicates B.

Input
-----

The first line of input gives the number of cases, N. N test cases follow. 
Each case is a line of text formatted as

    desired_message
    
Each message will consist of only lowercase characters a-z and space 
characters ' '. Pressing zero emits a space.

Output
------

For each test case, output one line containing "Case #x: " followed by the 
message translated into the sequence of keypresses.

Limits
------

1 <= N <= 100.

Small dataset

1 <= length of message in characters <= 15.

Large dataset

1 <= length of message in characters <= 1000.
"""

import string

INPUT_FILE = 'C-large-practice.in'
OUTPUT_FILE = 'C-large-practice.txt'

KEYPAD_KEY_SIZES = (0,3,3,3,3,3,4,3,4)

def get_accum_keypad():
    """Create an accumulative version of the keypad key sizes tuple"""
    accum_keypad = []
    total = 0
    for size in KEYPAD_KEY_SIZES:
        total += size
        accum_keypad.append(total)
    return accum_keypad

def get_keypad_letters():
    """
    Retruns a dictionary mapping of lowercase letters (a-z) and the space
    character, to the keypad buttons which must be pressed.
    """
    accum_keypad = get_accum_keypad()
    keypad_letters = {' ': (0, 1)}
    
    letterIndex = 0
    prev_accum = 0
    for letter in string.lowercase:
        for i in range(len(accum_keypad)):
            if letterIndex < accum_keypad[i]:
                key_number = i + 1
                repeat = letterIndex + 1 - prev_accum
                keypad_letters[letter] = (key_number, repeat)
                break
            prev_accum = accum_keypad[i]
        letterIndex += 1
        
    return keypad_letters

def read_input():
    """Get the numbers from the input file"""
    f = open(INPUT_FILE, 'r')
    number_of_lines = int(f.readline())
    
    inputs = []
    for i in range(number_of_lines):
        yield [i+1, f.readline().rstrip('\n')]
    f.close()

def convert(s):
    keypad_letters = get_keypad_letters()
    code = ''
    
    prev_key_number = None
    for c in s:
        key_number, repeat = keypad_letters[c]
        if prev_key_number == key_number:
            code += ' '
        code += str(key_number) * repeat
        prev_key_number = key_number
    return code

def get_output():
    """Calculate the ouput"""
    for case_index, s in read_input():
        yield [case_index, convert(s)]

def write_output():
    """Write the output to file"""
    f = open(OUTPUT_FILE, 'w')
    for case_index, code in get_output():
        f.write('Case #%d: %s\n' % (case_index, code))
    f.close()

if __name__ == '__main__':
    write_output()