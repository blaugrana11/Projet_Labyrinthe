import pytest
import my_AI
import unittest


def test_play():
    
    assert my_AI.play()== type(dict)

def test_lifes():
    assert 0 <= my_AI.lifes() <=3 

