doctors = {
    'artie' : 'neju',
    'bb' : 'baby'
}

query = input('Enter your query').strip().lower()

if query.startswith('who'):
    for doctor in doctors.keys():
        print(doctor)

if query.startswith('is'):
    for doc in doctors:
        print(doc, doctors.get(doc))
