def key(pair):
    return pair[0]

def lookup(given_key, set_of_records):
    if not set_of_records:
        return False
    if given_key == key(set_of_records[0]):
        return set_of_records[0][1]
    else:
        return lookup(given_key, set_of_records[1::])
    
data_base = [['Mickle', 12], ['John', 13], ['Alex', 14]]
print(lookup('Mickle', data_base))