Note for myself:

Solve part2 of day 10

some references:
https://www.reddit.com/r/adventofcode/comments/18evyu9/2023_day_10_solutions/

Tweets:

- I completed part 2 this morning by zooming in and transforming each postion into a 3x3 grid, so I had all the non enclosed
  connected. Later this evening I remembered the even/odd rule and refactored
  |- I did the even/odd first but it only works
  for the tests... :( So I ended up scaling 3x3 ...
  |- I couldn't find a smaller failing test to debug. Also, I needed an
  actual working solution to make sure any tests were correct. And a visual one. So the 3x3 expansion solution gives us that.
  Once you have the visuals, I could bug-fix the first approach, but I was tired 😅

- It was a tough one today! I was glad to have spotted Part 2 can be solved with
  https://wikiwand.com/en/Jordan_curve_theorem which makes it 2 lines of numpy
  https://github.com/mattmcd/PyBayes/blob/dev/scripts/journal_20231201_aoc_day10.py#L146 (it took me a couple of hours of
  fiddling to get it working though)
