class ArrayLeftRotation:

    # Longer but easier on the memory
    def array_left_rotation1(self, a, arr_length, shifts):
        for _ in range(shifts):
            index = arr_length - 1
            next_val = a[index]
            while index >= 0:
                index_to_move_to = (index - 1 + arr_length) % arr_length
                temp = a[index_to_move_to]
                a[index_to_move_to] = next_val
                next_val = temp
                index -= 1
        return a

    def array_left_rotation2(self, a, arr_length, shifts):
        arr = [None] * arr_length
        for index in range(arr_length):
            index_to_move_to = (index - shifts + arr_length) % arr_length
            arr[index_to_move_to] = a[index]
        return arr
