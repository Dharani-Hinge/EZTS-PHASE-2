#Implementation of forest(Implementation of trees)
Families={
           'Shivani':
                   { 'Bhavana':{'Mithra','Srinidhi'},
                     'Shreshta':{'Sadhvi','Gayatri'}},
           'Ananya':
                   {'Yochana':{'Ankitha'},
                    'Teja Sree':{'Anuhya'},
                    'Dharani':{'Swapna'}},
           'Anuhya':
                   {'Preethi':'Ravalika','Madhu':'Sreenija'}
           }
for Parent,Children in Families.items():
    print(f"{Parent} has {len(Children)} kids:")
    print(f"{',and '.join([str(Child) for Child in [*Children]])}")