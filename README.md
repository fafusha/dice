# Cee-lo
## Introductiction
There are many different dice games. Sometimes it takes many hours to finish a game. Computers allow us to simulate thousand of rounds of these dice games in the matter of seconds. This allows us to identify interseting features and traits about these games. These traits include: the number of turns it takes to play the round or the number of rounds it takes to have one player standing. Cee-lo is an interesting example of a dice game, it might take players an the entire night to finish, but with help of computers we can speed this process up.

## About
Cee-lo is a gambling game played with three six-sided
dice. There is not one standart set of rules, but there
are some constants that are hold true all the time, one
of which is the number fo dice - three. [Wikipedia](https://en.wikipedia.org/wiki/Cee-lo)

This specific implementation focuses on the Cee-lo
without a bank (Winner Take All). 

## Rules
In this version of the game, each round involves two or
more players of equal status. A bet is agreed upon and
each player puts that amount in the pile or pot. Each
player then has to roll a three dice at once, if a
player rolls one of the winning combinations in this case exactly
*4-5-6* or *trips* (three same numbers), that player is
eligible to claim the pot. If one the players is eligible
to claim the pot all other players have to roll the rice.
If one of the players rolls a winning combination the
eligible player loses the privilege to the pot, all
players add the bet to the pot and round starts over.
If none roll a winning combination, eligible player takes
the pot.  

## Interesting questions
There are many different questions that can be adressed about this game, some of which are:
- How long does it take to win a pot?
- What is the average winning pot size?  

Note that in order to anwsers these questions, we need to know, what time on average does a player take to make a turn and what is the bet. 
### How long does it take to win a pot?
![Plot 1](plot_time.png)
This graph illustrates the dependecy between the number of players and the average time length of the round. Real-life experiments showed that a player takes on average 15 seconds to complete a turn. This turn time in held constant in this simulation. Average time is calculated by simulating 1000 rounds of the game and caculating the mean value. It is reasonable to assume by looking at the graph that as the number of players incearses, the time to complete a round would grow exponentially.  

### What is the average winning pot size?
![Plot 2](plot_pot.png)
This graph depicts the dependecy between the number of players and the average winning pot size. For this game player bet is held constant at 0.05$. Average winning pot is calculated by simulating 1000 rounds of the game and calculating the mean value of it. By looking at the graph it is safe to assume that as the number of players incearses, the size of the winning pot would grow exponentially.


