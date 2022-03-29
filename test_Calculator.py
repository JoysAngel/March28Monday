import Calculator
import pytest

@pytest.mark.parametrize("a,b,c",[(3,2,5),(5,1,6),(8,2,10),(5,2,9)])
def test_add2numbers(a,b,c):

    res=Calculator.add2numbers(a,b)
    assert res==c

@pytest.mark.addsub
def test_sub2numbers():
    x=10
    y=20
    res=Calculator.sub2numbers(x,y)
    assert res==x-y

@pytest.mark.muldiv
def test_mul2numbers():
    x=10
    y=20
    res=Calculator.mul2numbers(x,y)
    assert res==x*y

@pytest.mark.muldiv
def test_div2numbers():
    x=10
    y=20
    res=Calculator.div2numbers(x,y)
    assert res==x/y
