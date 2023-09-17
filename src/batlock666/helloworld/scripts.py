# NOQA: D100

import argparse

from . import functions


def hello_world():
    """Console script ``hello_world``.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "name",
        type=str,
        nargs="?",
        default=None,
    )

    args = parser.parse_args()

    print(functions.hello_world(args.name))
