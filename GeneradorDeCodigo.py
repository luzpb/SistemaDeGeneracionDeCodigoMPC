from jinja2 import Environment, FileSystemLoader
import Datos

target_language = input("Ingresa el lenguaje de destino (python/micropython): ")
target_problem = input("Ingresa el problema de destino (QP/MPC): ")

if target_language == "python":
    target_library = input("Ingresa la librería de destino (cvxpy/pyomo): ")
    if target_library == "cvxpy":
        if target_problem == "QP":
            template_loader = FileSystemLoader(searchpath="QP")
            env = Environment(loader=template_loader)
            
            print("\nEl problema tiene restricciones:\n\t (1) NO \n\t (2) Solo restricciones de desigualdad \n\t (3) Solo restricciones lineales \n\t (4) Ambas")    
            target_constraints = input("Ingrese las restricciones(1/2/3/4):")

            if target_constraints == "1":
                template = env.get_template("Python_cvxpy_QP_NoRestricciones.py")
                rendered_template = template.render(Q=Datos.Q, c=Datos.c, n=Datos.n)

            elif target_constraints == "2" :
                template = env.get_template("Python_cvxpy_QP_RestDesigualdad.py")
                rendered_template = template.render(Q=Datos.Q, c=Datos.c, n=Datos.n, p=Datos.p, G=Datos.G, h=Datos.h)

            elif target_constraints == "3" :
                template = env.get_template("Python_cvxpy_QP_RestLineales.py")
                rendered_template = template.render(Q=Datos.Q, c=Datos.c, n=Datos.n, m=Datos.m, A=Datos.A, b=Datos.b)

            elif target_constraints == "4":
                template = env.get_template("Python_cvxpy_QP_Restricciones.py")
                rendered_template = template.render(Q=Datos.Q, c=Datos.c, n=Datos.n, m=Datos.m, A=Datos.A, b=Datos.b, p=Datos.p, G=Datos.G, h=Datos.h)
        
        if target_problem == "MPC":
            template_loader = FileSystemLoader(searchpath="MPC")
            env = Environment(loader=template_loader)
            print("\nElige el tipo de MPC: \n\t (1) Regulacion \n\t (2) Tracking")   
            target_constraints = input("Ingrese el numero(1/2):")
            if target_constraints == "1":
                print( " \nControlador MPC Regulacion. Resultados: ")
                template = env.get_template("python_cvxpy_mpcr.py")
                rendered_template = template.render(A=Datos.A, B=Datos.B, x0=Datos.x0, N=Datos.N, Q=Datos.Q, R=Datos.R, P=Datos.P,xmax=Datos.xmax,xmin=Datos.xmin,umax=Datos.umax,umin=Datos.umin)
            
            if target_constraints == "2":
                print( " \nControlador MPC Tracking. Resultados: ")
                template = env.get_template("python_cvxpy_mpct.py")
                rendered_template = template.render(A=Datos.A, B=Datos.B, x0=Datos.x0, N=Datos.N, Q=Datos.Q, R=Datos.R, P=Datos.P, xmax=Datos.xmax, xmin=Datos.xmin, umax=Datos.umax, umin=Datos.umin, xref=Datos.xref, uref=Datos.uref)

        else: 
            print("\nError: El problema de destino NO esta bien definido\n ")
                
    elif target_library == "pyomo":
        if target_problem == "QP":
            template_loader = FileSystemLoader(searchpath="QP")
            env = Environment(loader=template_loader)
            print("\nEl problema tiene restricciones:\n\t (1) NO \n\t (2) Solo restricciones de desigualdad \n\t (3) Solo restricciones lineales \n\t (4) Ambas")    
            target_constraints = input("Ingrese las restricciones(1/2/3/4):")

            if target_constraints == "1":
                template = env.get_template("Python_pyomo_QP_NoRestricciones.py")
                rendered_template = template.render(Q=Datos.Q, c=Datos.c, n=Datos.n)

            elif target_constraints == "2" : 
                template = env.get_template("Python_pyomo_QP_RestDesigualdad.py")
                rendered_template = template.render(Q=Datos.Q, c=Datos.c, n=Datos.n, p=Datos.p, G=Datos.G, h=Datos.h)

            elif target_constraints == "3" :
                template = env.get_template("Python_pyomo_QP_RestLineales.py")
                rendered_template = template.render(Q=Datos.Q, c=Datos.c, n=Datos.n, m=Datos.m, A=Datos.A, b=Datos.b)

            elif target_constraints == "4" :
                template = env.get_template("Python_pyomo_QP_Restricciones.py")
                rendered_template = template.render(Q=Datos.Q, c=Datos.c, n=Datos.n, m=Datos.m, A=Datos.A, b=Datos.b, p=Datos.p, G=Datos.G, h=Datos.h)
    
        if target_problem == "MPC":
            template_loader = FileSystemLoader(searchpath="MPC")
            env = Environment(loader=template_loader)
            
            ############################################################################ 
            # AÑADIR PLANTILLAS DE PYOMO PARA MPC 
            ############################################################################
        
        else: 
            print("\nError: El problema de destino NO esta bien definido\n ")       
    else:
        print("\nError: La librería de destino NO esta bien definido\n ")
            
elif target_language == "micropython":
    if target_problem == "MPC":
        template_loader = FileSystemLoader(searchpath="MPC")
        env = Environment(loader=template_loader)
        print("\nElige el tipo de MPC: \n\t (1) Regulacion \n\t (2) Tracking")   
        target_constraints = input("Ingrese el numero(1/2):")
        if target_constraints == "1":
            print( " \nControlador MPC Regulacion. Resultados: ")
            template = env.get_template("micropython_mpcr.py")
            rendered_template = template.render(A=Datos.A, B=Datos.B, x0=Datos.x0, N=Datos.N, Q=Datos.Q, R=Datos.R, P=Datos.P,xmax=Datos.xmax,xmin=Datos.xmin,umax=Datos.umax,umin=Datos.umin)       
        
        if target_constraints == "2":
            print( " \nControlador MPC Tracking. Resultados: ")
            template = env.get_template("micropython_mpct.py")
            rendered_template = template.render(A=Datos.A, B=Datos.B, x0=Datos.x0, N=Datos.N, Q=Datos.Q, R=Datos.R, P=Datos.P, xmax=Datos.xmax, xmin=Datos.xmin, umax=Datos.umax, umin=Datos.umin, xref=Datos.xref, uref=Datos.uref)

else: 
    print("\nError: EL lenguaje de destino NO esta bien definido\n ")

# Ejecutar el código generado
exec(rendered_template)

# Exportar el código generado a un archivo
with open("Controlador.py", "w") as output_file:
    output_file.write(rendered_template)
    
if target_language == "python":
    print("\nArchivo exportado correctamente (Controlador.py).")
elif target_language == "micropython":
    print("\nPlantilla de comprobacion exportado correctamente (Controlador.py).")
    print("Matrices a exportar en wowki (mpc_qp_matrices.py).")
        

    
