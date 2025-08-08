def perform_operation(num1: float,num2: float,operation: str):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "division":
        if num2 != 0:
            return num1 / num2
        else:
            return "can not divide by 0" 
        
    
