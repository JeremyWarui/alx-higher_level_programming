#!/usr/bin/python3
"""
Unittest for Base Class

# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""
import unittest
import json
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    pass