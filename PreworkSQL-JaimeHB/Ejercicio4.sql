/*1. Crea una tabla llamada "Pedidos" con las columnas: "id" (entero, clave primaria), "id_usuario" (entero, clave foránea de la tabla "Usuarios") y "id_producto" (entero, clave foránea de la tabla "Productos").*/
CREATE TABLE Pedidos (
    id INT PRIMARY KEY,
    id_usuario INT,
    id_producto INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id),
    FOREIGN KEY (id_producto) REFERENCES Productos(id)
)

/*2. Inserta al menos tres registros en la tabla "Pedidos" que relacionen usuarios con productos.*/
'Creamos primero dos usuarios:'
INSERT INTO Usuarios (id, nombre, edad) VALUES
(2, 'Ana', 28),
(3, 'Carlos', 35)

'Ahora hacemos el enunciado:'
INSERT INTO Pedidos (id, id_usuario, id_producto) VALUES
(1, 1, 1),
(2, 2, 2), 
(3, 1, 3)
/*3. Realiza una consulta que muestre los nombres de los usuarios y los nombres de los productos que han comprado, incluidos aquellos que no han realizado ningún pedido (utiliza LEFT JOIN y COALESCE).
*/

SELECT Usuarios.nombre AS NombreUsuario, COALESCE(Productos.nombre, 'Sin pedido') AS NombreProducto
FROM Usuarios
LEFT JOIN Pedidos ON Usuarios.id = Pedidos.id_usuario
LEFT JOIN Productos ON Pedidos.id_producto = Productos.id;

/*4. Realiza una consulta que muestre los nombres de los usuarios que han realizado un pedido, pero también los que no han realizado ningún pedido (utiliza LEFT JOIN).*/
SELECT Usuarios.nombre AS NombreUsuario
FROM Usuarios
LEFT JOIN Pedidos ON Usuarios.id = Pedidos.id_usuario
WHERE Pedidos.id IS NOT NULL OR Pedidos.id IS NULL;

/*5. Agrega una nueva columna llamada "cantidad" a la tabla "Pedidos" y actualiza los registros existentes con un valor (utiliza ALTER TABLE y UPDATE)*/
ALTER TABLE Pedidos
ADD cantidad INT;

UPDATE Pedidos
SET cantidad = 1
