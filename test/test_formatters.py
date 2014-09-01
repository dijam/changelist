from formatters import *
from nose.tools import assert_false, assert_true, assert_equal


test_files = {
    'README': 'Mon Aug 11 10:54:03 2014 +0200',
    'LICENSE': 'Mon Aug 11 10:54:03 2014 +0200'
}


def test_console():
    formatter = ConsoleFormatter()
    console_data = formatter.format(test_files)
    for filename, date in test_files.iteritems():
        assert_true(filename in console_data)
        assert_true(date in console_data)


def test_json():
    formatter = JsonFormatter()
    json_data = formatter.format(test_files)

    for filename, date in test_files.iteritems():
        assert_true(filename in json_data)
        assert_true(date in json_data)

