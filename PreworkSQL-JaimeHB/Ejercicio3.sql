/*1. Crea una tabla llamada "Productos" con las columnas: "id" (entero, clave primaria), "nombre" (texto) y "precio" (numérico).*/
CREATE TABLE public.Productos (
    id INT PRIMARY KEY,
    nombre TEXT,
    precio NUMERIC
)
/*2. Inserta al menos cinco registros en la tabla "Productos".*/
INSERT INTO public.Productos (id, nombre, precio) VALUES
(1, 'Camiseta', 15.99),
(2, 'Pantalones', 29.99),
(3, 'Zapatos', 49.99),
(4, 'Sombrero', 9.99),
(5, 'Calcetines', 5.99);

/*3. Actualiza el precio de un producto en la tabla "Productos".*/
UPDATE public.Productos
SET precio = 34.99
WHERE id = 2;

/*4. Elimina un producto de la tabla "Productos".*/
DELETE FROM public.Productos
WHERE id = 4

/*5. Realiza una consulta que muestre los nombres de los usuarios junto con los nombres de los productos que han comprado (utiliza un INNER JOIN con la tabla "Productos").*/
SELECT usuarios.nombre, productos.nombre
FROM public.usuarios
INNER JOIN public.productos
ON usuarios.id=productos.id

