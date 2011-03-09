"""
Problem B. Reverse Words
========================

Marcus Whybrow's "Google Code Jam Practice 2010" sollutions
http://code.google.com/codejam/contest/dashboard?c=351101#s=p1

Problem
-------

Given a list of space separated words, reverse the order of the words. Each 
line of text contains L letters and W words. A line will only consist of 
letters and space characters. There will be exactly one space character 
between each pair of consecutive words.

Input
-----

The first line of input gives the number of cases, N.
N test cases follow. For each test case there will a line of letters and space
characters indicating a list of space separated words. Spaces will not appear 
at the start or end of a line.

Output
------

For each test case, output one line containing "Case #x: " followed by the 
list of words in reverse order.
"""

INPUT_FILE = 'B-large-practice.in'
OUTPUT_FILE = 'B-large-practice.txt'

def read_input():
    """Get the numbers from the input file"""
    f = open(INPUT_FILE, 'r')
    
    number_of_lines = int(f.readline())
    for i in range(number_of_lines):
        yield [i+1, f.readline().split()]
    f.close()

def get_output():
    """Calculate the ouput"""
    for case_index, words in read_input():
        words.reverse()
        yield [case_index, words]

def write_output():
    """Write the output to file"""
    f = open(OUTPUT_FILE, 'w')
    for case_index, words in get_output():
        f.write('Case #%d: %s\n' % (case_index, ' '.join(words)))
    f.close()

if __name__ == '__main__':
    """
    This sollutions uses yields, which means less memory usage, but does keep 
    a lock on the input and output files for the duration of the programs 
    execution.
    """
    write_output()