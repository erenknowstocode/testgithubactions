from src.math_operations import *

def test_add():
    assert add_operation(2,3)==5
    assert add_operation(-1,1)==0
    
def test_sub():    
    assert sub_operation(4,3)==1
    assert sub_operation(5,3)==2
    