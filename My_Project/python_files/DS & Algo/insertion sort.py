def insertion_sort(arr, n):
	for i in range(1, n):

		## current position and element
		current_position = i
		current_element = arr[i]

		## iteratin until
		### it reaches the first element or
		### the current element is smaller than the previous element
		while current_position > 0 and current_element < arr[current_position - 1]:
			## updating the current element with previous element
			arr[current_position] = arr[current_position - 1]

			## moving to the previous position
			current_position -= 1

		## updating the current position element
		arr[current_position] = current_element

if __name__ == '__main__':
	## array initialization
	arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
	insertion_sort(arr, 9)

	## printing the array
	print(str(arr))