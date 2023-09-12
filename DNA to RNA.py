# Function to transcribe DNA to RNA
def transcribe_dna_to_rna(dna_sequence):
    rna_sequence = ""
    for nucleotide in dna_sequence:
        if nucleotide == 'A':
            rna_sequence += 'U'
        elif nucleotide == 'T':
            rna_sequence += 'A'
        elif nucleotide == 'C':
            rna_sequence += 'G'
        elif nucleotide == 'G':
            rna_sequence += 'C'
        else:
            print("Invalid DNA sequence. Please enter a valid sequence containing only A, T, C, and G.")
            return None
    return rna_sequence

# Input DNA sequence from the user
dna_sequence = input("Enter a DNA sequence: ")

# Convert the DNA sequence to uppercase to handle lowercase input
dna_sequence = dna_sequence.upper()

# Call the transcribe function and display the result
rna_sequence = transcribe_dna_to_rna(dna_sequence)

if rna_sequence:
    print("Transcribed RNA sequence:", rna_sequence)
