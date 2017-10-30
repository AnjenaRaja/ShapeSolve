import math
from random import randint

# Setup rounding decimal places
roundTo = 3

# Setup sides range
sideStart = 1
sideEnd = 12

# To check whether the 3 sides form a valid triangle
def IsValidTriangle(a, b, c):
    if a+b <= c or a+c <= b or b+c <= a:
        return False
    else:
        return True

# To calculate the area of a triangle
def AreaOfTriangle(a, b, c):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return round(area, roundTo)

# To calculate the perimeter of a triangle
def PerimeterOfTriangle(a, b, c):
    perimeter = a+b+c
    return round(perimeter, roundTo)

# To validate user entered values as number
def IsValidNumber(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

# To get user entered value return the value only if it is a valid number
def GetNumericInput(text):  
    temp = input("Enter the " + text + ":")
    while not IsValidNumber(temp):
        print("The value '" + temp + "' is invalid for " + text + ".")
        temp = input("Enter the " + text + ":")
    
    return float(temp)       

# To compute internal angle of the triangle given the sides
def ComputeInternalAngle(a,b,c, angle):
    if angle == "A":
        return round(math.acos((b*b+c*c-a*a)/(2*b*c))*(180/math.pi), roundTo)
    if angle == "B":
        return round(math.acos((a*a+c*c-b*b)/(2*a*c))*(180/math.pi), roundTo)
    if angle == "C":
        return round(math.acos((a*a+b*b-c*c)/(2*a*b))*(180/math.pi), roundTo)
        
# To process user input for a triange
def ProcessUserTriangle():
    a = GetNumericInput("side 'a' of the triangle")
    b = GetNumericInput("side 'b' of the triangle")
    c = GetNumericInput("side 'c' of the triangle")

    if IsValidTriangle(a, b, c):
        print("Area of the triangle = " + str(AreaOfTriangle(a, b, c)) + " square units")
        print("Perimeter of the triangle = " + str(PerimeterOfTriangle(a, b, c)) + " units")
        print("The internal angles are = " + str(ComputeInternalAngle(a,b,c, "A")) + "°, " + str(ComputeInternalAngle(a,b,c, "B")) + "° and " + str(ComputeInternalAngle(a,b,c, "C")) + "°")
    else:
        print("The sides '" + str(a) + "', '" + str(b) + "' and '" + str(c) + "' do not form a valid triangle.")

# To calculate the area of a rectangle
def AreaOfRectangle(l, b):
    area = l * b
    return round(area, roundTo)

# To calculate the perimeter of a rectangle
def PerimeterOfRectangle(l, b):
    perimeter = 2 * (l + b)
    return round(perimeter, roundTo)

# To check whether the 2 sides form a valid rectangle
def IsValidRectangle(l, b):
    if l > 0 and b > 0:
        return True
    else:
        return False
    
# To process user input for a rectange
def ProcessUserRectangle():
    l = GetNumericInput("length of the rectangle")
    b = GetNumericInput("breath of the rectangle")

    if IsValidRectangle(l, b):
        print("Area of the rectangle = " + str(AreaOfRectangle(l, b)) + " square units")
        print("Perimeter of the rectangle = " + str(PerimeterOfRectangle(l, b)) + " units")
    else:
        print("The sides '" + str(l) + "' and '" + str(b) + "' do not form a valid rectangle.")   


# To calculate the area of a square
def AreaOfSquare(s):
    area = s * s
    return round(area, roundTo)

# To calculate the perimeter of a square
def PerimeterOfSquare(s):
    perimeter = 4 * (s)
    return round(perimeter, roundTo)

# To check whether the side form a valid square
def IsValidSquare(s):
    if s > 0 :
        return True
    else:
        return False
    
# To process user input for a square
def ProcessUserSquare():
    s = GetNumericInput("side length of the square")

    if IsValidSquare(s):
        print("Area of the square = " + str(AreaOfSquare(s)) + " square units")
        print("Perimeter of the square = " + str(PerimeterOfSquare(s)) + " units")
    else:
        print("The side '" + str(s) + "' does not form a valid square.")    

# To calculate the area of a circle
def AreaOfCircle(r):
    area = ((r)**2)*math.pi
    return round(area, roundTo)

# To calculate the circumference of a circle
def CircumferenceOfCircle(r):
    circumference =(2)*(math.pi)*(r)
    return round(circumference, roundTo)

# To check whether the radius forms a valid circle
def IsValidCircle(r):
    if r > 0 :
        return True
    else:
        return False
    
# To process user input for a circle
def ProcessUserCircle():
    r = GetNumericInput("radius of the circle")

    if IsValidCircle(r):
        print("Area of the circle = " + str(AreaOfCircle(r)) + " square units")
        print("Circumference of the circle = " + str(CircumferenceOfCircle(r)) + " units")
    else:
        print("The radius '" + str(r) + "' does not form a valid circle.")    

# clear the screen first so that we can display the messages
def ClearScreen():
    print ("\n" * 50)

# To display welcome page explaining about this software
def DisplaySplashScreen():
    print ("=" *80)
    print ("\t\t\t\tWelcome to ShapeSolve")
    print ("\t\t\t\t=====================")
    print ("ShapeSolve is a Python program that can sovle geometry problems. It can also ")
    print ("quiz you on area and perimeter of triangles, rectangles, squares and circles.")
    print ("")
    print ("Developed by: Anjena Raja #2, Grade 5, Mrs. Carr for Genius Hour");
    print ("=" *80)        

# To display closing credits
def DisplayCredits():
    print ("=" *80)
    print ("Thank you for using ShapeSolve.")
    print ("Hope you found this software useful.")
    print ("Contact the developed for comments and feedback.")
    print ("")
    print ("Bye!")
    print ("")
    print ("Developed by: Anjena Raja #2, Grade 5, Mrs. Carr for Genius Hour");
    print ("=" *80)        

# To validate user entered menu choice
def IsValidMainMenu(menu):
    if menu == "X" or menu == "x":
        return True
    if menu == "S" or menu == "s":
        return True
    if menu == "Q" or menu == "q":
        return True

    return False

# To get user entered value return the value only if it is a valid menu
def GetMainMenuInput(text):  
    temp = input("Enter " + text + ":")
    while not IsValidMainMenu(temp):
        print("The value '" + temp + "' is invalid for " + text + ".")
        temp = input("Enter " + text + ":")
    
    return temp       

# Display Main Menu and get user inputs
def DisplayMainMenu():
    print ("=" *80)        
    print ("Choose your option:")
    print ("===================")
    print ("Enter S for ShapeSolve to solve.")
    print ("Enter Q for ShapeSolve to quiz you.")
    print ("Enter X to exit ShapeSolve.")
    MenuChoice = GetMainMenuInput("your menu choice (S, Q or X)")

    if MenuChoice == "X" or MenuChoice == "x":
        DisplayCredits()

    if MenuChoice == "S" or MenuChoice == "s":
        DisplaySolveMenu()
        DisplayMainMenu()
        
    if MenuChoice == "Q" or MenuChoice == "q":
        DisplayQuiz()
        DisplayMainMenu()


# To validate user entered solve menu choice
def IsValidSolveMenu(menu):
    if menu == "T" or menu == "t":
        return True
    if menu == "R" or menu == "r":
        return True
    if menu == "S" or menu == "s":
        return True
    if menu == "C" or menu == "c":
        return True
    if menu == "X" or menu == "x":
        return True

    return False

# To get user entered value return the value only if it is a valid menu
def GetSolveMenuInput(text):  
    temp = input("Enter " + text + ":")
    while not IsValidSolveMenu(temp):
        print("The value '" + temp + "' is invalid for " + text + ".")
        temp = input("Enter " + text + ":")
    
    return temp       

# Display Solve Menu and get user inputs
def DisplaySolveMenu():
    print ("=" *80)        
    print ("Choose your option:")
    print ("===================")
    print ("Enter T for ShapeSolve to solve triangles.")
    print ("Enter R for ShapeSolve to solve rectangles.")
    print ("Enter S for ShapeSolve to solve squares.")
    print ("Enter C for ShapeSolve to solve circles.")
    print ("Enter X to exit Solve Menu.")

    MenuChoice = GetSolveMenuInput("your menu choice (T, R, S, C or X)")

    if MenuChoice == "X" or MenuChoice == "x":
        return

    if MenuChoice == "T" or MenuChoice == "t":
        ProcessUserTriangle()
        DisplaySolveMenu()

    if MenuChoice == "R" or MenuChoice == "r":
        ProcessUserRectangle()
        DisplaySolveMenu()

    if MenuChoice == "S" or MenuChoice == "s":
        ProcessUserSquare()
        DisplaySolveMenu()

    if MenuChoice == "C" or MenuChoice == "c":
        ProcessUserCircle()
        DisplaySolveMenu()

# Generate Random shape for quiz
def GenerateRandomShape():
    temp = randint(1,4)
    if temp == 1:
        return "Triangle"
    if temp == 2:
        return "Circle"
    if temp == 3:
        return "Rectangle"
    if temp == 4:
        return "Square"

# Generate Random side for quiz
def GenerateRandomSide():
    return randint(sideStart, sideEnd) 

# Generate Random side for Triangle
def GenerateRandomTriangleSide(a, b):
    return randint(sideStart, a + b - 1) 

# Display Quiz and get user inputs
def DisplayQuiz():
    print ("=" *80)        
    # Generate random shape
    shape = GenerateRandomShape()
    print("ShapeSolve has chosen '"+ shape +"' for you to solve!")

    # Generate sides of the random shape
    if shape == "Square":
        s = GenerateRandomSide()
    if shape == "Rectangle":
        l = GenerateRandomSide()
        b = GenerateRandomSide()
    if shape == "Circle":
        r = GenerateRandomSide()
    if shape == "Triangle":
        a = GenerateRandomSide()
        b = GenerateRandomSide()
        c = GenerateRandomTriangleSide(a, b)
       
    # Display the sides to user
    if shape == "Square":
        print ("The side of your square is:" + str(s))
    if shape == "Rectangle":
        print ("The sides of your rectangle are:" + str(l) + " and " + str(b))
    if shape == "Circle":
        print ("The radius of your circle is:" + str(r))
    if shape == "Triangle":
        print ("The sides of your triangle are:" + str(a) + ", " + str(b) + " and " + str(c))
        

    # Get user input for Area and Perimeter
    if shape == "Square":
        uarea = GetNumericInput("area of the square");
        uperimeter = GetNumericInput("perimeter of the square")
    if shape == "Circle":
        uarea = GetNumericInput("area of the circle");
        ucircumference = GetNumericInput("circumference of the circle")
    if shape == "Rectangle":
        uarea = GetNumericInput("area of the rectangle");
        uperimeter = GetNumericInput("perimeter of the rectangle")
    if shape == "Triangle":
        uarea = GetNumericInput("area of the triangle");
        uperimeter = GetNumericInput("perimeter of the triangle")

    # Compute area and perimeter
    if shape == "Square":
        area = AreaOfSquare(s)
        perimeter = PerimeterOfSquare(s)
    if shape == "Circle":
        area = AreaOfCircle(r)
        circumference = CircumferenceOfCircle(r)
    if shape == "Rectangle":
        area = AreaOfRectangle(l, b)
        perimeter = PerimeterOfRectangle(l, b)
    if shape == "Triangle":
        area = AreaOfTriangle(a, b, c)
        perimeter = PerimeterOfTriangle(a, b, c)

    # Compare calculated area and user entered area and display correct or wrong
    if shape == "Square":
        if area == uarea:
            print("The area you have calculated is correct. :)");
            print("Good job!")
        else:
            print("The area you have calculated is incorrect. :(");
            print("Area of square = " + str(area) + " square units")

        if perimeter == uperimeter:
            print("The perimeter you have calculated is correct. :)");
            print("Good job!")
        else:
            print("The perimeter you have calculated is incorrect. :(");
            print("Perimeter of the square = " + str(perimeter) + " units")        


    if shape == "Circle":
        if area == uarea:
            print("The area you have calculated is correct. :)");
            print("Good job!")
        else:
            print("The area you have calculated is incorrect. :(");
            print("Area of circle = " + str(area) + " square units")

        if circumference == ucircumference:
            print("The circumference you have calculated is correct. :)");
            print("Good job!")
        else:
            print("The perimeter you have calculated is incorrect. :(");
            print("Circumference of the circle = " + str(circumference) + " units")        


    if shape == "Rectangle":
        if area == uarea:
            print("The area you have calculated is correct. :)");
            print("Good job!")
        else:
            print("The area you have calculated is incorrect. :(");
            print("Area of rectangle = " + str(area) + " square units")

        if perimeter == uperimeter:
            print("The perimeter you have calculated is correct. :)");
            print("Good job!")
        else:
            print("The perimeter you have calculated is incorrect. :(");
            print("Perimeter of the rectangle = " + str(perimeter) + " units")        


    if shape == "Triangle":
        if area == uarea:
            print("The area you have calculated is correct. :)");
            print("Good job!")
        else:
            print("The area you have calculated is incorrect. :(");
            print("Area of triangle = " + str(area) + " square units")

        if perimeter == uperimeter:
            print("The perimeter you have calculated is correct. :)");
            print("Good job!")
        else:
            print("The perimeter you have calculated is incorrect. :(");
            print("Perimeter of the triangle = " + str(perimeter) + " units")        
   
# Main program flow
def Main():
    #ClearScreen()
    DisplaySplashScreen()
    DisplayMainMenu()
 
Main()


