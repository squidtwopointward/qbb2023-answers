#!/bin/bash

# chmod +x bash_script.sh
# ./bash_script.sh

# bwa index c_elegans.PRJNA13758.WS283.genomic.fa

# the "do"indicates the start of the for loop

# for sample in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63 
# do 
# 	echo "Aligning sample:" $sample
# 	bwa mem sacCer3.fa\
# 	${sample}.fastq\ > ${sample}.sam

# done # indicated what will end


#Regrouping It is meta data that is being stored. Adding more information
#adding the t did can be used to speed up the program t= treads
# for sample in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63 
# do 
# 	echo "Aligning sample:" ${sample}
# 	bwa mem -t 4 -R "@RG\tID:${sample}\tSM:${sample}" \
# 	  sacCer3.fa \
# 	  ${sample}.fastq \
# 	  ${sample}.fastq > ${sample}.sam
# done

# for sample in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63 
# do
# 	samtools sort -O bam -o ${sample}.bam ${sample}.sam 

# 	samtools index ${sample}.bam
	
# done


# for sample in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63 
# do 

# freebayes -f sacCer3.fa A01_09.bam A01_11.bam A01_23.bam A01_24.bam A01_27.bam A01_31.bam A01_35.bam A01_39.bam A01_62.bam A01_63.bam -p 1 --genotype-qualities > variants.vcf


# vcffilter -f "QUAL > 20" variants.vcf >filtered.vcf

# vcfallelicprimitives -k -g filtered.vcf > decomposed.vcf

# snpEff ann R64-1-1.105 decomposed.vcf > annotation.vcf

 