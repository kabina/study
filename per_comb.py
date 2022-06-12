from itertools import permutations, combinations, combinations_with_replacement, product
data = [1,2,3,4]
cdata = list(map(lambda x : str(x), data))
cdata = "".join(cdata)
print(cdata)
l = list(permutations(data, 3))
print(f"permutation: size={len(l)} data={l}")
l = list(combinations(data, 2))
print(f"combinations: size={len(l)} data={l}")
l = list(combinations_with_replacement(data, 2))
print(f"combinations_with_replacement: size={len(l)} data={l}")
l = list(product(data, repeat=2))
print(f"product: size={len(l)} data={l}")
