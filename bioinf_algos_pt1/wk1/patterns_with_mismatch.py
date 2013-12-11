import re
import sys
import operator
'''
#myFilename = input("Eneter filename:")
myFilename = "/Users/siakhnin/Downloads/rosalind_1f.txt"
f = open(myFilename, 'r')
inputstr = f.read()


inputstr =  """ATTCTGGA
     CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT
     3"""
inputstr = """AGGTACAT
ACTTCATACAACTGACAGCGGACCCCAAGAAGGGTGTTCACTCCTGTTCACTATACCCATAGGGCGAACTTAAAGAGGACGTGATTGAGAACATCTCGACGTGCGATGACCTACTAACTGTCAGGAGCATCAATCACGTTGAAACCAAGGCCCTCGCTAATTATGCATTAGCATTAACTCTCACGAACACACGCGGTTGGCTCTCCCGGGAGTCCGCCAGAGGATGACCAGCTGGGACGCACGTGGTCAGGGTGAAGACCGCTGTTACGACATCAGCACTCATGTGTGGTGGCAAGCTACTGACTTTGAGCACGCCAAGACAGTACTGTCGAGGGTACACGAGCAATAGATCACAGCCTAATCGGGGTATTGGGAAATATTTTTAATAGTTGGGCAGGAGGTCTGGGGGGTCACATTATGCGAGAGCGTGCCGTATGAATATATAGGAAAATAGTTGCTAGGAGGCATTGCCAGGTCTAACCCGCTACCAACTCAGGTACTGCAACATCAGGCGGGAAGGCGAGTCGGGTTAATTTGCGGCATACGAGTACAATCTTATGATTCGCAACCTAATGCTTGTGAGCATGGCTTTATTCCGAAGGCGGCCGGAGGTCGAGCCGCCACGGTAAGCGGACCTACAACAGATTACCTTACCAGCTTGATATTGGCGACATAGACCACTGAGGGATAGCAGCTTTGTGCCTGCGATGTACTCACTGTGCGCCAGGAAACTAAATCTTATTACCCCCTTGTCTCTGAACACGAATGACGAGATTGGGATAGGACACAAGTAGTGTGGCGTGTAGGTCACGCCATATGTGCACACACTTGATCCAAGCCCAAAACTCCGAATGCTGAATAATGACACGTCGATGTTTCCCCTACCGAAATTACAGGGGGTGCCCTTCTCAATAGGGCCGACTGGACGCTGTCCCGCAGATTGTTTTAGTCCATTAACGTGGTGATGCTGCTACTAAACCAAACATTAACTACGGCGGCGGGAAATGCGCCTTAATTTAATCGAGGGCCGGCTGGGTTATCGAGTTTTACGGCTAGCTACGCGTGTGATCTCCCCCCGGTCCTGATTACCAGAGTCGCGTTCAATCCCAACCAGCTAAAGAGCGGAACACAAGTCGAATTGAGTGATGCAATGGGCTCGCAGCGTCCCATGGGGGTAGGTCCTCCCCCCGGTAAAACCCGCTCTTAATGTCCTGTCGCAGAATCCCCTAACTAAGGGACACAGCGCCGCTAACTTGGTCCTAACACAAGCAGATATCAGCTTAGCCTGCCTAATTGTGTTCAAGCCCTCAATCTGCACATGGGCAAAGGAATACGACCCTCAAATCTCTTTGGCTCACTATAGTGACTGCTCTTAAACCCCTGGCATCTCTATTTCAATGGCGAATCGAAAAGTCGCGCGCTAATCCTGAGAGACAGTTACAAATCTCCATCACACCGGCCGTCGCTCGCTCGATTTCTGCCACCGTCGTGTCATCTCGCCTTACCAGCACCCAAAGGGAAGACCGCAAGTGATATTAGGACAACGTTCATTCACATGCGGACTATATGCTGCTGGCCATCATTGAGCGGCCGGTATTAGCCCAAGCGGTCGCAGTCGATGTTGAACCACAGAAGGCATGTGTCTAATTTCCGGGGCGTATCGGGTTATTCTGCTCGTTTAGGAGCCGTTCGCGCCAGGACCGTAAGGGAACTTGGAATTTACGTGCGCCTCTTAGTCCGGTCCAACCGCGCGTGATATAGGTGCAAGTAAGTACAACCGCAATTGATTCACTCTTACCTCCGGACGGAAGCGACGGCTCACTTTCGGGATCAGTTTTGTCTCACTACGACTGATCGAAGGGTCTTAGGTCGGTATCGTTAATATCACGCAGACGTCAGTGAACCAGTACCACGAGGTAGCAAGGTAAATGCCATAGCTGGCACATCGGACCAGCTTTGTCCGAAACCGTTCTAGAAACGTGAAGCTCCCATGTCCGCTCAAGCTTATAGTTTTTTTAATGACATAAAGTGCCCGACGTCCACTCACGAATTGCGCAGACTTGGCCCACTCGGGAGACCTATAAATGAAACCAGATAGTCTCTAGTATCGGTTCACATGAGTAGGTACTGGAGGATTGATTTTATATTATAGTAGGGTCCTTTGATCGTGGTATAGAGCCGAGCATTTTCATCTAAAAAGCTATCTAAGCGGATCTGCCCATACGCGCTACTGGTGGCCTACGGAGATCAACCCCTTTTGGACGCAGCGTGAGCCATTAAACTAGCGATATGTGAACATCTCCCTTAGGGAGGGCGCCACGTTGTAGTTGGGGTCGGCCATCGCGATTATGAGGGCGAAGTGTGACTTGAGTTCGTCACGCGCAAAACCACAACCTCCGTTAGTCTCATGTTTCGACTACGGCCAAACGTTAGGTACAGCGATCTTAACCCTCTCAAAGTTGAAACACGCGCCTAGGCTGGTGGCTAAAACTAGCTGGATTCAGCTTGACCGCAGGACGGGCCGGAAGAGACGTTGCGTGATTACATTGGAACTTAGGTCAAATTTGACGCCTATCCCCAATCAAACCATATAATGTACGGTGGTTATAATGCTGGCCAATGAGCAAGCCAGCTAGACATTGTGTTGATGTGCCAATTGTAAGAATTCATCTATCGGCAACGGTCAATACCTTTCTTCATGGACTTGTTATCATGTAGAACCAGCGAAGGCACCTTACAAATTCGCCCGATGACTAGCTACTGCGTTCCCAAAACGACAGCAATTTCTATAGGCGGTACCCACGTCGCTTAAGAAGGCTGCACTCCCCCCCCCAAGCATTTACCACCGAGAACTAAAATCGCCTTATTCAGTGCACCGGCCGCACGAACCAATACAGTACCCTGTGTTTCGTGACTGAGACAGTGACACCTCTCGGGTGTAATTCGAGCTCAAGGTAGGTGTTTGTGGAGCTTCGACCGGTTATGATGCGCGAGTTGGGGCTCACTCACGGTTGATAAGCGCACAGGTACTGCACCTCGCCATCATGTCGTACCGTGGTCATTCCTAGGCAGTCGGACACTGAGGTTTTGCACCATCGCTCACTGAAATTCTACACTCGTACTCACTCAGCGCTGTTCATGTCCGGCCCTTCTGCCCAATGTTATCAGGCCACCTGAAAACTGGCTCGACAAGGCATGATATTAGGGATAACGGCTGCGACAACGCATCGGAAGACACCCTTCCTATTTAAGTAAAGGACGGTCTCTGGCGTCATTGTAGTGGAGATAATCAACCAAGGACGTTCTATGTGTAGCACGCAATTGGGCCATACCAACCGAATATTAGGACAATGCTATGCTTTAGTTACCTAGGTACGCATCTGCCTCTGCTGGTTCGCCACCCAGCCATTTAGTTTGAGGCGTTCGGTGTTACACTATCACTCTACGACCGTCACTTGAGCTATTGGGCGTGTCATACTGAATCTTTATACCGACGGCTGTAAGTGTATGGATACATGATCCCGGGTTACAATTCGAACCTTCCATCGGCTTAGCGTTGATATTTGGCAGTATCTTGGATTTGACCAGGCGTCTCCCGTTTAGGGAGGTCGTATTTAAATTCCATTTGCAGTAAAGCTTATTGTAACTTTTGTACCGGGGTAAATAGAGGCGGGTGTCCGCGAAGACTTCCCAGTAAAGCTCCAATCCAACTATCCCGAAGGCGAGTTTGTCGGTACCTATTCGAGGCCGCGGTTTCCAACACGCAGTGACAACCTGGAATTTTCATATCGAACCGAGATGCTGAACAAGGTGCGTACTGGTGTACAGAACCTGCTCTTGCAGCACCCCCTCAGGACGCCGGTAAATCGTTATGGCTTCCTGCACACCCTAGGAGGTCAATCTTAAAGCCTTGCGAAGGTCATAGGAGGAGTGAGTTCGCCATATGGCGCCCCAAGGTAAGCGCCGAAGCCTGGCGTATAGTGACGATTGGCACAGAAATCCCTTGCAGTAGTGCCCGAAAGGTAACTGCGGTACGTGTTTAGACCATACGAAACGGATTTGTGGGGAGTCGCAATAATAGCCGGGAGCTTTCCATAAGGTCCTATACACGGCGAAGACGCAATTGGCTGATAGTCAAGGTTTAGTTCCTAATCAATTCATATGGCCGCTTGCGTATTACAAACCAGGTGCCCCAAGGAGTTCGCGGGCCGCACCCTCGGCCGTCATTCGGCATGTTGGGAAGGTCGTGGGAGGGTCGATCGGTCCTGCCGTAGCGTAGAATAGTACGAGAGTAATAGTGAGTCAGCACAAGGTTTCGCCGACTTGGACCCATACGGTAATGATTACCCCAGTATCGCAGACCAGGTCTGAATCCGAGGTTTCCAGTCAGCAACATTTAGGATGGGAAAGTGGAGTGTAACCATGTGGAACTGAGACTCTAGAAACATAGGCATGGTCAACGAAATCGGTATCGGGTTCACACCGCTTTACAAACGTGACCGAGGTATGCAGAGCCTGCTCTCGAACGGAAAGTACAAGTGTAAAGGTAGACTCACTGATGAGCTTCATTGGACGATCTCGTAATGTCAACGGTGGGTCAGGTGAGCTAGCAAATGCCGCAGGGGGTTCGCTGTCCGATTAACAATTTCCAATTGGTGCCAGATGTGTCCGCCTCAGTGTACCTCGAAAGCCCATTCTATTGTGAGGTAAGTTCCTATGTGTCGCTGCGGACTGAAGGAACCAAAAATAACCGGGGTTTCCCTGTACATTTCCTAACAGCGAGGTATGGTAAATCAGTATGTCGTGCATATGTGTCTGATTGGGACGTTATATTTCTGTACACTAGTTAATATCTCCACTTTCCCAGTCAACTATTCTCGCGTCACACTAACAGTGGAAGACCCCGATACAGGGCGGCGACGCGTCTTTAACACCTGTGATCGGGATTCGAAACTGGGCCAACACATAGCGCATAATGGTACAGTGTATGTTCATAGGTGCGCGCGTCGGTGTGCCGGAAGAGGATGCCTGGAGCCGCGACTAGGTAGAGCAGGTGCCGTTACAGCACACCCTGCTAAACTCGCTGTATTGCTCTTGAATAAAGCTAACGATACCTCATATTTCGAGTGGAGTTATGTATCCCTCCAAGTGATGTTCGCTCACGTACGGAACCCGGCCAGGGGCATATAGTCCTACCCCGACTCCATAATATTGACCGCAGTGCTGCTCTACTCGTGGATGCTTTAAACATGGGGTTATACCTTTCGCGGCTTGCTTTTTCCGAACTTGCACTCAACTGAATTACTATGAAAGGAACAGCTGACTCAATCATTAGAAGTGTGCTGTTATGGGTACGGTTACAGTCAACCTCATTTCATCTGTTCTATATACTGTGCGGGGGCCTGGCACAGCGGTCAAACAGCCCCTTATTTGCCGGGTACTGGTGTGTCGGGCGACTAAAGAAAAGCACCGATGATGGACATCTGTGTTTTTTGACTGCGGACTAGTTATGAGTTCAAGATTAATATGACCCGCATTATCAGCCGTGGCTTAGCGTCCTGGTTAGTGAAACACATTGCTAGCCATCCTCCGATTTTCACTCCGAATGTTTGAGGAGCGCTCTCGACTTAGGTCATGGATCCAAAACAGTCGATTGAAGCCTCGCACATTCAAGCATAACGATGGCATGTATTGATGATGCACTCTGACTATTCAACGCGCCGCTGATACCATCGTTAATTCAGTTAATTTAGATAGAATGTGTCGACGTCGACACCTCTATTTGCATGGTGGTGGGGTAGGTTAAAGATTTGCCAATGCCAGAAGCATCACCCACCCTGAAGCCTACTCGCGCACAGTTGTAATGGTATGCCCGATGACCTCCTATTCGTAATCTGAATCGAATCAAGTTCCAAGTTCGTGCTGGATAGTAGGAGGTCTGCAACGCTCCGCTCGGTTTTCAGGCGCTTTTCCGAATCCCTGAACTCCCCGACAGTCGATGCGTAATTATCGTCCTTTCTCATCTCAAGAGTATTGCTAATCCTGAAATTCGTTACTTGTTCTTCTGCTCGTTCCTCGATTCGCTTCGACGTTGATGGTCGTCATGGTCACTGGAATGGGTGGGACTGCATTATTCGGGTACATTAGAGTCGCAGTAGCTAACGAGATGCATTGAGAGCTATACAGGCCAGTGGACGTCTCCCTGCCGTGTCCATAGTATGACGATCAATGGTGGGCGCTACACTTGGCCCTTACTCCGTCCGCGACATACTTACTGGGTCTTACTTCACCTTTTGCTGTTTGTATCAGCACTGTCAGAGGAAAGCACGAACCACCAGTCGGCGTGTGCACGAGTTTCCAACTACTAACCATGTGCCGGATAAAGATTCAATTGAGCGCCTAGCCCCATCATAGTCCCCGAGTATACCCATAGTTAGCGTTATGTTCATGAGTGGTGTGAATATCGTTGCGTTTTTGCGTGGAGTTGCGGATAGCCCCACATAAGATGTGTTCTTTTTTCGCCTAGGCCCGATCGTTCTGCGTGGGTAGAATTTGCTTAAACGGACGCTGAGGACACATATTGCGAAATGAGTCCAGGTATGCGCGTCTGGGTGCCACTACAAGGTACGTTCTATTAGTACGCACTTAGGCTTCTCAATCAAGGGTAACGTGCTTATGCTAGACGGCGGTAGGCTTACCTAGACTCCCACGTCTACAAATGGTAGAATGAAGCGGCCGGATAGTAGGCATAGGCGGAGCGCGTATTCTGTAATTCGCACATTAGATCCCCGACACTGTTAACGTCGTGTAACGGTCAAGGGGTTGATTACCGATCATCGTCGTTTGAACGCAGCTTAGTCACGAGAACGCGTCCCTCACGTACTAAGGATAGACTTCGCTGGAGCTGGCTGATACAAGAGAATTAGCCCTTCCTTGTGATAGGTACAT
5"""
'''
inputstr =  """CCGCCCCGC
     CACCAAGCAAGACCCCAAGCCAAGCACCCAAGACCACCCCGCTCTCAAGCTCTCCGACCACCCTAAGACCACCAAGAAGCTCAAGAAGCCTCTAAGCTCTCAAGACCCCGCTCACCCCGCCGCTCCGCTAAGCACCCCGCCTCCGCCGACCCCGCCAAGAAGCCCGCCTAAGCTCCGACCCTCACCCCGCAAGCCCCGAAGCTAAGCCTCCGCTCCGCCGCTCCGAAGACCAAG
     2"""
def isSimilarEnough(str1, str2, threshold):
    cur_score = threshold
    #CCCCGCACC CCCCGCCCC CCGCCCCCC CCGCCCCGC
    # subtract length difference from score
    cur_score -= abs(len(str1) - len(str2))
    
    #early exit
    if cur_score < 0:
        return False
    
    for i,c in enumerate(str1):
        #have characters in both strings
        if i < len(str2):
            #one mismatch found
            if c != str2[i]:
                cur_score -= 1
        #string2 ran out of characters        
        else:
            break
        #early exit
        if cur_score < 0:
            return False
    
    if cur_score < 0:
        return False
    else:
        return True
    

inputlist = [x.strip() for x in inputstr.split("\n")]
pattern = inputlist[0]
genome = inputlist[1]
max_mismatch = int(inputlist[2])

for i,c in enumerate(genome):
    if isSimilarEnough(pattern, genome[i:i+len(pattern)], max_mismatch):
        print(i)
