Note to myself:

Create a nth term function

references:
https://www.reddit.com/r/adventofcode/comments/18e9n1q/2023_day_9_challenge_find_the_10_000_000th_term/
https://www.reddit.com/r/adventofcode/comments/18e8dua/2023_day_9_easy_bake_derivatives/

One way:

1 3 6 10 15 21
2 3 4 5 6
1 1 1 1

One observation i can see is that,

6 = 2 + 4(1)
and 21 = 2 + (3 + 4 + 5 + 6)

So i can use this to find general term, where if i want to know 7th term of second sequence

7th = 2 + (1 + 1 + .. 6 times) = 2 + 6 = 8

and now 8th term of first sequence:

8th = 1 + (2 + 3 + 4 + 5 + 6 + 7 + 8) = 36

1 3 6 10 15 21 28 36
2 3 4 5 6 7 8
1 1 1 1
