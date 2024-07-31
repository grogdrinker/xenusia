#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  predittore_ffnn_fromseq.py
#  
#  Copyright 2019 Gabriele Orlando <orlando.gabriele89@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#
import time,os
from xenusia import utils,NNWrappers
def quality_check_aaSeq(sequences):
    allowedLetters = ['A', 'C', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'M', 'L', 'N', 'Q', 'P', 'S', 'R', 'T', 'W', 'V', 'Y']
    for k in sequences:
        for l in sequences[k]:
            if not l in allowedLetters:
                raise ValueError("Non-amino acid letter "+l+" found in sequence"+k)

def run_prediction(sequences,device):
    print("Testing ",len(sequences),"proteins")
    contactModel = NNWrappers.NNwrapper(device=device)
    contactModel.load()
    model = NNWrappers.NNwrapperDomain(device=device, extra_model=contactModel)
    model.load()

    names = sorted(sequences.keys())
    resu = model.predict(sequences)
    x=[]
    for i in range(len(resu)):
        cc = utils.sliding_w(list(resu[i]))
        x += [max(cc)]

    return {names[i]: x[i] for i in range(len(names))}
def prediction(sequence,outfile=None,device="cup"):
    print("Running prediction")
    old_time = time.time()
    if os.path.exists(sequence):
        sequences = utils.leggifasta(sequence)
    else:
        sequences = {"inputSequence":sequence}
    quality_check_aaSeq(sequences)
    pred = run_prediction(sequences,device)
    if outfile is None:
        print("###########")
        print("# XENUSIA RESULTS #")
        for k in pred.keys():
            print(k, round(pred[k],3))
        print("###################")
    else:
        f=open(outfile,"w")
        f.write("Name\tScore\n")
        for k in pred.keys():
            f.write(k+ "\t"+str(round(pred[k],3))+"\n")
        f.close()
    print("Done in ",round(time.time()-old_time,4),"seconds. The monkeys are listening")


if __name__ == '__main__':
    import argparse,sys
    import textwrap
    parser = argparse.ArgumentParser(
        prog='Xenusia',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''\
             if you have problems or you bugs,
             mail orlando.gabriele89@gmail.com.
             
             The monkeys are listening
             '''))

    parser.add_argument('sequence', help='Either an amino acid sequence or a fasta file with amino acid sequences')
    parser.add_argument('--outfile',"-o", help='the output file. if not provided, it prints on screen',default=None )

    parser.add_argument('--cuda', action='store_true', help='run everything on GPU')

    args = parser.parse_args()

    if args.cuda:
        device="cuda"
    else:
        device="cpu"

    prediction(args.sequence,outfile=args.outfile,device=device)



