import re
import sys
import operator
import numpy as np
import timeit

def generateIndices(input_vector, num_dims):
    s = slice(None)
    index_list = []
    last_index = -1
    cur_index = len(input_vector) - 1
    
    if num_dims > 0:
        #find location of the last slice
        for c in input_vector[::-1]:
            if input_vector[cur_index] == slice(None):
                last_index = cur_index
                break
            cur_index -= 1
            
        #new slice will be next to the last slice    
        z = last_index+1    
        
        #generate a list of all possible index lists s.t. new slice occupies positions after the last slice
        while z < len(input_vector):
            temp_list = list(input_vector)
            temp_list[z] = s
            index_list.append(temp_list)
            z+=1
    else:
        index_list.append(input_vector)
            
    #if more slices to add
    if num_dims > 1:
        tmp_list = []
        #go through each possible index list and recursively add one more slice.
        #add result to the result list.
        for v in index_list:
            tmp_list.extend(generateIndices(v,num_dims-1))
        
        return tmp_list
    #if no more slices to add return the list generated in this call
    else:
        return index_list

let_to_int = {'A': 0,'C': 1,'T': 2,'G': 3}
int_to_let = {0:'A',1:'C',2:'T',3:'G'}   
complements = {'A':'T','C':'G','G':'C','T':'A'}

def genomeLettersToInts(input_str):    
    out_str = []    
    for c in input_str:
        out_str.append(let_to_int[c])
        
    return out_str

def intsToGenome(input_list):
    out_str = []
    for c in np.nditer(input_list):
        out_str.append(int_to_let[int(c)])
    
    return out_str

def getWinnerList(winners):
    x = np.vstack(winners).T
    q = np.vectorize(int_to_let.get)(x)
    for w in x:
        print(''.join(intsToGenome(w))),

def getReverseComplement(input_list):
    lookup = {0:2,1:3,3:1,2:0}
    out_list = []
    
    for x in input_list[::-1]:
        out_list.append(lookup[x])   
   
    return out_list

def doIt():
    '''
    myFilename = "/Users/siakhnin/Downloads/dataset_8_5 (2).txt"

    f = open(myFilename, 'r')
    inputstr = f.read()
    
    '''
    #inputstr =  """ACGTTGCATGTCGCATGATGCATGAGAGCT
    # 4 1"""
    inputstr = """CACCAAGCAAGACCCCAAGCCAAGCACCCAAGACCACCCCGCTCTCAAGCTCTCCGACCACCCTAAGACCACCAAGAAGCTCAAGAAGCCTCTAAGCTCTCAAGACCCCGCTCACCCCGCCGCTCCGCTAAGCACCCCGCCTCCGCCGACCCCGCCAAGAAGCCCGCCTAAGCTCCGACCCTCACCCCGCAAGCCCCGAAGCTAAGCCTCCGCTCCGCCGCTCCGAAGACCAAG
9 2"""
    inputlist = [x.strip() for x in inputstr.split("\n")]
    inputstr = inputlist[0]
    tmp = inputlist[1].split(" ")
    k = int(tmp[0])
    print(k)
    max_mismatch = int(tmp[1])
    print(max_mismatch)
    global_kmer_count = np.zeros([4]*k)
    
    
    for i in range(0,len(inputstr) - k + 1):
        local_kmer_count = np.zeros([4]*k)
        
        cur_kmer = inputstr[i:i+k]
        cur_indices = generateIndices(genomeLettersToInts(cur_kmer), max_mismatch)
        
        for val in cur_indices:
            local_kmer_count[tuple(val)] += 1
            
        global_kmer_count[local_kmer_count > 0] += 1
    
    mask = global_kmer_count > 0
    indices = np.vstack(np.where(mask)).T
    
    winners = np.where(global_kmer_count == global_kmer_count.max())
    getWinnerList(winners) 
    
    new_kmer_count = np.copy(global_kmer_count)
    for row in indices:
        new_kmer_count[tuple(row)] += global_kmer_count[tuple(getReverseComplement(row))]
        
    winners = np.where(new_kmer_count == new_kmer_count.max())
    getWinnerList(winners)   

doIt()



