Link to any outside resources in this README


Q1: Are the majority of the CpG dinucleotides methylated or unmethylated?
* yes, the majority are methylated

Q2: Calculate the number of sites present only in the bismark file, present only in the nanopore file, and the shared sites as a percentage of total sites (both unique and shared sites)

*0.5403406688601172

Q3: How does using nanopore for methylation calling differ from bisulfite sequencing in terms of coverage? Which method appears better and why?
* Bisulfites have more variance coverage when compared to nanopore. Nanpore is better for longer reads for repetitive regions. It depends on what you are looking will depend on which sequencing you will want to do.

Q4: What can you infer about the two different approaches and their ability to detect methylation changes? Q4: What is the effect of tumorigenesis on global methylation patterns?
 * I can infer from bisulfite sequencing is that it is high resolution, but is limited while nanopore is better for longer reads as I previously stated. It  would be best to use both methods to look at methylation changes. 
 As for tumerigenesis, it will be different for each tumor. There will be similar landmarks within the tumor depending on its origin and cell type, but in general they will be different from the usual pattern seen in healthy patients.
 
Q5: What changes can you observe between the normal and tumor methylation landscape? What do you think the possible effects are of the changes you observed?
* There are some regions where there are some methylation from the tumor landscape that the normal have and vice versa. There are multiple effect that are happening within a tumor cell that are not seen or fully understood yet.
  
Q6: What does it mean for a gene to be “imprinted”? 
*When Jacob falls in love with a baby vampire hybrid. 
  
Q7: What is happening when you select the option to phase the reads? What is required in order to phase the reads?
*It gives you genetic information about the variance happening. What is required is a normal reference. 
  
Q8:Can any set of reads be phased? Explain your answer.
*Being phase is having 2 variant, phasing is telling which parent the variant comes from. You need parental DNA and genetic variance to be able to determine where it comes from.