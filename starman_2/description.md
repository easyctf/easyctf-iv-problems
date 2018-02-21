Starman is back at it again! Having successfully brought back several hackers from the asteroid belt, he wants to eliminate the possibility of competition from the hackers he left behind. He has equipped his Roadster with an asteroid-destroying laser, but unfortunately he's only able to fire it once. Asteroids can be represented as points in a 2D plane. The laser, when fired, sends a beam of width `W` straight forward, and destroys everything in its path. Starman can go anywhere to fire his beam. It's expensive to fire wider beams, so your job is to find out the smallest possible width of the beam.

### Input Format
The first line contains a single integer `N`, representing the number of asteroids. The following `N` lines each contain two integers `x_i` and `y_i`, representing the `x` and `y` coordinates of the `ith` asteroid.

`3 <= N <= 200000`

`-10^8 <= x_i, y_i <= 10^8`

### Output Format
A decimal printed to six decimal places (including trailing zeroes; this can be accomplished using `printf` or your language's equivalent) representing the minimum possible value of `W`.

### Sample Input
```
5
12 4
-2 5
-8 -7
-1 -11
5 3
```

### Sample Ouput
```
11.234578
```
