'''b)	As second task: you have the list of symbols (example: a, b, c, c, a (it’s very primitive)).
You should write function that returns the first repeating element from this list (in our example it’s “c”).'''

def repeat(ls):
    previous = None
    for current in ls:
        if current == previous:
            return current
        previous = current
print(repeat([16, 1, 18, 19, 20, 1, 18, 'c', 'c', 'b', 'c']))
