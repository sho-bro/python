curr_users = ['bro', 'john', 'beji', 'nyeku', 'mac']
new_users = ['JOHN', 'Mac', 'chandu']
for a in new_users:
    for b in curr_users:
        if a.lower() == b.lower():
            print('this username is not available')
print(a + ' available')     