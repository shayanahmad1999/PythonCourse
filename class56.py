# zip
nums = '1234'
letters = ['a', 'b', 'c', 'd']
names = ['John', 'Eric', 'Michael', 'Graham', 'Joe']
combo = list(zip(nums,letters,names))
print(combo)

# unzip
num,let,nam = zip(*combo)
print(num,let,nam)

# zip dict

keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'
keys = keys.split()
values = values.split()
print(keys,values)
en_sv_dict = dict(zip(keys,values))
print(en_sv_dict)
new_dict = {key:value for key,value in zip(keys,values)}
print(new_dict)

# unzip dict

en,sv = list(en_sv_dict.keys()),list(en_sv_dict.values())
print(en,sv)
en1,sv1 = zip(*en_sv_dict.items())
print(en1,sv1)