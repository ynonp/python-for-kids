# Randomization

1. We have learned to place objects in different colors and move them according to some pattern.
   But sometimes, we want to be "surprised". We do not want the same predictable result
   over and over again. Imagine a computer game in which the level is always the same.

2. Introducing the concept of randomization. p5 has random_uniform for this purpose.
   The parameters are 'upper limit', 'lower limit'.

3. Can you place a random color object in the work area center? Now make it change colors at random.

4. Place the aforementioned object at random locations in the work area.


# Mouse Clicks

1. Recall that we learned to "catch" a key press. We shall now catch a mouse click
   using a condition on the special variable mouse_is_pressed. Then we capture the
   coordinates of the click in the 'mouse_x' and 'mouse_y' special variables.

2. Use Python's print() method to log the x and y coordinates of your clicks.

3. Place a shape at the origin (0,0) and then slowly move it to the click location.


# Advanced Setups and Homework

1. Every time a mouse click takes place, move a circle to the click location from a random
   location on the work area border. Control the speed of movement as you wish.
   
2. Develop a game: bombs (circles) drop randomly from the top of the work area
   and using clicks you fire missiles (rectangles) from the bottom of the work area to intercept them.
   If you hit - the bomb is destroyed.