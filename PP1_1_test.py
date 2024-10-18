import os.path
import sys
from PP1_1 import *

def test_q1(capsys):

  try:
  exists = os.path.exists("PP1_1.py")

    assert exists
  except:
    sys.exit()

  q1()
  captured = capsys.readouterr()
  assert captured.out == "Hello World\n"

def test_q2(capsys):

  try:
  exists = os.path.exists("PP1_1.py")
    assert exists
  except:
    sys.exit()

  q2()
  captured = capsys.readouterr()
  assert captured.out == "1\n2\n3\n4\n5\n"

def test_q3(capsys):

  try:
  exists = os.path.exists("PP1_1.py")
    assert exists
  except:
    sys.exit()

  q3()
  captured = capsys.readouterr()
  assert captured.out == " Help Me!\n"

def test_q4(capsys):

  try:
  exists = os.path.exists("PP1_1.py")
    assert exists
  except:
    sys.exit()

  q4()
  captured = capsys.readouterr()
  assert captured.out == "3 x 3 = 9\n"
