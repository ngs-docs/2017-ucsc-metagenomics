#! /usr/bin/env python2
import screed
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('listfile')
    parser.add_argument('ffn_file')
    parser.add_argument('outfile')
    args = parser.parse_args()

    nameset = set()
    for name in open(args.listfile):
        name = name.strip()
        nameset.add(name)
    print 'loaded %d names' % (len(nameset),)
    
    outfp = open(args.outfile, 'w')
    
    m = 0
    for n, record in enumerate(screed.open(args.ffn_file)):
        if n % 1000 == 0:
            print '...', n, m
        name = record.name.split()[0]
        if name in nameset:
            # keep the sequence
            m += 1
            outfp.write('>%s\n%s\n' % (record.name, record.sequence))



if __name__ == '__main__':
    main()
