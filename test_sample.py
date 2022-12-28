
# simple catchall to keep my test coverage up while I experiment

# I think this will run the learning_python script and ensure we get coverage of it in test without doing any specific testing.
import learning_python


# content of test_sample.py - seeing how test coverage works in python
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4
    

