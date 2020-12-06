#!/usr/bin/env python
# coding: utf-8

# In[1]:


def make_matrix(str1, str2, match, mismatch, gap):
    
    
    # Make strings into list
    s2 = list(str2)
    s1 = list(str1)
    
    
    # Make empty matrix
    mat = [[None for i in range(len(s2)+2)] for j in range(len(s1)+2)] 
    arr = [[None for i in range(len(s2)+2)] for j in range(len(s1)+2)] 
    
    # Set top left entry to be a blank string
    mat[0][0] = ''; mat[1][1] = ''; mat[0][1] = ''; mat[1][0] = ''
    arr[0][0] = ''; arr[1][1] = ''; arr[0][1] = ''; arr[1][0] = ''
    
    
    # Fill first row and column to be the given strings
    for i in range(2, len(s1)+2):
        mat[i][0] = s1[i-2]
        arr[i][0] = s1[i-2]
    for i in range(2, len(s2)+2):
        mat[0][i] = s2[i-2]
        arr[0][i] = s2[i-2]
    
    
    # Fill second row by adding mismatch value
    for row in range(1, len(s1)+2): 
        arr[row][1] = ''
        if row == 1:
            mat[row][1] = 0
        else:
            mat[row][1] = mat[row-1][1] + mismatch

    
    # Fill second column by adding mismatch value
    for row in range(1, len(s2)+2):  
        arr[1][row] = ''
        if row == 1:
            mat[1][row] = 0
        else:
            mat[1][row] = mat[1][row-1] + mismatch
   
    
    # Fill rest of the matrix using the rules
    for i in range(2, len(s1)+2):
        for j in range(2, len(s2)+2):
            
            # Get value of diag based on match of corresponding characters
            diag = None
            if s1[i-2] == s2[j-2]:
                diag = ('tl', mat[i-1][j-1] + match)
            else:
                diag = ('tl', mat[i-1][j-1] + mismatch)
            
            # Get value for top, and left
            top = ('t', mat[i-1][j] + gap)
            left = ('l', mat[i][j-1] + gap)
            
            # Set max of the three as the final value
            vals = [diag, top, left]
            mat[i][j] = max(vals, key=lambda x: x[1])[1]
            
            arrows = [item for item in vals if item[1] == max(vals, key = lambda x: x[1])[1]]
            arr[i][j] = [dir[0] for dir in arrows]
      
    # Return the formed matrix
    return mat, arr


# In[2]:


def print_arr(mat, space):
    for row in mat:
        print(' '.join([str(item).rjust(space) for item in row]))


# In[3]:


def get_strings(str1, str2, mat, arr, final_list):
    s1 = list(str1)
    s2 = list(str2)
    
    m = len(s1) + 1
    n = len(s2) + 1
    return get_string_recur(s1, s2, mat, arr, [], m, n, final_list)


# In[10]:


# def get_string_recur(s1, s2, mat, arr, lcs, m, n, final_list):
# #     print(''.join([x[0] for x in lcs]))
#     if m<2 or n<2:
#         final_list.append([lcs])
#         print("FINAL STRING:",''.join([x[0] for x in lcs]))
#         for seq in final_list:
#             print(seq)
#             print()
#         return final_list
#     else:
#         d = arr[m][n]
#         fin = []
#         if len(d) > 1:
#             print("SPLIT:", m-2, n-2)
#         if 't' in d:
#             lcs.append(('-', mat[m][n]))
#             f = get_string_recur(s1,s2,mat, arr, lcs, m-1, n, final_list)
#             fin = fin + [*f]
#         if 'tl' in d:
#             lcs.append((s1[m-2], mat[m][n]))
#             f =  get_string_recur(s1,s2,mat, arr, lcs, m-1, n-1, final_list)
#             fin = fin + [*f]
#         if 'l' in d:
#             lcs.append(('-', mat[m][n]))
#             f =  get_string_recur(s1,s2,mat, arr, lcs, m, n-1, final_list)
#             fin = fin + [*f]
#         return fin


# In[13]:


def DNA(str1, str2 = True, match = 1, mismatch = -1, gap = -1):

    mat, arr = make_matrix(str1, str2, match, mismatch, gap)
    final_list = []
    print_arr(mat, 2)
    print_arr(arr, 12)
#     print()
#     options = set()
#     final_list = get_strings(str1, str2, mat, arr, final_list)
#     for string in final_list:
#         comb = ''.join([x[0] for x in string])[::-1]
#         score = sum([x[1] for x in string])
#         options.add((comb, score))
    
#     for option in options:
#         print(option)


# In[14]:


DNA('GATTACA', 'GCATGCU', match = 1)

