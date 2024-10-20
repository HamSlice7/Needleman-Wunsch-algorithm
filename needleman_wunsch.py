import numpy as np

def needleman_wunsch_algo(sequence_1, sequence_2, gap_penalty, mismatch_penalty,award_penatly):
    
    #Getting the number of rows and column for the matrix
    n = len(sequence_1)
    m = len(sequence_2)

    #Generating a matrix to hold the scores
    scores = np.zeros((n+1,m+1))
    
    #Fill in first column
    for i in range(0, n+1):
        scores[i,0] = gap_penalty * i

    #Fill in the first row
    for j in range(0,m+1):
        scores[0,j] = gap_penalty * j
    
    print(scores)


needleman_wunsch_algo('AAATTT', 'AAATTC',-1,-1,1)