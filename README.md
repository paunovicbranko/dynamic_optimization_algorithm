In a cognitive radio network, the network controller autonomously allocates 200 MHz of unlicensed frequency spectrum to interested users.
Before the spectrum is assigned, each user informs the controller about the bandwidth in MHz required for communication and the amount of
money they are willing to pay for spectrum usage. Initially, the controller allocates the spectrum to a group of users that allows maximum
revenue collection. Users without spectrum allocation have the option to gamble with the controller to increase their financial amount and
become more competitive.

A user initially without spectrum allocation is allowed to participate in 4 rounds of gambling, with a 0.3 probability of receiving spectrum
allocation after gambling. The spectrum will be allocated if the user earns more money during gambling than a user with the same or larger
spectrum. The probability of losing the invested money during each gambling round is 0.5. After the gambling rounds conclude, the controller
recalculates the spectrum distribution.

Users who have not obtained the desired spectrum after the redistribution are allowed to gamble under the same conditions. The gambling and
redistribution process ends when there are no more interested users willing to gamble for spectrum or when the number of redistributions
exceeds a predefined limit.

Write a program in the selected programming language that simulates the process of allocating frequency spectrum. Given a table of data
(user, desired spectrum, money) and a maximum of N=5 spectrum recalculations by the controller, the program should output the final spectrum
allocation for each user. Test the program with a randomly chosen scenario.

Assign a counter to each operation in the algorithm, then run the program for a different number of users (choosing user parameters and the
assigned spectrum randomly). Graphically represent the dependency of the number of operations on the number of users in the range from 5 to 50 users.
