~~~~~~~~~~~~~
Conditionals
~~~~~~~~~~~~~

In Python the command:

```
from random import randint
```

Allows us to use random numbers in our program (just like the line "from p5 import *" allowed us to draw shapes)

After we write this line we can call "randint(a, b)" to get a random number in range [a, b].

Our starter program will use this function to paint the background green or red:

1. It defines a global variable called "color"

2. In setup() we give it a random value between 0 and 10

3. In draw() we check if the value is > 5 to know what color to use.

Look at the code in lines 14-17:

1. The structure is called "if". We have the word if followed by a condition

2. After an "if" statement the code will branch: either the first (then block) or second (else block) will happen according to the truthness of the condition.

3. Else block is optional

~~~~~~~
Now You
~~~~~~~

1. Can you change the program so it is more likely to get green?

2. More likely to get a red?

3. What happens if we move the line "color = randint(0, 10)" to the draw() method? why?

4. Can you make it flash slower?

5. Python has a special condition syntax that can check if a value is in range:

```
if 0 <= color < 5:
  pass
```

Meaning if color is larger or equal to zero AND smaller than 5. 

Use this syntax and have the program show sometimes a blue background also.


1. What happens if we remove line 7 ("global color") from setup function?

2. In a previous lesson we created a rectangle that moves all the way to the end of the screen. Use "if" to have the rectangle move back when it reaches the end

3. Use a random number to have the rectangle move at a random speed

4. Write a new program that will draw 3 rectangles, having ONLY 1 red rectangle and the other two grey

5. Draw two rectangles at two opposite sides of the screen and have them moving towards each other. Stop moving when they collide.
