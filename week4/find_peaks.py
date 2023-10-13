#!/usr/bin/env python

import sys
from pain import load_bedgraph, bin_array
import numpy
import scipy.stats
import matplotlib.pyplot as plt



def main():
    # Load file names and fragment width
    forward_fname, reverse_fname, out_fname, control_fwd, control_rev, fragment_length = sys.argv[1:7]
    
    forward_fname = sys.argv[1]
    reverse_fname = sys.argv[2]
    out_fname = sys.argv[3]
    control_fwd = sys.argv[4]
    control_rev = sys.argv[5]
    fragment_length = sys.argv[6]
    fragment_length = int(fragment_length)



    # # Define what genomic region we want to analyze
    chrom = "chr2R"
    chromstart = 10000000
    chromend =  12000000
    chromlen = chromend - chromstart

    # # Load the sample bedgraph data, reusing the function we already wrote

    forward = load_bedgraph(forward_fname, chrom, chromstart, chromend)
    reverse = load_bedgraph(reverse_fname, chrom, chromstart, chromend)
    
    # # Combine tag densities, shifting by our previously found fragment width

    combined = numpy.zeros(chromlen, int) 
    combined[:-fragment_length//2] = reverse[fragment_length//2:]
    combined[fragment_length//2:] += forward[:-fragment_length//2]
   
    # # Load the control bedgraph data, reusing the function we already wrote
    forward_ctrl = load_bedgraph(control_fwd, chrom, chromstart, chromend)
    reverse_ctrl = load_bedgraph(control_rev, chrom, chromstart, chromend)
    # # Combine tag densities
    combined_ctrl = forward_ctrl + reverse_ctrl

    # # Adjust the control to have the same coverage as our sample

    # # Create a background mean using our previous binning function and a 1K window
    # # Make sure to adjust to be the mean expected per base
    coverage_num = numpy.sum(combined)/numpy.sum(combined_ctrl) # calculated total data in sample
    combined_ctrl = combined_ctrl * coverage_num
    

    # Find the mean tags/bp and make each background position the higher of the
    # the binned score and global background score
    background_mean = bin_array(combined_ctrl,1000)
    background_mean = background_mean/1000
    background_mean = numpy.maximum(background_mean, numpy.mean(combined_ctrl))

    # Score the sample using a binsize that is twice our fragment size
    # We can reuse the binning function we already wrote
    combined_scored = bin_array(combined, 2 * fragment_length)

    # Find the p-value for each position (you can pass a whole array of values
    # and and array of means). Use scipy.stats.poisson for the distribution.
    # Remeber that we're looking for the probability of seeing a value this large
    # or larger
    # Also, don't forget that your background is per base, while your sample is
    # per 2 * width bases. You'll need to adjust your background
    pvalues = 1 - (scipy.stats.poisson.cdf(combined_scored, background_mean *2*fragment_length))

    # Transform the p-values into -log10
    # You will also need to set a minimum pvalue so you doen't get a divide by
    # zero error. I suggest using 1e-250
    pvalues = numpy.maximum(1e-250, pvalues)
    pvalues = -numpy.log10(pvalues)

    # Write p-values to a wiggle file
    # The file should start with the line
    # "fixedStep chrom=CHROM start=CHROMSTART step=1 span=1" where CHROM and
    # CHROMSTART are filled in from your target genomic region. Then you have
    # one value per line (in this case, representing a value for each basepair).
    # Note that wiggle files start coordinates at 1, not zero, so add 1 to your
    # chromstart. Also, the file should end in the suffix ".wig"

    # Write bed file with non-overlapping peaks defined by high-scoring regions 

def write_wiggle(pvalues, chrom, chromstart, fname):
    output = open(forward_fname, 'w')
    print(f"fixedStep chrom={chrom} start={chromstart + 1} step=1 span=1",
          file=output)
    for i in pvalues:
        print(i, file=output)
    output.close()

def write_bed(scores, chrom, chromstart, chromend, width, forward_fname):
    chromlen = chromend - chromstart
    output = open(forward_fname, 'w')
    while numpy.amax(scores) >= 10:
        pos = numpy.argmax(scores)
        start = pos
        while start > 0 and scores[start - 1] >= 10:
            start -= 1
        end = pos
        while end < chromlen - 1 and scores[end + 1] >= 10:
            end += 1
        end = min(chromlen, end + width - 1)
        print(f"{chrom}\t{start + chromstart}\t{end + chromstart}", file=output)
        scores[start:end] = 0
    output.close()


if __name__ == "__main__":
    main()