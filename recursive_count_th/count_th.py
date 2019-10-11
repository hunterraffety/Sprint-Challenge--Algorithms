'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#cache to hold words
cache = []
print(f"cache length outside: {len(cache)}")
def count_th(word):
    #count = 0
    #print(f"the word: {word}")
    #print(f"length: {len(word)}")
    if len(word) < 2:  #base case
        #print(f"not long enough")
        return
    elif word[0:2] == "th":  # needs to be elif
        # add word to cache here?
        cache.append(word[0:2])
        #print(f"word after check: {word} {len(word)}")
        #word is still word after slicing off the matching th.
        #need to store the remainder of the word in order to run it recursively through the function? what happens if the first two letters coming up next are NOT "th"?
    leftover_word = word[1:]
    print(f"leftovers: {leftover_word}")
    print(f"cache length inside: {len(cache)}") # wont print under "" test case -- only when it passes
    #print(f"long enough")  #invoke recursion here
    count_th(leftover_word)  #generates infinite loop when a word longer than 2 is entered
        # lol fires off infinitely til: RecursionError: maximum recursion depth exceeded while calling a Python object
    return len(cache)
    # TBC <-- what does this mean?
    # initial thoughts
    # cant use a for loop
    # i can check the first two letters for "th" using slice, and then begin the offset of checking every two letters through the recursion until it reaches the end of the word
    # it will only look for "th" and ignore everything else out outside of the first two letters because of slice
    # i should use a cache list and append the found "th" in it instead of a count and just return the length of the cache len(cache)
    pass

#print(count_th("")) #exit #### exits
#print(count_th("thehehethht")) #this has 2 #### prints 2

print(count_th("THththeeeee")) #this has 1 TH but only 2 lower #### prints 2
#print(count_th("asdsfasghgasheeeee")) # this has 0 #### prints 0
