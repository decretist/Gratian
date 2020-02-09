#!/usr/local/bin/python3
# Paul Evans (10evans@cua.edu)
# 5 February 2020
'''Roll up _dicta_ samples into 2500- to 3000-word chunks'''
import re
def main():
    recension = '2' # either '1' or '2'
    output_all = False # True equivalent to corpus3, False equivalent to corpus6
    output_de_Pen = False
    if output_de_Pen: output_file_basename = f'./tmp/dePen{recension}_'
    else: output_file_basename = f'./tmp/Gratian{recension}_'
    sequence = 1
    running_total = 0
    dicta = '' # accumulator
    toc_file = open(f'toc_{recension}r.txt', 'r')
    lines = toc_file.readlines()
    for line in lines:
        input_filename = line.rstrip()
        if not output_all:
            match = re.match(r'^de Pen. D.\d d.[ap].c.\d{1,2}$', input_filename)
            if output_de_Pen:
                if not match: continue
            else:
                if match: continue
        output_filename = output_file_basename + str(sequence) + '.txt'
        input_file = open(f'./{recension}r/' + input_filename + '.txt', 'r')
        dictum = input_file.read()
        input_file.close()
        word_count = len(dictum.split())
        # findall returns same word count as split for all 1r and 2r dicta
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
    # output final incomplete file
    output_file = open(output_filename, 'w')
    output_file.write(dicta)
    output_file.close()

if __name__ == '__main__':
    main()
