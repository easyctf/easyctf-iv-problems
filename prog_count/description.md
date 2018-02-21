Given a set of numbers, print out how many non-empty subsets sum to a given integer.

### Input Format
The first line contains two integers `N` and `S`. The second line contains `N` space-separated integers `a_1, a_2, ..., a_N`.

`1 <= N <= 20`

`-100 <= S <= 100`

`-1000 <= a_i <= 1000`

### Output Format
A single integer, the number of non-empty subsets which sum to `S`. Two subsets are different if an element appears in one and does not appear in the other. Note that `a_1` is distinct from `a_2`, even if their values are identical.

### Sample Input
```
6 5
2 4 1 1 1 2
```

### Sample Ouput
```
8
```