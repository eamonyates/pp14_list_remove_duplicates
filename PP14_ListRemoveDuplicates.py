import random


a = [1,1,1,2,3,4,5,6,7,8,8,8,8,8,2,3,5,4]
print (sorted(a))


def remove_duplicates_set(list1):
	set_list = set(list1)
	print (sorted(set_list))


def remove_duplicates_loop(list1):
	non_dup = []
	for num in list1:
		if num not in non_dup:
			non_dup.append(num)
	print (sorted(non_dup))


if __name__ == "__main__":
	remove_duplicates_loop(a)
