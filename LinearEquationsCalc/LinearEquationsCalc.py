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
#functions that uses cramers rule to solve for x and y
def solve_3x3_matrix(a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3):
        
        #////////////////////
        # MATRIX C
        #//////////////////// 
        matrix_c = [[d1],
                    [d2],
                    [d3]]
        matrix_c_string = f"""
        C = |[{matrix_c[0][0]}]|
            |[{matrix_c[1][0]}]|
            |[{matrix_c[2][0]}]|
                             """
        #////////////////////
        # MATRIX D
        #////////////////////
        matrix_d = [[a1,b1,c1],
                    [a2,b2,c2],
                    [a3,b3,c3]]
        matrix_d_var_dx = (matrix_d[1][1] * matrix_d[2][2]) - (matrix_d[1][2] * matrix_d[2][1])
        matrix_d_var_dy = (matrix_d[1][0] * matrix_d[2][2]) - (matrix_d[1][2] * matrix_d[2][0])
        matrix_d_var_dz = (matrix_d[1][0] * matrix_d[2][1]) - (matrix_d[1][1] * matrix_d[2][0])
        matrix_d_var_d = (matrix_d[0][0]*(matrix_d_var_dx)) - (matrix_d[0][1]*(matrix_d_var_dy)) + (matrix_d[0][2]*(matrix_d_var_dz))
        matrix_d_string = f"""
        D = |[{matrix_d[0][0]},{matrix_d[0][1]},{matrix_d[0][2]}]|
            |[{matrix_d[1][0]},{matrix_d[1][1]},{matrix_d[1][2]}]|
            |[{matrix_d[2][0]},{matrix_d[2][1]},{matrix_d[2][2]}]| = {matrix_d_var_d}
                              """

        
        #////////////////////
        # MATRIX DX
        #////////////////////
        matrix_dx = [[d1,b1,c1],
                     [d2,b2,c2],
                     [d3,b3,c3]]
        matrix_dx_var_dx = (matrix_dx[1][1] * matrix_dx[2][2]) - (matrix_dx[1][2] * matrix_dx[2][1])
        matrix_dx_var_dy = (matrix_dx[1][0] * matrix_dx[2][2]) - (matrix_dx[1][2] * matrix_dx[2][0])
        matrix_dx_var_dz = (matrix_dx[1][0] * matrix_dx[2][1]) - (matrix_dx[1][1] * matrix_dx[2][0])
        matrix_dx_var_d = (matrix_dx[0][0]*(matrix_dx_var_dx)) - (matrix_dx[0][1]*(matrix_dx_var_dy)) + (matrix_dx[0][2]*(matrix_dx_var_dz))
        matrix_dx_string = f"""
        Dx = |[{matrix_dx[0][0]},{matrix_dx[0][1]},{matrix_dx[0][2]}]|
             |[{matrix_dx[1][0]},{matrix_dx[1][1]},{matrix_dx[1][2]}]|
             |[{matrix_dx[2][0]},{matrix_dx[2][1]},{matrix_dx[2][2]}]| = {matrix_dx_var_d}
                               """

        
        #////////////////////
        # MATRIX DY
        #////////////////////
        matrix_dy = [[a1,d1,c1],
                     [a2,d2,c2],
                     [a3,d3,c3]]
        matrix_dy_var_dx = (matrix_dy[1][1] * matrix_dy[2][2]) - (matrix_dy[1][2] * matrix_dy[2][1])
        matrix_dy_var_dy = (matrix_dy[1][0] * matrix_dy[2][2]) - (matrix_dy[1][2] * matrix_dy[2][0])
        matrix_dy_var_dz = (matrix_dy[1][0] * matrix_dy[2][1]) - (matrix_dy[1][1] * matrix_dy[2][0])
        matrix_dy_var_d = (matrix_dy[0][0]*(matrix_dy_var_dx)) - (matrix_dy[0][1]*(matrix_dy_var_dy)) + (matrix_dy[0][2]*(matrix_dy_var_dz))
        matrix_dy_string = f"""
        Dy = |[{matrix_dy[0][0]},{matrix_dy[0][1]},{matrix_dy[0][2]}]|
             |[{matrix_dy[1][0]},{matrix_dy[1][1]},{matrix_dy[1][2]}]|
             |[{matrix_dy[2][0]},{matrix_dy[2][1]},{matrix_dy[2][2]}]| = {matrix_dy_var_d}
                               """

        
        #////////////////////
        # MATRIX DZ
        #////////////////////
        matrix_dz = [[a1,b1,d1],
                     [a2,b2,d2],
                     [a3,b3,d3]]
        matrix_dz_var_dx = (matrix_dz[1][1] * matrix_dz[2][2]) - (matrix_dz[1][2] * matrix_dz[2][1])
        matrix_dz_var_dy = (matrix_dz[1][0] * matrix_dz[2][2]) - (matrix_dz[1][2] * matrix_dz[2][0])
        matrix_dz_var_dz = (matrix_dz[1][0] * matrix_dz[2][1]) - (matrix_dz[1][1] * matrix_dz[2][0])
        matrix_dz_var_d = (matrix_dz[0][0]*(matrix_dz_var_dx)) - (matrix_dz[0][1]*(matrix_dz_var_dy)) + (matrix_dz[0][2]*(matrix_dz_var_dz))
        matrix_dz_string = f"""
        Dz = |[{matrix_dz[0][0]},{matrix_dz[0][1]},{matrix_dz[0][2]}]|
             |[{matrix_dz[1][0]},{matrix_dz[1][1]},{matrix_dz[1][2]}]|
             |[{matrix_dz[2][0]},{matrix_dz[2][1]},{matrix_dz[2][2]}]| = {matrix_dz_var_d}
                       """

        #///////////////////////////////
        # MATRICIES DETERMINANTS
        #//////////////////////////////
        d = matrix_d_var_d
        dx = matrix_dx_var_d
        dy = matrix_dy_var_d
        dz = matrix_dz_var_d
        #////////////////////
        # X,Y,Z
        #////////////////////
        x = divide(dx,d)
        y = divide(dy,d)
        z = divide(dz,d)
        xyz_string = f"X = {x}, Y = {y}, Z = {z}"
        #//////////////////////////////////
        # Unsolved Equations strings
        #/////////////////////////////////
        equation1 = f"{matrix_d[0][0]}X + {matrix_d[0][1]}Y + {matrix_d[0][2]}Z = {matrix_c[0][0]}"
        equation2 = f"{matrix_d[1][0]}X + {matrix_d[1][1]}Y + {matrix_d[1][2]}Z = {matrix_c[1][0]}"
        equation3 = f"{matrix_d[2][0]}X + {matrix_d[2][1]}Y + {matrix_d[2][2]}Z = {matrix_c[2][0]}"
        #////////////////////
        #"Solved" Equations
        #////////////////////
        solved_eq1 = (matrix_d[0][0] * x + matrix_d[0][1] * y + matrix_d[0][2] * z) 
        solved_eq2 = (matrix_d[1][0] * x + matrix_d[1][1] * y + matrix_d[1][2] * z)
        solved_eq3 = (matrix_d[2][0] * x + matrix_d[2][1] * y + matrix_d[2][2] * z) 
        #////////////////////
        #Rounded Equations
        #////////////////////
        rounded_eq1 = round(solved_eq1,2)
        rounded_eq2 = round(solved_eq2,2)
        rounded_eq3 = round(solved_eq3,2)
        #///////////////////////////////
        # Solved Equation strings
        #//////////////////////////////
        solved_eq1_string = f"{matrix_d[0][0]} * {x} + {matrix_d[0][1]} * {y} + {matrix_d[0][2]} * {z} = {rounded_eq1}"
        solved_eq2_string = f"{matrix_d[1][0]} * {x} + {matrix_d[1][1]} * {y} + {matrix_d[1][2]} * {z} = {rounded_eq2}"
        solved_eq3_string = f"{matrix_d[2][0]} * {x} + {matrix_d[2][1]} * {y} + {matrix_d[2][2]} * {z} = {rounded_eq3}"


        #///////////////////////////////
        # main
        #//////////////////////////////

        if d == 0:
            #if deteminant of d = 0 the equation has no solution
            print("Equation Has No Solution")
        else:

            print("\n")

            print("_____________________________")
            print("-System of Equations")
            print("-----------------------------")
            print("Equation 1")
            print(equation1)
            print("-----------------------------")
            print("Equation 2")
            print(equation2)
            print("-----------------------------")
            print("Equation 3")
            print(equation3)
            print("_____________________________")

            print("\n")
            
            print("__________________________________________")
            print("-Matrices")
            print("------------------------------------------")
            print(matrix_c_string)
            print("------------------------------------------")
            print(matrix_d_string)
            print("------------------------------------------")
            print(matrix_dx_string)
            print("------------------------------------------")
            print(matrix_dy_string)
            print("------------------------------------------")
            print(matrix_dz_string)
            print("__________________________________________")

            print("\n")

            print("____________________________")
            print("X,Y,Z")
            print("----------------------------")
            print(xyz_string)
            print("____________________________")

            print("\n")
            print(f"Lets insert {x}, {y}, {z} into the equations")
            print(f"_______________________________________")
            print("______________________________")
            print("Equations")
            print("-----------------------------")
            print("Equation 1")
            print(solved_eq1_string)
            print("-----------------------------")
            print("Equation 2")
            print(solved_eq2_string)
            print("-----------------------------")
            print("Equation 3")
            print(solved_eq3_string)
            print("_____________________________")
            
            print("\n")
            if rounded_eq1 == matrix_c[0][0] and rounded_eq2 == matrix_c[1][0] and rounded_eq3 == matrix_c[2][0]:
                print("_____________________________________________________________")
                print("Answer")
                print("-------------------------------------------------------------")
                print(f"Sucess: X:{x}, Y:{y}, Z:{z} will solve system of equations")
                print("-------------------------------------------------------------")
                print("_____________________________________________________________")
            else:
                print("_____________________________________________________________")
                print("Answer")
                print("-------------------------------------------------------------")
                print(f"Failed: X:{x}, Y:{y}, Z:{z} will not solve system of equations")
                print("-------------------------------------------------------------")
                print("_____________________________________________________________")


        



def solve_2x2_matrix(a1,b1,c1,a2,b2,c2):
        #initialize 2x2 matrices
        #////////////////////
        # MATRIX C
        #////////////////////
        matrix_c  =  [[c1],
                      [c2]]
        matrix_c_string = f""" 
        C = |[{matrix_c[0][0]}]|
            |[{matrix_c[1][0]}]|
        """
        #////////////////////
        # MATRIX D
        #////////////////////
        matrix_d  =  [[a1, b1],
                     [a2, b2]]

        matrix_d_string = f"""
        D = |[{matrix_d[0][0]}, {matrix_d[0][1]}]|
            |[{matrix_d[1][0]}, {matrix_d[1][1]}]| = {d}
        """
        #////////////////////
        # MATRIX DX
        #////////////////////
        matrix_dx =  [[c1, b2],
                     [c2, b2]]
        matrix_dx_string = f"""
        Dx = |[{matrix_dx[0][0]}, {matrix_dx[0][1]}]|
             |[{matrix_dx[1][0]}, {matrix_dx[1][1]}]| = {dx}
        """
        #////////////////////
        # MATRIX DY
        #////////////////////
        matrix_dy =  [[a1, c1],
                     [a2, c2]]
        matrix_dy_string = f"""
        Dy = |[{matrix_dy[0][0]}, {matrix_dy[0][1]}]|
             |[{matrix_dy[1][0]}, {matrix_dy[1][1]}]| = {dy}
        """
        #///////////////////////////////
        # MATRICIES DETERMINANTS
        #//////////////////////////////
        d  = (matrix_d[0][0]*matrix_d[1][1]) - (matrix_d[0][1]*matrix_d[1][0]) 
        dx = (matrix_dx[0][0]*matrix_dx[1][1]) - (matrix_dx[0][1]*matrix_dx[1][0])
        dy = (matrix_dy[0][0]*matrix_dy[1][1]) - (matrix_dy[0][1]*matrix_dy[1][0])

        #////////////////////
        # X,Y
        #////////////////////
        x = divide(dx,d)
        y = divide(dy,d)
        xy_string = f"X = {x}, Y = {y}"

        #//////////////////////////////////
        # Unsolved Equations strings
        #/////////////////////////////////
        equation1 = f"{matrix_d[0][0]}X + {matrix_d[0][1]}Y = {matrix_c[0][0]}"
        equation2 = f"{matrix_d[1][0]}X + {matrix_d[1][1]}Y = {matrix_c[1][0]}"

        #////////////////////
        #"Solved" Equations
        #////////////////////
        equation1_solved = matrix_d[0][0] * x + matrix_d[0][1] * y
        equation2_solved = matrix_d[1][0]* x + matrix_d[1][1] * y

        #////////////////////
        #Rounded Equations
        #////////////////////
        rounded_eq1 = round(equation1_solved,2)
        rounded_eq2 = round(equation2_solved,2)

        #///////////////////////////////
        # Solved Equation strings
        #//////////////////////////////
        solved_eq1_string = f"{matrix_d[0][0]} * {x} + {matrix_d[0][1]} * {y} = {rounded_eq1}"
        solved_eq2_string = f"{matrix_d[1][0]} * {x} + {matrix_d[1][1]} * {y} = {rounded_eq2}"

     



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
            print(equation1)
            print("-----------------------------")
            print("Equation 2")
            print(equation2)
            print("_____________________________")

            print("\n")
            
            print("__________________________________________")
            print("-Matrices")
            print("------------------------------------------")
            print(matrix_c_string)
            print("------------------------------------------")
            print(matrix_d_string)
            print("------------------------------------------")
            print(matrix_dx_string)
            print("------------------------------------------")
            print(matrix_dy_string)
            print("__________________________________________")

            print("\n")

            print("____________________________")
            print("X,Y")
            print("----------------------------")
            print(xy_string)
            print("____________________________")

            print("\n")
            print(f"Lets insert {x}, {y} into the equations")
            print(f"_______________________________________")
            print("______________________________")
            print("Equations")
            print("-----------------------------")
            print("Equation 1")
            print(solved_eq1_string)
            print("-----------------------------")
            print("Equation 2")
            print(solved_eq2_string)
            print("_____________________________")
            
            print("\n")

            
            if rounded_eq1 == matrix_c[0][0] and rounded_eq2 == matrix_c[1][0]:
                print("_____________________________________________________________")
                print("Answer")
                print("-------------------------------------------------------------")
                print(f"Sucess: X:{x}, Y:{y} pair will solve system of equations")
                print("-------------------------------------------------------------")
                print("_____________________________________________________________")
            else:
                print("_____________________________________________________________")
                print("Answer")
                print("-------------------------------------------------------------")
                print(f"Failed: X:{x}, Y:{y} pair will not solve system of equations")
                print("-------------------------------------------------------------")
                print("_____________________________________________________________")


            


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
        d1 = float(input("enter d1 "))
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
        d2 = float(input("enter d2 "))

        break
    except ValueError:
        print("Error, lets try again")
        print("\n")
while True:
    try:
        #get second equation
        print("Enter the third equation")
        a3 = float(input("Enter a3: "))
        b3 = float(input("Enter b3: "))
        c3 = float(input("Enter c3: "))
        d3 = float(input("enter d3 "))

        break
    except ValueError:
        print("Error, lets try again")
        print("\n")


solve_3x3_matrix(a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3)
#solve_2x2_matrix(a1,b1,c1,a2,b2,c2)
