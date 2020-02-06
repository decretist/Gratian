#!/usr/local/bin/python3
# Paul Evans (10evans@cua.edu)
# 5 February 2019
'''
Roll up _dicta_ samples into 2500- to 3000-word chunks
'''
import re
def main():
    print('Humanum genus duobus regitur')
    file_number = 1
    running = 0 # running count of words in sample
    sample = '' # sample accumulator
    toc_file = open('toc_2r.txt', 'r')
    lines = toc_file.readlines()
    for line in lines:
        input_filename = line.rstrip()
        input_file = open('./2r/' + input_filename + '.txt', 'r')
        string = input_file.read()
        input_file.close()
        word_count = len(string.split())
        # findall returns same word count as split for all 1r and 2r samples
        # word_count = len(re.findall(r'\w+', string))
        if running <= 2500:
            running += word_count
            sample += string
        else:
            output_filename = './tmp/Gratian2_' + str(file_number) + '.txt'
            output_file = open(output_filename, 'w')
            output_file.write(sample)
            output_file.close()
            file_number += 1
            running = 0
            sample = string
    # output incomplete sample
    output_filename = './tmp/Gratian2_' + str(file_number) + '.txt'
    output_file = open(output_filename, 'w')
    output_file.write(sample)
    output_file.close()

if __name__ == '__main__':
    main()
