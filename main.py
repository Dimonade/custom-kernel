#!/usr/bin/env python3

from zen_custom import ColorLognameFormatter

from kernel_config import KernelDict, KConfig, KConfigParameter

from logging import getLogger, StreamHandler

if __name__ == "__main__":
    logger = getLogger()
    logger.setLevel("DEBUG")
    stdout_handler = StreamHandler()
    stdout_handler.setFormatter(
        ColorLognameFormatter(fmt="%(levelname)s | %(name)-70s | %(message)s")
    )
    logger.addHandler(stdout_handler)

    kconfig = KConfig()
    print(kconfig)
    exit()

    config = KernelDict()

    print(config)
