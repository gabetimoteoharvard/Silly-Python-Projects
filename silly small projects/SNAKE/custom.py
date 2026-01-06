class CustomFunctions:
    def __init__(self):
        self.name = None

    @staticmethod
    def array_in_array(arr_1, arr_2):
        for arr in arr_2:
            if arr[0] == arr_1[0] and arr[1] == arr_1[1]:
                return True
        return False

    @staticmethod
    def equal_array(arr_1, arr_2):
        for i in range(len(arr_1)):
            if arr_1[i] != arr_2[i]:
                return False
        return True

    @staticmethod
    def append_arr(arr_1, arr_2):
        ans = arr_1
        for arr in arr_2:
            ans.append(arr)
        return ans

    
