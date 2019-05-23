from . import james_test

def test_james_test():
    assert james_test.apply("Jane") == "hello Jane"
