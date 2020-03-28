# Brainf\*ck;

Additional features:
- `:`: Print memory value as interger (not string as in the original Brainf\*ck)
- `;`: Read standard input as interger (not string as in the original Brainf\*ck)

Fibonacci number example. Input:
```
python brainfck.py "
>++++[-<+++++++++++>]<>
+:<.>>+:<<.>>
[<[->>>+<<<]>[->+>+<<]>>:
<<<<.>>>>
[-<<+>>]<[-<<+>>]<]
"
```
Return:
```
1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025...
```
