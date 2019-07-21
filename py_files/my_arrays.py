a = [4]

def list_empty(list_):
    if list_:
        return False
    else:
        return True
    
if list_empty(a):
    print('empty')
else:
    print(a)