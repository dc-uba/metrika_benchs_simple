import re
from bench_suites import python_suite

# Experiment reading measures from a generated file instead of using internal python timer


def configure(engine):
    suite = python_suite()
    setup = engine.organize_experiment(suite, 'join-perf-time')
    setup.invoke_with_command(lambda program, size, version:
                              '/usr/bin/time -v python%d -c "%s" >output' % (version, program % size))
    setup.measure_parsing_file('secs', parse_cpu, "output")
    setup.measure_parsing_file('mem(KB)', parse_mem, "output")
    setup.set_report(report_values, 'time and mem(KB)', 'performance of join when using distinct types of objects')
    setup.set_plotter(plot, 'str vs list', 'performance of join when using distinct types of objects')

def plot(plotter, name, i):
    plotter.group_by('size')
    plotter.plot_boxes('times-time-boxes')
    plotter.plot_bars('times-time-bars')

def report_values(reporter):
    reporter.add_column('contender', lambda contender, _: contender['program'].name, 10)
    reporter.add_column('python', lambda contender, _: contender['pyver'].value())
    reporter.add_column('input', lambda contender, _: str(contender['size']), 12)
    reporter.add_common_columns()
    reporter.sort_by(lambda row: (row[2], row[3]))


def parse_cpu(file):
    f = "[-+]?(\d+([.,]\d*)?|[.,]\d+)([eE][-+]?\d+)?"  # float_regexp
    contents = file.read()
    return float(re.search("User time \(seconds\): (%s)" % (f), contents).group(1))


def parse_mem(file):
    contents = file.read()
    return int(re.search("Maximum resident set size \(kbytes\): (\d+)", contents).group(1))

