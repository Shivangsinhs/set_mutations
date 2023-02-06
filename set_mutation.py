# Enter your code here. Read input from STDIN. Print output to STDOUT

number =int(input())
list1 = set(map(int,input().split()))
rep=int(input())
for i in range(rep):
    sr,number = input().split()
    list2 = set(map(int,input().split()))
    eval("list1.{0}({1})".format(sr,list2))
print(sum(list1))
