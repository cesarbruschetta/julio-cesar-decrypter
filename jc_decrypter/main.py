""" module to methods to main  """
import pkg_resources
import argparse
import sys
import logging
from typing import List

from jc_decrypter.processing import decrypter

logger = logging.getLogger(__name__)


def process(args: List) -> int:
    """ method to main process """

    packtools_version = pkg_resources.get_distribution("jc-decrypter").version
    parser = argparse.ArgumentParser(description="Criptografia de Júlio César")

    parser.add_argument("--version", action="version", version=packtools_version)
    parser.add_argument("--loglevel", default="INFO")

    parser.add_argument("--token", "-t", required=True, help="Token de acesso a api")

    args = parser.parse_args(args)

    # CHANGE LOGGER
    level = getattr(logging, args.loglevel.upper())
    logger = logging.getLogger()
    logger.setLevel(level)

    result = decrypter(args.token)
    logger.info("Sua nota é: %(score)s", result["return_submit"])

    return 0


def main() -> None:
    """ method main to script setup.py """
    sys.exit(process(sys.argv[1:]))


if __name__ == "__main__":
    sys.exit(process(sys.argv[1:]))
