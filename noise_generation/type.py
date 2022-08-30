import random

import numpy as np
import numpy.random
import pandas as pd

noise_levels=[0,1,2,5,10]
# the amount of noise generated in %
for x in noise_levels:
    noise_level = x

    input_data = 'C:/Users/vince/Desktop/Studium/Thesis/experiments/wnrr/data/valid.txt'
    # training_data = "C:/Users/vince/Desktop/test/train.txt"

    data = pd.read_csv(input_data, sep='\t', header=None)
    data.columns = ["head", "relation", "tail"]
    rows = (len(data.index))
    #make a list of all relations in dataset
    uniqueRelations = np.array(data.relation.unique())
    typeRegistry = {}
    #go through the datasset and save for each relations the indices of facts connected by that relation
    for index, row in data.iterrows():
        same_type = np.where(uniqueRelations == row.relation)[0]
        current_type = same_type[0]
        # data['type'][index]=current_type
        print(index)
        indices = typeRegistry.get(current_type, [])
        indices.append(index)
        typeRegistry.update({current_type: indices})
    i = 0
    modified_triple = []
    #until noise level is reached, replace either head or tail of a fact with the head or tail of a fact using the same relation
    while i < int(rows * noise_level * 0.01):
        randType = numpy.random.randint(len(typeRegistry.keys()))
        typeArray = typeRegistry.get(randType)
        if (len(typeArray) < 2):
            continue
        random.shuffle(typeArray)
        head_or_tail = numpy.random.randint(low=0, high=2)
        #check if the triple has already been altered, in that case skip to next triple
        if (typeArray[0] in modified_triple):
            continue
        if (head_or_tail == 0):
            data['head'][typeArray[0]] = data['head'][typeArray[1]]
        else:
            data['tail'][typeArray[0]] = data['tail'][typeArray[1]]
        modified_triple.append(typeArray[0])
        i += 1
        print("Modified: " + str(typeArray[0]))
    print('done')
    #the outputfile name is a placeholder since it has to be placed in the correct folder and then be renamed anyway to 'test' or 'valid'
    outputfile = 'dataset_with_' + str(noise_level) + '_noise.txt'
    data.to_csv(outputfile, sep='\t', header=False, index=False)


