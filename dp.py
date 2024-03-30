def longestCommonPrefix(strs):

    i = 0
    char = strs[0][i]    # 'f'

    for idx, s in enumerate(strs):
        if s[i] != char:
            return strs[0][:i-1]
        i += 1
    
    return strs[0]
