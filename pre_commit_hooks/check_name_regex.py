from pathlib import Path
import argparse
import re


def check_name_regex(filenames, regex, dir_):
    if dir_ is not None:
        filenames = [
            f for f in filenames
            if any([
                Path(f).is_relative_to(Path(d))
                for d in dir_
            ])
        ]

    filenames = [
        Path(f).name
        for f in filenames
    ]
    filenames_not_matching_regex = [
        f
        for f in filenames
        if not any([
            re.match(r, f)
            for r in regex
        ])
    ]

    return len(filenames_not_matching_regex)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('filenames', nargs='*')
    parser.add_argument('-r', '--regex',
                        action='append',
                        help='Regex string to match filenames against',
                        required=True)
    parser.add_argument('-d', '--dir',
                        action='append',
                        help='Only consider files from these directories')
    args = parser.parse_args(argv)

    return check_name_regex(args.filenames, args.regex, args.dir)


if __name__ == '__main__':  # pragma: nocover
    raise SystemExit(main())
