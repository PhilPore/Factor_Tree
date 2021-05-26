import sys
import math

class Tree_Node:
    def __init__(self, val):
        self.val = val
        self.left = None #this will be the prime
        self.right = None #always move down this way
        

class Bin_Tree:
    def __init__(self, head):
        self.root = head
    def In_Order(self,head):
        #trav = head
        print(head.val)

        if head.left:
            self.In_Order(head.left)
        if head.right:
            self.In_Order(head.right)
        #padding = "" 
               

def make_fact_tree(prime_list, value, F_Tree):
    iteri = F_Tree.root
    factor_list = []
    factored_vars = None
    cur_val = value
    ind = 0
    print(f"Value sent in {value}")
    while cur_val > 1:
        prime_check = math.sqrt(cur_val)
        #print(f"prime check {prime_check}")
        #print(f"cur_val {cur_val}")
        for i in prime_list:
            if cur_val%i == 0:
                factor_list.append(i)
                cur_val//=i
                iteri.left = Tree_Node(i)
                iteri.right = Tree_Node(cur_val)
                iteri = iteri.right

                #print(f"In prime check. Vals cur: {cur_val} {cur_val*i} {i}")
                break
            if i > prime_check:
                factor_list.append(cur_val)
                cur_val/=cur_val
                break
        ind+=1
    print(f"Prime Factor list {factor_list}")

    return factor_list

arg1 = int(sys.argv[1])
r_file = open("primes.txt","r")
prime_list = r_file.read().split(",")
print(len(prime_list))
for i in range(len(prime_list)):
    prime_list[i] = int(prime_list[i])
#print(prime_list[-1])
Factor_Node = Tree_Node(arg1)
Factor_Tree = Bin_Tree(Factor_Node)
make_fact_tree(prime_list,arg1, Factor_Tree)
Factor_Tree.In_Order(Factor_Tree.root)
#print(type(prime_list[-1]))

