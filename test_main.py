from main import hello 
 
def test_hello(): 
    expected = "Hello, Jenkins!" 
    result = hello() 
     
    if result == expected: 
        print(f"Test passed: {result}") 
    else: 
        print(f"Test failed: Expected {expected}, but got 
{result}") 
 
if __name__ == '__main__': 
    test_hello() 
