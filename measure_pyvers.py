
# Example of measuring python2 vs python3

from bench_variations import python_suite

def configure(engine):
    suite = python_suite()
    setup = engine.organize_experiment('py2-vs-py3', suite)
    setup.invoke_with_command(lambda program, size, version: 'python%d -c "%s"' % (version, program % size))
    setup.measure_execution_time()
