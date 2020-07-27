'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# count how many times the lowercase 'th' occurs in every string.
# create a counter for every string.
# i = 0
# i2 = 1
# count = 0

def count_th(word, i = 0, i2 = 1, count = 0):
    arr = list(word)

    if len(arr) == 0:
        return count

    if i2 > len(arr) - 1:
        return count

    if arr[i] == 't' and arr[i2] == 'h':
        count += 1
        i += 1
        i2 += 1
        return count_th(word, i, i2, count)
    else:
        i += 1
        i2 += 1
        return count_th(word, i, i2, count)





word = 'abcthxyzththtth'

print(count_th(word))


    # substring = 'th'
    # count = word.count(substring)

    # return count
