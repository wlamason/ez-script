"""{{cookiecutter.project_name}} - {{cookiecutter.project_description}}"""

import argparse
import logging
import time
from contextlib import contextmanager
from typing import Optional

from pydantic import BaseModel

logger = logging.getLogger(__name__)


#############
# Utilities #
#############


@contextmanager
def time_it(msg: str):
    """Context manager to capture the timing of functions and code blocks."""
    start = time.perf_counter_ns()
    try:
        yield
    finally:
        end = time.perf_counter_ns()
        logger.info(f"{msg} took {(end - start) / 1_000_000}ms")


###################
# Pydantic Models #
###################


# TODO: Add expected config attributes
class Config(BaseModel):
    """Configurations from config.json file."""


# TODO: Add expected secret attributes
class Secrets(BaseModel):
    """Secrets from secrets.json file."""


# TODO: Fix comment
########
# {{cookiecutter.project_name}} #
########


@time_it("{{cookiecutter.project_name}}")
def main(config: Config, secrets: Secrets) -> int:
    """Main processing logic."""
    # TODO: Fill in


###################
# CLI Boilerplate #
###################


def config_logger(verbosity: str):
    """Configure logging script."""
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    file_handler = logging.FileHandler("{{cookiecutter.project_name}}.log")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(verbosity)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="{{cookiecutter.project_description}}")
    parser.add_argument(
        "-v", "--verbosity", default="INFO", choices=["WARNING", "INFO", "DEBUG"], help="Level to log at."
    )
    parser.add_argument("-c", "--config", default="config.json", help="Config filename.")
    parser.add_argument("-s", "--secrets", default="secrets.json", help="Secrets filename.")
    return parser.parse_args(argv)


if __name__ == "__main__":
    args = parse_args()
    config_logger(args.verbosity)
    config = Config.parse_file(args.config)
    secrets = Secrets.parse_file(args.secrets)
    raise SystemExit(main(config, secrets))
