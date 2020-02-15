def proteins(strand):
    map = {
        'AUG': 'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': 'STOP',
        'UAG': 'STOP',
        'UGA': 'STOP'
        }
    proteins = []

    chunk_size = 3

    for i in range(0, len(strand), chunk_size):
        codon = strand[i:i+chunk_size]
        protein = map[codon]
        if protein == 'STOP':
            break
        proteins.append(protein)

    return proteins

