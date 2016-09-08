
from metrika.suite import Suite

programs = {
    'str': "'-'.join(str(n) for n in range(%d))",
    'list': "'-'.join([str(n) for n in range(%d)])"
}

sizes = {'test': 10, 'small': 10000, 'big': 1000000}

versions = [2, 3]


def simple_suite():
    suite = Suite()
    suite.add_variable_from_dict('program', programs)
    suite.add_variable_from_dict('size', sizes)
    return suite


def python_suite():
    suite = simple_suite()
    suite.add_variable_from_list('pyver', versions)
    return suite

