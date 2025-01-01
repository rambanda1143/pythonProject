
def sorted_squares(arr):
    n=len(arr)
    left , right =0 , n-1
    result=[0]*n
    pos=n-1


    while left <=right:
        left_square=arr[left]**2
        right_square=arr[right]**2
        if left_square >right_square:
            result[pos]=left_square
            left+=1
        else:
            result[pos] = right_square
            right -= 1
        pos -= 1
    return result



arr=[-12, -8, -7, -5, 2, 4, 5, 11, 15]
print(sorted_squares(arr))