from re import I


def encrypt(word):
    rev = word[::-1]                    #reverse input
    vow = {"a": "0", "e": "1",
        "i": "2", "o": "2",
        "u": "3"}
    
    for n in vow:
        rev = rev.replace(n, vow[n])
        #########################################################
        #tried this first, didnt work b/c i and o need to have same value...
        # if n in vow:                    #if nth letter is vowel
        #     ans += str(vow.index(n))    #add its index value to the output
        # else:
        #     ans += n                    #if nth letter isnt a vowel, add letter to the answer
    
    return rev + "aca"