#LinearEquationSolver 
#Cramers Rule


#function to divide and avoid zero division error
def divide(x,y):
    try:
        result = x/y
        result = round(result,3)
    except ZeroDivisionError:
        print("division by zero error")
    else:
        return result
#function that uses cramers rule to solve for x and y
def solve_2x2_matrix(a1,b1,c1,a2,b2,c2):
        #initialize 2x2 matrices
        matrix_d  =  [[a1, b1],
                     [a2, b2]]

        matrix_dx =  [[c1, b2],
                     [c2, b2]]

        matrix_dy =  [[a1, c1],
                     [a2, c2]]

        matrix_c  =  [[c1],
                      [c2]]

        #Get determinant of matrices
        d  = (matrix_d[0][0]*matrix_d[1][1]) - (matrix_d[0][1]*matrix_d[1][0])
        dx = (matrix_dx[0][0]*matrix_dx[1][1]) - (matrix_dx[0][1]*matrix_dx[1][0])
        dy = (matrix_dy[0][0]*matrix_dy[1][1]) - (matrix_dy[0][1]*matrix_dy[1][0])
        
        #get x and y by dividing determinants
        x = divide(dx,d)
        y = divide(dy,d)

        #solve the first equation and round
        equation1_solved = matrix_d[0][0] * x + matrix_d[0][1] * y
        rounded_eq1 = round(equation1_solved,2)
        #solve the second equation and round
        equation2_solved = matrix_d[1][0]* x + matrix_d[1][1] * y
        rounded_eq2 = round(equation2_solved,2)

       

        # forumla =  a1X + b1Y = c1
        eq1 = f"{matrix_d[0][0]}X + {matrix_d[0][1]}Y = {matrix_c[0][0]}"
        # forumla = a2X + b2Y = c2
        eq2 = f"{matrix_d[1][0]}X + {matrix_d[1][1]}Y = {matrix_c[1][0]}"
        #make strings to visually represent matrices
        c = f""" 
        C = |[{matrix_c[0][0]}]|
            |[{matrix_c[1][0]}]|
        """
        dm = f"""
        D = |[{matrix_d[0][0]}, {matrix_d[0][1]}]|
            |[{matrix_d[1][0]}, {matrix_d[1][1]}]| = {d}
        """
        dxm = f"""
        Dx = |[{matrix_dx[0][0]}, {matrix_dx[0][1]}]|
             |[{matrix_dx[1][0]}, {matrix_dx[1][1]}]| = {dx}
        """
        dym = f"""
        Dy = |[{matrix_dy[0][0]}, {matrix_dy[0][1]}]|
             |[{matrix_dy[1][0]}, {matrix_dy[1][1]}]| = {dy}
        """
        # X and Y pair
        xy_pair = f"X = {x}, Y = {y}"
        #Solved Equations
        new_eq1 = f"{matrix_d[0][0]} * {x} + {matrix_d[0][1]} * {y} = {rounded_eq1}"
        new_eq2 = f"{matrix_d[1][0]} * {x} + {matrix_d[1][1]} * {y} = {rounded_eq2}"

        #Main 
        if d == 0:
            #if deteminant of d = 0 the equation has no solution
            print("Equation Has No Solution")
        else:
            print("\n")
            print("_____________________________")
            print("Equations")
            print("-----------------------------")
            print("Equation 1")
            print(eq1)
            print("-----------------------------")
            print("Equation 2")
            print(eq2)
            print("_____________________________")

            print("\n")
            
            print("__________________________________________")
            print("-Matrices")
            print("------------------------------------------")
            print(c)
            print("------------------------------------------")
            print(dm)
            print("------------------------------------------")
            print(dxm)
            print("------------------------------------------")
            print(dym)
            print("__________________________________________")

            print("\n")

            print("____________________________")
            print("X,Y pair")
            print("----------------------------")
            print(xy_pair)
            print("____________________________")

            print("\n")
            print(f"Lets insert {x}, {y} into the equations")
            print(f"_______________________________________")
            print("______________________________")
            print("Equations")
            print("-----------------------------")
            print("Equation 1")
            print(new_eq1)
            print("-----------------------------")
            print("Equation 2")
            print(new_eq2)
            print("_____________________________")
            
            print("\n")

            
            if rounded_eq1 == matrix_c[0][0] and rounded_eq2 == matrix_c[1][0]:
                print("_____________________________________________________________")
                print("Answer")
                print("-------------------------------------------------------------")
                print(f"Confirmed: X:{x}, Y:{y} pair will solve system of equations")
                print("-------------------------------------------------------------")
            


#//////////////////////////////////////
#--Main----------------------
#//////////////////////////////////////
while True:
    try:
        #get first equation
        print("Enter the first equation")
        a1 = float(input("Enter a1: "))
        b1 = float(input("Enter b1: "))
        c1 = float(input("Enter c1: "))
        break
    except ValueError:
        print("Error, lets try again")
        print("\n")
while True:
    try:
        #get second equation
        print("Enter the second equation")
        a2 = float(input("Enter a2: "))
        b2 = float(input("Enter b2: "))
        c2 = float(input("Enter c2: "))
        break
    except ValueError:
        print("Error, lets try again")
        print("\n")




solve_2x2_matrix(a1,b1,c1,a2,b2,c2)
