# Factor_Tree
Input a number and it will give you the prime factor list and a tree traversal of the values used to make the number.
Tree is outputted as:

      Initial Value
        /      \
        Prime   Multiple
                  /   \
                Prime  Multiple
           etc etc

# The Files
1. **factorize.py** - Makes a list of primes and writes it to *primes.txt*
2. **primes.txt** - Has the list of primes
3. **factortree.py** - grabs the primes from primes.txt and takes in a value from cmd. This value is then used to generate the prime factor list, and the tree.

# Current Problems
* Primes numbers are between 2 and 100,000. Mostly because it took a while to do a million so I decided to go with a smaller number. Possible fixes involve having an L and R pointer that get closer to each other, halving the inner loop's time complexity.
* Tree look ugly. Need to fix because right now it's just newlines

## To Do:
- [ ] Make tree pretty
- [ ] Optional adjust the length of the prime list.
