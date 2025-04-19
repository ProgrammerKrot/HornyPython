class Finder():
    def find_max_value(self, input_list):
        if not input_list:
            return None
        elif len(input_list) == 1:
            return 0

        maximum = 0
        i = 0

        while input_list:
            if input_list[i] > maximum:
                maximum = input_list[i]
            else:
                pass
            if len(input_list) > 1:
                del (input_list[i])
                i -= 1
            else:
                break
            i += 1
        return maximum


# Example usage:
input_list = [10, 25, 15]
call = Finder()
x = Finder.find_max_value(call, input_list)  # Output: 'b'
if x != 0:
    print(True)
    print(x)
else:
    print(False)