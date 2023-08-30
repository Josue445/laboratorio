persona = {
        'first_name': 'Edem',
        'last_name':'Terraza',
        'age': 31,
        'country': 'Perú',
        'is_married': True, #
        'skills': ['JavaScript', 'React','Node','MongoDB','python'],
        'address':{
            'street': 'Space street',
            '<ipcode':'02210'
                }
}

#a
print("-------------a-----------")
print("-------------a-----------") 
print(persona['skills'][2])

#b
print("-------------b-----------")
print("-------------b-----------")
for clave in persona:
    if clave == 'skills':
        for skills in persona['skills']:
            print(skills)

if 'python' not in persona['skills']:
    print("NO esta")
else:
    print("SÍ esta")

print(persona['skills'])


print("------------c------------")
print("------------c------------") 