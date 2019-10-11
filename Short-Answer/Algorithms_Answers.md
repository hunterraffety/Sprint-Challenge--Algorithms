#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

O represents the function. the n represents the number of elements.

a) this item i think is O(n^2). I believe so because the results of it execution time depends on the comparisons for the end case, where a is finally equal to a + -n squared-. this requires multiple iterations to hit the end case. It could be O(n^5) maybe(?) because I think no matter what, it's quadratic, and that's the "classification" this would get. I've never seen the O(n^5) notation though. So, probably very wrong.

b) the fact this is a loop within a loop says to me that this is O(n^2) based on what i've read especially in the big-o cheat sheet. this requires the calculations to be dependent on multiple loops that are being affected by j incrementing until it hits whatever the input of n is for the initial loop while simultaneously being incremented in the first loop as well as multiplied in the second loop. This would be a quadratic big O function given my description of my answer.

c) this is O(n). it is linear because the direct result of the timing of it depends on the size of n. in other words, the amount of time this takes is directly correlated to the size of whatever it eats up.

## Exercise II

This sounds like a divide and conquer question to me.

Suppose I dropped an egg off of an unknown size building. I'm going to make the building concrete in my head. I will suggest that it's 10 stories high.

# Suppose also that an egg gets broken if it is thrown off floor f or higher

If I drop an egg off of floor 10 as a test case and it breaks:

# and doesn't get broken if dropped off a floor less than floor f

I'd go ahead and try to drop it off of floor 5 and it doesn't break:

I know that I can repeat my logic by going up to floor 9 and testing if it breaks, and if it does, I can go to floor 6. If it doesn't break, I can go up to floor 8, and it if breaks, I can go to floor 7 and hopefully find it doesn't break there because it didn't on floor 5 or 6, but it did on 8, 9, and 10 -- but NOT 5 or 6. Therefore if my logic is correct, I'd not expect the egg to break on floor 7 because there is no 6.5 in the building.

The idea is that I am dividing my sides and whittling them down in between each iteration. I think at least. It makes sense in my head.
