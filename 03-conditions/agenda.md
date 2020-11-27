~~~~~~~~~~~~~
Conditionals
~~~~~~~~~~~~~

In python the command `if` creates a new program branch. If will check the condition, and if the condition is true will execute the block below it.

We use `if` to conditionally run parts of the program.

Let's continue to the starter code:

1. In what line is the `if` command?

2. Note the `:` at the end of that line. Everything between `if` and `:` is called the condition. What is the condition in the starter code?

3. Note the line after the `if` starts indented. This is called a block and will continue until the indentation ends. How many lines are there in our block?

4. Can you guess what the program does? Run it to verify

5. Move line 16 to appear below the if block, without changing the functionality of the program

6. Add inside the block a new line:

```
background(0,0,0)
```

What did it do? Can you see the flashing black background?

7. Move the new background line out of the block. What happened now? why?

-----------------------

1. Modify the code so the rectangle will change direction when it reaches the end, going back to the other side

2. Add a new `y` variable and have the rectangle move in diagonal. When it hits a right or left wall change its horizontal direction; when it hits top or bottom wall change its vertical direction

----------------------------

1. Create a second rectangle and have both rectangles change directions when they collide
