def print_numbers(n):
    print n
    n-=1
    if n:
        print_numbers(n)
    n+=1
    print n
print_numbers(5)
  