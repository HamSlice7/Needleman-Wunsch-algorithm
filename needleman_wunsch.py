import numpy as np #later write my own function for creating a zero's matrix

def match_score(n1,n2, mismatch_penalty:int, match_award:int):
    """
    Function that will check if two inputted nucleotides are a match or mismatch and return
    a match award or a mismatch penalty respectively

    """
    if n1 == n2:
        return match_award
    else:
        return mismatch_penalty




def needleman_wunsch_algo(sequence_1:str, sequence_2:str, gap_penalty:int, mismatch_penalty:int, match_award:int) -> str:
    """
    Calculate the optimal globl alignment of two sequences via the Needleman-Wunsch algorithm

    Input:Sequences that with be globally aligned via Needleman-Wunsch and the desired gap penalty, mismatch penalty,
    and match award. Later include linear of affine penalty
    Output: The optimal global alignment for the two sequences via Needleman-Wunsch

    """
    
    #Getting the number of rows and column for the matrix
    n = len(sequence_1)
    m = len(sequence_2)

    #Generating a matrix to hold the scores
    scores = np.zeros((n+1,m+1))
    
    #Fill in boundry conditions for first column to initialize recursion relation
    for i in range(0, n+1):
        scores[i,0] = gap_penalty * i

    #Fill in boundry conditions for the first row to initialize recursion relation
    for j in range(0,m+1):
        scores[0,j] = gap_penalty * j
    
    print(scores)


needleman_wunsch_algo('AAATTT', 'AAATTC',-1,-1,1)