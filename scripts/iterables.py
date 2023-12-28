# [[file:learnings.org::*Size comparison][Size comparison:1]]
import sys
import array

# small

s_arr = array.array('i', [134587, 234589, 33542])
s_lst = [134587, 234589, 33542]
s_tup = (134587, 234589, 33542)

print(f"""
Small Array:{sys.getsizeof(s_arr)}
Small List: {sys.getsizeof(s_lst)}
Small Tuple: {sys.getsizeof(s_tup)}
""")

# medium_with_listcomp

m_arr_lc = array.array('i', [i for i in range(1, 1000000, 10)])
m_lst_lc = [i for i in range(1, 1000000, 10)]
m_tup_lc = tuple([i for i in range(1, 1000000, 10)])

print(f"""
Medium List Comp Array:{sys.getsizeof(m_arr_lc)}
Medium List Comp List: {sys.getsizeof(m_lst_lc)}
Medium List Comp Tuple: {sys.getsizeof(m_tup_lc)}
""")

# medium_with_genexp

m_arr_exp = array.array('i', (i for i in range(1, 1000000, 10)))
m_lst_exp = [(i for i in range(1, 1000000, 10))]
m_tup_exp = tuple(i for i in range(1, 1000000, 10))

print(f"""
Medium GenExp Array:{sys.getsizeof(m_arr_exp)}
Medium GenExp List: {sys.getsizeof(m_lst_exp)}
Medium GenExp Tuple: {sys.getsizeof(m_tup_exp)}
""")

# large_with_listcomp

l_arr_lc = array.array('i', [i for i in range(1, 10000000, 2)])
l_lst_lc = [i for i in range(1, 10000000, 2)]
l_tup_lc = tuple([i for i in range(1, 10000000, 2)])

print(f"""
Large List Comp Array:{sys.getsizeof(l_arr_lc)}
Large List Comp List: {sys.getsizeof(l_lst_lc)}
Large List Comp Tuple: {sys.getsizeof(l_tup_lc)}
""")

# large_with_genexp

l_arr_exp = array.array('i', (i for i in range(1, 10000000, 2)))
l_lst_exp = [(i for i in range(1, 10000000, 2))]
l_tup_exp = tuple(i for i in range(1, 10000000, 2))

print(f"""
Large GenExp Array:{sys.getsizeof(l_arr_exp)}
Large GenExp List: {sys.getsizeof(l_lst_exp)}
Large GenExp Tuple: {sys.getsizeof(l_tup_exp)}
""")
# Size comparison:1 ends here

# [[file:learnings.org::*Unpacking 1:1][Unpacking 1:1:1]]
one, two = (123.0934, 21340.0435)
print({one})
# Unpacking 1:1:1 ends here

# [[file:learnings.org::*Unpacking larger iterable than variable count"][Unpacking larger iterable than variable count":1]]
tuple = (1, 2, 3, 4, 5, 6, 7)
one, two, *others = tuple

print(f"one: \t {one} \n two: \t {two} \n others: \t {others} \n")
print(f"Type from tuple: \n \t {type(tuple)} \n Type from others: \n \t {type(others)} ")

print(*range(5))

try:
    print(type(*range(5)))
except Exception as e:
    print(e)

print([*range(8)])

print(type([*range(80)]))
# Unpacking larger iterable than variable count":1 ends here

# [[file:learnings.org::*Pattern matching][Pattern matching:1]]
items = [
    ["pat", 2, 'tesqwert', 'casdfase', (3, 4, 5, 6)],
    ["nev",3, 'tesqwert', 'cabasse', (3.3, 4.5, 5.2, 6.5, 9.1)],
    ["pat", 4, 'tewqerst', 'cawegasse', (3.44, 4.33, 5, 6, 6, 6)],
    ["nev",5, 'teqwerst', 'caasdasdse', (3.23, 4, 5, 6)],
    ["pat", 6, 'teswert', 'casasbdasde', (3, 4, 5, 6)],
    ["pat", 23, 'tadsfest', 'casdbase', (3, 4, 5, 6)],
    ["nev", 22, 'teswert', 'casasdbdsabe', (3.3, 4.6, 5.3, 6.6)],
    ["never", 'tasdfest', 'caswere', (3.0, 4.2, 5.6, 6.8)],
]

for item in items:
    match item:
        case ["pat", int(x), _, _, (v1, v2, v3, v4)]:
            print(item)
        case ["nev", _, str(t1), str(t2), *_]:
            print(f"nev: {t1} \t \t {t2}")
        case [*_, t as tail]:
            print(tail)
# Pattern matching:1 ends here

# [[file:learnings.org::*double loop in generator/comprehension][double loop in generator/comprehension:1]]
lisT = [t for t in range(10) for i in range(5)]
print(lisT)
# double loop in generator/comprehension:1 ends here

# [[file:learnings.org::*Advanced silcing][Advanced silcing:1]]
word = "pineapple"

# non overlapping ranges
print(word[:4], word[4:])

# diffenent steps

print(word[::2])

# easy reverting
print(word[::-1])

multi = [[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]]

print(multi[1][0])
print(multi[0][1])

print(multi[0][1:2])
# Advanced silcing:1 ends here
