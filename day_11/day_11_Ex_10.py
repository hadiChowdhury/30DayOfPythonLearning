def capitalize_list_items(lst):
    upper_lst = []
    for item in lst:
         upper_lst.append(str(item).capitalize())
    return upper_lst
print(capitalize_list_items(['am', 'ball', 'cat', 'door', 'eyes']))
