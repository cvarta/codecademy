import itertools

def main():
	m = [1, 2, 3]
	n = [4, 5, 6]

	print join_lists(m, n)
	print join_lists2(m, n)
	print join_lists3(m,n,n)

def join_lists(x,y):
    return x + y
	
def join_lists2(x,y):
	return list(itertools.chain(x,y))
	
	
def join_lists3(*lists):
	return list(itertools.chain(*lists))


if __name__ == "__main__":
  main()
