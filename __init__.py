# -*- coding: utf-8 -*-

"""Top-level package for Subprocess Manager."""

__author__ = """Daniele Turato"""
__email__ = 'daniele.turato@siav.it'
__version__ = '0.1.0'

from subprocess_manager.subprocess_manager import SubprocessManager
import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())
