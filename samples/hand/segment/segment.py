#!/usr/local/bin/python3
# Paul Evans (10evans@cua.edu)
# 5-9 February 2020
'''Roll up dicta samples into 2500-word segments'''
import argparse
import re
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('recension', type=str, help="'1' or '2'")
    parser.add_argument('-a', '--all', action='store_true')
    parser.add_argument('-p', '--dePen', action='store_true')
    args = parser.parse_args()
    recension = args.recension
    if args.all:
        output_all = True
        corpus = 'corpus3'
        output_de_Pen = False
    else:
        output_all = False
        corpus = 'corpus6'
        if args.dePen: output_de_Pen = True
        else: output_de_Pen = False
    if output_de_Pen: output_file_basename = f'./{corpus}/dePen{recension}_'
    else: output_file_basename = f'./{corpus}/Gratian{recension}_'
    sequence = 1
    running_total = 0
    output_string = ''
    table_of_contents_file = open(f'toc_{recension}r.txt', 'r')
    lines = table_of_contents_file.readlines()
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
        input_string = input_file.read()
        input_file.close()
        word_count = len(input_string.split())
        # findall returns same word count as split for all 1r and 2r dicta
        # word_count = len(re.findall(r'\w+', input_string))
        if running_total <= 2500:
            running_total += word_count
            output_string += input_string
        else:
            output_file = open(output_filename, 'w')
            output_file.write(output_string)
            output_file.close()
            sequence += 1
            running_total = word_count
            output_string = input_string
    # output final incomplete file
    output_file = open(output_filename, 'w')
    output_file.write(output_string)
    output_file.close()

if __name__ == '__main__':
    main()
