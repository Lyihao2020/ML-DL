# 返回字典

def build_person(first_name, last_name, age=''):
    person = {'firstname': first_name, 'lastname': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('Max', 'Steven', 20)
print(musician)
