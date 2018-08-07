# The dict class allows creating an associative array
# of keysand values. Key must be unique immutable objects

empty_disc = dict()
print('empty_disc ->', empty_disc)
empty_disc = {}
print('empty_disc ->', empty_disc)

dict_syn = {'k1': 'v1', 'k2': 'v2'}
print('dict_syn ->', dict_syn)
dict_syn = dict(k1='v1', k2='v2')
print('dict_syn ->', dict_syn)
print("dict_syn['k2'] ->", dict_syn['k2'])
dict_syn['k3'] = 'v3'
print('dict_syn ->', dict_syn)

del(dict_syn['k3'])
print('dict_syn ->', dict_syn)

dict_syn['k1'] = 1
print('dict_syn ->', dict_syn)
dict_syn['k2'] = 1
print('dict_syn ->', dict_syn)

dict_ref = dict_syn
dict_copy = dict_syn.copy()
print('dict_syn ->', dict_syn)
print('dict_ref ->', dict_ref)
print('dict_copy ->', dict_copy)

key_list = dict_copy.keys()
print('key_list ->', key_list)
value_list = dict_copy.values()
print('value_list ->', value_list)

mapping = zip(key_list, value_list)
print('mapping ->', mapping)
dict_new = dict(mapping)
print('dict_new ->', dict_new)

print("'k3' in dict_new ->", 'k3' in dict_new)
print("'k3' in dict_new ->", 'k3' not in dict_new)

