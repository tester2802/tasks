# numbers = range(10)
# squared_evens = [n ** 2 for n in numbers if n % 2 == 0]
# print(squared_evens)   # [0, 4, 16, 36, 64]

sequence = [1,4,7,1,0,3,5]
for idx, item in enumerate(sequence):
	print(idx,idx*2, idx%2)