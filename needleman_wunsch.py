import numpy as np

def needleman_wunsch_algo(sequence_1, sequence_2, gap_penalty, mismatch_penalty,award_penatly):
    
    #Getting the number of rows and column for the matrix
    n = len(sequence_1)
    m = len(sequence_2)

    #Generating a matrix to hold the scores
    scores = np.zeros((n+1,m+1))
    print(scores)


needleman_wunsch_algo('ATGATGA', 'GCGCGCGC',-1,-1,1)