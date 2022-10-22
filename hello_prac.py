people = [{'name': 'bob', 'age': 27},
          {'name': 'carry', 'age': 30}]


def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
        return '해당하는 이름이 없습니다'


print(get_age('bob'))
