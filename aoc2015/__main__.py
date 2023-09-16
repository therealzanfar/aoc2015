#! /usr/bin/env python3

"""Console script for aoc2015."""

import logging
import sys

import click
from click_default_group import DefaultGroup
from rich.logging import RichHandler

CLICK_CONTEXT = {"help_option_names": ["-h", "--help"]}


def setup_logging(verbosity: int = 0) -> None:
    """
    Set up a root logger with console output.

    Args:
        verbosity (int, optional): The logging level; 0=Error, 1=Warning,
            2=Info, 3+=Debug. Defaults to 0.
    """
    logging_level = logging.ERROR
    if verbosity == 1:
        logging_level = logging.WARNING
    elif verbosity == 2:  # noqa: PLR2004
        logging_level = logging.INFO
    elif verbosity >= 3:  # noqa: PLR2004
        logging_level = logging.DEBUG

    logging.basicConfig(
        level=logging_level,
        format="%(message)s",
        datefmt="[%x]",
        handlers=[RichHandler(rich_tracebacks=True)],
    )


@click.group(
    cls=DefaultGroup,
    default="day",
    default_if_no_args=True,
    context_settings=CLICK_CONTEXT,
)
@click.option("-v", "--verbose", count=True)
def cli(verbose: int = 0) -> int:
    """CLI Entry Point."""
    args = locals().items()
    setup_logging(verbose)
    logger = logging.getLogger(__name__)
    logger.debug(
        "Running with options: %s",
        ", ".join(f"{k!s}={v!r}" for k, v in args),
    )

    return 0


@click.command()
@click.argument("PART", nargs=-1)
def compute_day(part: tuple[str]) -> None:
    """
    Compute the final solution for the day.

    PART is the day and part specifier for which solution to compute. The
      first argument given is assumed to be the day (1-25), and the second is
      assumed to be the part (a, b). If either is left blank, the most recent
      part available is computed. If 'ALL' is specified for either argument,
      then all days or all parts are computed.
    """


cli.add_command(compute_day, name="day")


if __name__ == "__main__":
    sys.exit(cli())
