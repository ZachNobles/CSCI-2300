(1) Consider the following pseudocode of a function which takes an integer n ≥ 0 as input.
```
Function foo(n)
  if n == 0 then
    Return;
  end

  for i = 0 to n − 1 do
    Print ’*’;
  end
  foo(n − 1);
  ```
Let T(n) be the number of times the above function prints a star (*) when called with input n ≥ 0.
What is T(n) exactly, in terms of only n (and not values like T(n − 1) or T(n − 2))? Prove your statement.

---

(2) Same as Problem 2 above, but for the following:
```
Function bar(n)
  Print ’*’;
  if n == 0 then
    Return;
  end
  for i = 0 to n − 1 do
    bar(i);
  end
```
