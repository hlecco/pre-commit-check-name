"""Tests check_name_regex.py."""
import pre_commit_hooks.check_name_regex as check_name_regex


def test_check_all_match():
    """Assert every filename matches at least one regex."""
    filenames = ['foo', 'bar']
    regex = ['^f', '^b']
    dir_ = None

    assert check_name_regex.check_name_regex(filenames, regex, dir_) == 0


def test_check_number_unmatched():
    """Check if the number of unmatched filenames is correct."""
    filenames = ['foo', 'bar', 'baz']
    regex = ['^f']
    dir_ = None

    assert check_name_regex.check_name_regex(filenames, regex, dir_) == 2


def test_dir_filter():
    """Filter out filenames that are not on checked directories."""
    filenames = ['somedir/foo1', 'somedir/bar1', 'foo2', 'bar2']
    regex = ['^f']
    dir_ = ['somedir']

    assert check_name_regex.check_name_regex(filenames, regex, dir_) == 1


def test_argparse():
    """Check parameters usage on main call."""
    argv = [
        '-r', '^f',
        '-r', '^b',
        'foo', 'bar'
    ]
    assert check_name_regex.main(argv) == 0

    argv = [
        '-r', '^f',
        '-d', 'somedir',
        'somedir/foo1', 'somedir/bar1', 'foo2', 'bar2'
    ]
    assert check_name_regex.main(argv) == 1
