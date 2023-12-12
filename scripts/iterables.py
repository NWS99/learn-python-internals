import sys
import array

# small

arr_s = array.array('d', [134587.09, 234589.40, 33542.14])
lst_s = [134587.09, 234589.40, 33542.14]
tup_s = (134587.09, 234589.40, 33542.14)

print(f"""
Small Array:{sys.getsizeof(arr_s)}
Small List: {sys.getsizeof(lst_s)}
Small Tuple: {sys.getsizeof(tup_s)}
""")

# large

arr_l = array.array('d', [i for i in range(1, 1000000, 13)])
lst_l = [i for i in range(1, 1000000, 13)]
tup_l = (i for i in range(1, 1000000, 13))

print(f"""
Large Array:{sys.getsizeof(arr_l)}
Large List: {sys.getsizeof(lst_l)}
Large Tuple: {sys.getsizeof(tup_l)}
""")
