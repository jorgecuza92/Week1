# NESTED JSON STRUCTURE

geo = {'lat': '-35.2323', 'long': '81.2323'}

address = [{'street': 'Kulas light', 'suite': 'Apt. 445', 'city': 'houston', 'zip': 77007, 'geo': geo}]

nesting = [{'id': 1,
           'name': 'Leanne Graham',
           'username': 'Bret',
           'email': 'Sincere@blah.com',
           'address': address
           }]

print(nesting)






