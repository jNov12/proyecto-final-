import tkinter
from tkinter import messagebox
from data import AgregarProducto,ObtenerTablaProductos,BorrarProducto
from tkinter import ttk

principal=tkinter.Tk()
def inicio():
    principal.title("Menu Principal")
    principal.geometry("500x200")

    # Etiqueta y campo de entrada para el Nombre de Usuario
    label_usuario = tkinter.Label(principal, text="Usuario:")
    label_usuario.pack()
    usuario_entry = tkinter.Entry(principal)
    usuario_entry.pack()

    # Etiqueta y campo de entrada para la Contraseña
    label_contrasena = tkinter.Label(principal, text="Contraseña:")
    label_contrasena.pack()
    contrasena_entry = tkinter.Entry(principal, show="*")
    contrasena_entry.pack()

 
    def verificar_credenciales():
        usuario = usuario_entry.get()
        contrasena = contrasena_entry.get()
        print(usuario, contrasena)
        
        if usuario=="admin" and contrasena=="admin":
            VentanaAdmin()
        elif usuario=="user" and contrasena=="user":
            VentanaUser()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")    
            


        usuario_entry.delete(0, "end")
        contrasena_entry.delete(0, "end")
        
        


    salir=tkinter.Button(principal,text="Login",command=verificar_credenciales)
    salir.place(x=230,y=100)

    principal.mainloop()




def VentanaUser():
    principal.withdraw()#sirve para la ocultar
    listar=tkinter.Tk()
    listar.title("Listar Curso")
    listar.geometry("700x500")
    


    arbol=ttk.Treeview(listar,columns=("#1","#2","#3","#4"))
    arbol.place(x=0,y=0,width=700)
    arbol.heading("#0",text="Id producto")
    arbol.column("#0",width=40)
    arbol.heading("#1",text="Nombre")
    arbol.column("#1",width=40)
    arbol.heading("#2",text="Stock")
    arbol.column("#2",width=40)
    arbol.heading("#3",text="Precio")
    arbol.column("#3",width=40)
    arbol.heading("#4",text="Ventas")
    arbol.column("#4",width=40)

    lista=ObtenerTablaProductos()
    for elem in lista:
        arbol.insert("",tkinter.END,text=elem[0],values=(elem[1],elem[2],elem[3],elem[4]))
    
    def regresar():
        principal.deiconify()
        listar.withdraw()

    logout = tkinter.Button(listar, text="Logout", command=regresar)
    logout.place(x=350,y=450)

    def update():
        # Primero, elimina todos los elementos existentes en el Treeview
        for item in arbol.get_children():
            arbol.delete(item)

        lista=ObtenerTablaProductos()
        for elem in lista:
            arbol.insert("",tkinter.END,text=elem[0],values=(elem[1],elem[2],elem[3],elem[4]))
    

    act = tkinter.Button(listar, text="Actualizar Tabla", command=update)
    act.place(x=550,y=450)


def VentanaAdmin():
    # Crear una ventana
    principal.withdraw()
    ventana = tkinter.Tk()
    ventana.title("Formulario de Producto")
    # Establecer el tamaño inicial de la ventana
    ventana.geometry("400x400")
    # Etiqueta y campo de entrada para el Nombre
    label_nombre = tkinter.Label(ventana, text="Nombre del Producto:")
    label_nombre.pack()
    entry_nombre = tkinter.Entry(ventana)
    entry_nombre.pack()

    # Etiqueta y campo de entrada para el Stock
    label_stock = tkinter.Label(ventana, text="Stock del Producto:")
    label_stock.pack()
    entry_stock = tkinter.Entry(ventana)
    entry_stock.pack()

    # Etiqueta y campo de entrada para el Precio
    label_precio = tkinter.Label(ventana, text="Precio del Producto:")
    label_precio.pack()
    entry_precio = tkinter.Entry(ventana)
    entry_precio.pack()

    def guardar_producto():
        nombre = entry_nombre.get()
        stock = entry_stock.get()
        precio = entry_precio.get()
        # Aquí puedes realizar acciones con los datos ingresados, como guardarlos en una base de datos o mostrarlos en la consola
        AgregarProducto(nombre, stock, precio)
        messagebox.showinfo("Producto", "Producto Guardado")
        entry_nombre.delete(0, "end")
        entry_stock.delete(0, "end")
        entry_precio.delete(0, "end")
    # Botón para guardar el producto
    boton_guardar = tkinter.Button(ventana, text="Guardar Producto", command=guardar_producto)
    boton_guardar.pack()

    def regresar():
        principal.deiconify()
        ventana.withdraw()

    buscarnombre = tkinter.Label(ventana, text="ID del producto:")
    buscarnombre.pack()
    entry_id = tkinter.Entry(ventana)
    entry_id.pack()

    Nom = tkinter.Label(ventana, text="Nombre:")
    Nom.pack()
    entry_nom = tkinter.Entry(ventana)
    entry_nom.pack()


    Stock = tkinter.Label(ventana, text="Stock:")
    Stock.pack()
    entry_Stock = tkinter.Entry(ventana)
    entry_Stock.pack()


    precio = tkinter.Label(ventana, text="Precio:")
    precio.pack()
    entry_Precio = tkinter.Entry(ventana)
    entry_Precio.pack()


    Ventas = tkinter.Label(ventana, text="Ventas:")
    Ventas.pack()
    entry_Ventas = tkinter.Entry(ventana)
    entry_Ventas.pack()


    def BuscarProducto():
        entry_nom.delete(0, "end")
        entry_Stock.delete(0, "end")
        entry_Precio.delete(0, "end")
        entry_Ventas.delete(0, "end")


        productos = ObtenerTablaProductos()
        for producto in productos:
            if producto[0] == int(entry_id.get()):
                entry_nom.insert(0,producto[1])
                entry_Stock.insert(0,producto[2])
                entry_Precio.insert(0,producto[3])
                entry_Ventas.insert(0,producto[4])
                return
            
        messagebox.showerror("Error", "Producto no encontrado")
            
    


    boton_busc = tkinter.Button(ventana, text="Buscar Produto", command=BuscarProducto)
    boton_busc.place(x=300,y=160)
    

    
    def BorrarProductos():
        BorrarProducto(int(entry_id.get()))
        messagebox.showinfo("Producto", "Producto Borrado")
        entry_nom.delete(0, "end")
        entry_Stock.delete(0, "end")
        entry_Precio.delete(0, "end")
        entry_Ventas.delete(0, "end")
    
    borrar = tkinter.Button(ventana, text="Borrar Producto",command=BorrarProductos)
    borrar.pack()

    def iraProc():
        VentanaUser()
        

    logout = tkinter.Button(ventana, text="Ver Productos", command=iraProc)
    logout.pack()

    logout = tkinter.Button(ventana, text="Logout", command=regresar)
    logout.pack()


inicio()