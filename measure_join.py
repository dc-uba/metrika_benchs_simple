# Example of benchmarking join: iterator of strings vs lists of strings

from bench_suites import simple_suite


def configure(engine):
    suite = simple_suite()
    setup = engine.organize_experiment(suite, 'join-perf')
    setup.invoke_with_command(lambda program, size: 'python -c "%s"' % (program % size))
    setup.measure_execution_time()
    setup.set_report(report_run_time, 'run-time', 'performance of join when using distinct types of objects')
    setup.set_plotter(plot, 'str vs list', 'performance of join when using distinct types of objects')


def report_run_time(reporter):
    reporter.add_column('contender', lambda contender, _: contender['program'].name)
    reporter.add_column('input', lambda contender, _: str(contender['size']), 14)
    reporter.add_common_columns()
    reporter.sort_by(lambda row: (row[1], row[2]))


def plot(plotter, name, i):
    plotter.group_by('size')
    plotter.plot_boxes('times-python')

# example of how to run:
# $> python -m metrika run -x join-perf size=test
