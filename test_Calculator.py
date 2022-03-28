import Calculator

def test_add2numbers():
    x=10
    y=20
    res=Calculator.add2numbers(x,y)
    assert res==x+y

def test_sub2numbers():
    x=10
    y=20
    res=Calculator.sub2numbers(x,y)
    assert res==x-y

def test_mul2numbers():
    x=10
    y=20
    res=Calculator.mul2numbers(x,y)
    assert res==x*y

def test_div2numbers():
    x=10
    y=20
    res=Calculator.div2numbers(x,y)
    assert res==x/y
