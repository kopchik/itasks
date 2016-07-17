"""
These are tests for code of countdown problem.
Most of them are ``full-stack''.
"""


from workday_countdown import countdown, _countdown, myformat
import pytest
import cProfile
import pstats

def test_countdown_input_validation():
  # not enough arguments
  with pytest.raises(AssertionError):
    countdown("1 2 3")

  # negative arguments
  with pytest.raises(AssertionError):
    countdown("1 2 3 4 5 6 -7")

def test_countdown_correctness():
  # trivial case
  assert countdown("1 2 3 4 5 6 1") == "1 = 1"

  # provided examples
  assert countdown("1 2 3 4 5 6 12") == "2 * 6 = 12"
  assert countdown("5 8 6 25 13 87 390") == "5 * 6 * 13 = 390"

  # test parenthesis in myformat function
  assert myformat() == "( 1 + 2 ) = 3"


def test_countdown_performance():
  """ Evaluates the performance in the worst case. """
  profiler = cProfile.Profile()
  profiler.enable()
  countdown("1 1 1 1 1 1 1000")
  profiler.disable()
  stats = profiler.getstats()
  tot_time = stats[0].totaltime
  assert tot_time < 3, "Wow, your computer is really slow. Or is it my code?"
