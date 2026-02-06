from pytest_qatouch import qatouch

@qatouch.TR(10)
def test_example_pass():
    assert True

@qatouch.TR(11)
def test_sum():
    assert 1 + 1 == 2

