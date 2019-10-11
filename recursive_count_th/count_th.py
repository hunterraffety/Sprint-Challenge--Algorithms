'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    print(f"the word: {word}")
    print(f"length: {len(word)}")
    if len(word) < 2:  #base case
        print(f"not long enough")
        return
    else:
        print(f"long enough")  #invoke recursion here
        count_th(f"reinvokation of count_th: {word}") #generates infinite loop when a word longer than 2 is entered
        pass
    # TBC <-- what does this mean?
    # initial thoughts
    # cant use a for loop
    # 
    
    pass

#print(count_th(""))
print(count_th("thehehethht"))
#print(count_th("THththeeeee"))
