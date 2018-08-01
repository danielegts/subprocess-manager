# -*- coding: utf-8 -*-
import subprocess
import logging

class SubprocessManager(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info("SubprocessManager initialized")

    def execute(self, command):
        try:
            return subprocess.check_output(command)
        except subprocess.CalledProcessError as e:
            self.logger.error(e)


if __name__ == '__main__':
    sm = SubprocessManager()

    print(sm.execute(r"ls -l"))
