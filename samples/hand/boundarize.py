#!/usr/local/bin/python3
# Paul Evans (10evans@cua.edu)
# 5 February 2020
'''Roll up _dicta_ samples into 2500- to 3000-word chunks'''
import re
def main():
    recension = '1' # either '1' or '2'
    sequence = 1
    running_total = 0
    dicta = '' # accumulator
    toc_file = open(f'toc_{recension}r.txt', 'r')
    lines = toc_file.readlines()
    for line in lines:
        output_filename = f'./tmp/Gratian{recension}_' + str(sequence) + '.txt'
        input_filename = line.rstrip()
        input_file = open(f'./{recension}r/' + input_filename + '.txt', 'r')
        dictum = input_file.read()
        input_file.close()
        word_count = len(dictum.split())
        # findall returns same word count as split for all 1r and 2r samples
        # word_count = len(re.findall(r'\w+', dictum))
        if running_total <= 2500:
            running_total += word_count
            dicta += dictum
        else:
            output_file = open(output_filename, 'w')
            output_file.write(dicta)
            output_file.close()
            sequence += 1
            running_total = word_count
            dicta = dictum
    # output final incomplete sample
    output_file = open(output_filename, 'w')
    output_file.write(dicta)
    output_file.close()

if __name__ == '__main__':
    main()
