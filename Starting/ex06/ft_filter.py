#!/usr/bin/env python3


def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true.
    """
    
    if function is None:
        for element in iterable:
            if element:
                yield element
    else:
        for element in iterable:
            if function(element):
                yield element

# nombres = [0, 1, 2, 3, 4, 5, False, None, "", "Python"]
# resultat = ft_filter(None, nombres)
# res = filter(None, nombres)
# print(resultat, list(resultat))  # Output: [1, 2, 3, 4, 5, 'Python']
# print(res, list(res)) 
# personnes = [18, 23, 42, 61, 88]
# 
# travailleurs = ft_filter(lambda age: age <= 62, personnes)
# tra = filter(lambda age: age <= 62, personnes)
# print(travailleurs, list(travailleurs))
# print(tra, list(tra))
# 
# personnes = [{
#   'nom': 'Bertrand',
#   'age': 32
# }, {
#   'nom': 'François',
#   'age': 60
# }, {
#   'nom': 'Thomas',
#   'age': 30
# }, {
#   'nom': 'Loïc',
#   'age': 9
# }]
# 
# majeurs = ft_filter(lambda personne: personne['age'] >= 18, personnes)
# maj = filter(lambda personne: personne['age'] >= 18, personnes)
# print(majeurs,list(majeurs))
# print(maj,list(maj))
