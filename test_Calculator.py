import Calculator
import pytest

@pytest.mark.parametrize("a,b,c",[(3,2,5),(5,1,6),(8,2,10),(4,3,2,)])
def test_add2numbers(a,b,c):

    res=Calculator.add2numbers(a,b)
    assert res==c

@pytest.mark.parametrize("a,b,c",[(9,2,7),(6,1,5),(3,2,1),(5,8,3)])
def test_sub2numbers(a,b,c):
    res=Calculator.sub2numbers(a,b)
    assert res==c

@pytest.mark.parametrize("a,b,c",[(3,2,6),(5,1,5),(8,2,16),(5,2,9)])
def test_mul2numbers(a,b,c):

    res=Calculator.mul2numbers(a,b)
    assert res==c

@pytest.mark.parametrize("a,b,c",[(10,2,5),(4,4,1),(8,2,4),(5,2,9)])
def test_div2numbers(a,b,c):

    res=Calculator.div2numbers(a,b)
    assert res==c
