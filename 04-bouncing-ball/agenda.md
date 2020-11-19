# Bouncing Ball

In this lesson we'll use everything we've learned so far to create a bouncing ball.

The bouncing ball will keep moving until it hits a wall, then change its direction until it hits another wall.

## Walls

First draw 4 walls: top, left, right and bottom

Use rectangle to draw the wall and give them a nice color

## Bounce

Now let's make the wall bounce:

1. How do you make the ball go in a different direction?

2. When should the direction change?

## Use an `if` and two new variables to make the ball bounce:

1. First create a variable named "speed_x" that will control the speed and direction of the ball on the X axis

2. Then create a variable named "speed_y" that will control the speed and direction of the ball on the Y axis

3. Play with the numbers and make sure you can make the ball go faster or slower or in any one direction

4. Now use an `if` - if the ball hits the right wall, its speed_x value should be inverted

5. If the ball hits the left wall, again speed_x should be inverted

6. If the ball hits top wall it should start to move down

7. And if the ball hits bottom wall it should start to move up

## Change Color When Hitting the wall

1. Now let's have some fun - when the ball hits a wall change its color

