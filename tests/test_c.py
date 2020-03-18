from src import c
def test_c():
    num1 = 5
    num2 = 3 
    expected = 15
    obtianed = c.mul(num1,num2)
    assert expected == obtianed