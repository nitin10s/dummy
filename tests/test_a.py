from src import a
def test_b():
    num1 = 5
    num2 = 3 
    expected = 2
    obtianed = a.sub(num1,num2)
    assert expected == obtianed