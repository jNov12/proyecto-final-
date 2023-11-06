drop database mibasededatos;
create database mibasededatos;
use mibasededatos;

CREATE TABLE Productos (
    ID_Producto INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255),
    Stock INT,
    Precio DOUBLE,
    Ventas INT
);


-- Ejemplo 1
INSERT INTO Productos ( Nombre, Stock, Precio, Ventas) VALUES ('Pasta dental', 100, 29.99, 50);

-- Ejemplo 2
INSERT INTO Productos (Nombre, Stock, Precio, Ventas) VALUES ('Lacteos', 150, 19.95, 30);

-- Ejemplo 3
INSERT INTO Productos ( Nombre, Stock, Precio, Ventas) VALUES ('Embutidos', 200, 39.99, 20);

-- Ejemplo 4
INSERT INTO Productos (Nombre, Stock, Precio, Ventas) VALUES ('Cereales', 80, 49.50, 10);

-- Ejemplo 5
INSERT INTO Productos (Nombre, Stock, Precio, Ventas) VALUES ('Productos para el cabello', 120, 14.75, 45);

select * from Productos;
