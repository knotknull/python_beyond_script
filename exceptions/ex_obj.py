
# Atomic Numbers

nobles = {'He': 2, 'Ne': 10, 'Ar': 18, 'Kr': 36, 'Xe': 54}


def show_element_info(element):
    print('Atomic number of {} is {}'.format(element, nobles[element]))

for element in ['Ne', 'Br', 'Ar']:
    try:
        show_element_info(element)
    except KeyError as err:
        missing_element = err.args[0]
        print('<< Missing data for element: ' + missing_element + ' >>')
