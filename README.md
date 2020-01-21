# Birthday-problem

Birthday problem is well-known problem in probability theory. The objective is to find the probability that some people in a room will have the same birthday. 

The problem is only solvable by a simplified assumption: that each day is equally likely for a birthday. For this reason, 29 Feb is excluded and there are 365 possible birthdays in a year.

The mathematical definition of the problem is as follows:
Find the probability P(A) that at least two people in the room have the same birthday. It is easier to calculate the probability that none of the people in the room have the same birthday, which is represented by P(A′) = 1 - P(A).

Now given the number of people n, we can use p(n) to denote the probability of at least two out of the n people having the same birthday. Similarly, it is easier to first calculate the probability p(n') that all n birthdays are different. 

p(n') = 1 * (1 - 1/365) * ... * (1 - (n'-1)/365)
 
The event of at least two of the n persons having the same birthday is complementary to all n birthdays being different. Therefore,

p(n) = 1 - p(n')

The codes provided are to calculate the probability of the birthday problem, given the number of people in the room. 
