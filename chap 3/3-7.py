a = ['aritra', 'swastik', 'hulo']
print(a[0] + ' you are invited')
print(a[1] + ' you are invited')
print(a[2] + ' you are invited')
print("hulo couldn't come")
a[2] = 'prantika'
print(a[0] + ' you are invited')
print(a[1] + ' you are invited')
print(a[2] + ' you are invited')
print('guys I found a bigger table')
a.insert(0, 'debdeep')
a.insert(2, 'beji')
a.append('bantu')
print(a[0] + ' you are invited')
print(a[1] + ' you are invited')
print(a[2] + ' you are invited') 
print(a[3] + ' you are invited')
print(a[4] + ' you are invited')
print(a[5] + ' you are invited')
print('sorry only 2 can come')
a.pop(0)
a.pop(0)
a.pop(0)
a.pop(0)
print(a)
print(a[0] + ' you are invited')
print(a[1] + ' you are invited')
del a[0]
del a[0]
print(a)