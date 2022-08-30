import random
from random import randint

import pandas as pd


noise_levels=[0,1,2,5,10]
# the amount of noise generated in %
for x in noise_levels:
    noise_level=x
    file = 'PATH_TO_DATA'
    data = pd.read_csv(file, sep='\t', header=None)
    data.columns = ["head", "relation", "tail"]
    rows = (len(data.index))

    # select random relations where nodes will be modified
    acceptor_triples = []
    indices = list(range(rows))
    random.shuffle(indices)
    for x in range(int(rows * noise_level * 0.01)):
        acceptor_triples.append(indices.pop(0))
    print(acceptor_triples)

    # select donor nodes from disjoint set of relations
    donor_triples = []
    for x in range(int(rows * noise_level * 0.01)):
        donor_triples.append(indices.pop(0))
    print(donor_triples)
    printed_progress = ''

    # randomly select a head or tail node to be altered
    for x in range(len(donor_triples)):
        head_or_tail = randint(0, 1)
        if head_or_tail == 0:
            data['head'][acceptor_triples[x]] = data['head'][donor_triples[x]].copy()
        else:
            data['tail'][acceptor_triples[x]] = data['tail'][donor_triples[x]].copy()

    print(data.head())
    #outputfile has to be copied into correct dataset folder and renamed to either valid.txt or train.txt
    outputfile = 'outputfile_' + str(noise_level) + '.txt'
    data.to_csv(outputfile, sep='\t', header=False, index=False)
print("done")
