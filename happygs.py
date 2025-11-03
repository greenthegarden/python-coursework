def check_all_gs_happy(string_to_check):
    """
    Check if all 'g' and 's' in the string are happy.
    A 'g' is happy if it is followed by another 'g' or an 's'.
    An 's' is happy if it is followed by another 's' or a 'g'.
    """
    string_as_list = list(string_to_check)
    for chararacter in range(len(string_to_check)-1):
        print(string_as_list[chararacter])
        print(string_as_list[chararacter+1])
        print(string_as_list[-1])
        print(string_as_list[-2])
        if string_as_list[chararacter] ==  'g' and string_as_list[chararacter+1] !=  'g' or string_as_list[-1] ==  'g' and string_as_list[-2] !=  'g':
            return "Lonely"
    else:
        return "Happy"

test_string = "xggt"
answer = check_all_gs_happy(test_string)

print(f"Is the string '{test_string}' happy? {answer}")
