m = [1, 2, 3]
n = [4, 5, 6]
o = [7, 8, 9]

# Update the below function to take
# an arbitrary number of arguments
def join_lists(*x):
    new = []
    for i in x:
        new += i
    return new

print join_lists(m, n, o)
