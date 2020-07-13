#!/usr/bin/env python

import argparse
import fitz
import os
import sys

from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg


def make_pdf(input_folder, output_path, fname, quiet):
    output = fitz.Document()
    non_svgs = []
    n = 0
    for file_path in os.listdir(input_folder):
        if file_path.lower().endswith('.svg'):
            n += 1
            im = svg2rlg(os.path.join(input_folder, file_path))
            b = renderPDF.drawToString(im)            # convert to pdf
            img_pdf = fitz.open('pdf', b)         # open as pdf
            output.insertPDF(img_pdf)
        else:
            non_svgs.append(file_path)

    if n:
        try:
            output.save(output_path)

            if not quiet:
                print("Successfully rendered " + str(n) + " SVGs to " + fname)
                if non_svgs:
                    print("Ignored " + str(len(non_svgs)) + " non-svg files:")
                    for line in non_svgs:
                        print('\t' + line)
        except:
            print('Error - something went wrong while saving the file', file=sys.stderr)
            return 1
    else:
        print('Error - no SVGs in input folder\n', file=sys.stderr)
        return 1

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', metavar='input', nargs='?', type=str,
                        default='.', help='Path to folder of SVGs - defaults to current folder')
    parser.add_argument('output', metavar='output', nargs='?', type=str,
                        default='out.pdf', help='Output filename - defaults to out.pdf')
    parser.add_argument('-f', '--force', dest='force',
                        action='store_true', help='Force overwrite output file')
    parser.add_argument('-q', '--quiet', dest='quiet',
                        action='store_true', help='Supress messages')

    # parser.add_argument('')

    args = parser.parse_args()

    in_path = os.path.join(os.getcwd(), args.folder)
    out_path = os.path.join(os.getcwd(), args.output)

    if not os.path.isdir(in_path):
        sys.exit('Error - no such directory \"' + args.folder + '\"')

    if os.path.isfile(out_path) and not args.force:
        sys.exit('Error - file \"' + args.output + '\" already exists!')
        

    if make_pdf(in_path, out_path, args.output, args.quiet):
        if not args.quiet:
            parser.print_help()
            sys.exit()
