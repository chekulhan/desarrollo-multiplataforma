-- =========================================================
-- ERP SIMPLE DEMO - POSTGRESQL
-- Flujo:
-- Confirmar pedido
--   ↓
-- Reservar stock
--   ↓
-- Si no hay stock:
--   generar compra o fabricación
--   ↓
-- Crear tareas logísticas
--   ↓
-- Registrar auditoría
-- =========================================================

-- =========================================================
-- LIMPIEZA
-- =========================================================

DROP TABLE IF EXISTS auditoria CASCADE;
DROP TABLE IF EXISTS tareas_logisticas CASCADE;
DROP TABLE IF EXISTS ordenes_fabricacion CASCADE;
DROP TABLE IF EXISTS necesidades_compra CASCADE;
DROP TABLE IF EXISTS lineas_pedido CASCADE;
DROP TABLE IF EXISTS pedidos CASCADE;
DROP TABLE IF EXISTS stock CASCADE;
DROP TABLE IF EXISTS productos CASCADE;
DROP TABLE IF EXISTS clientes CASCADE;

-- =========================================================
-- TABLAS
-- =========================================================

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    ciudad VARCHAR(100)
);

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    tipo VARCHAR(50),
    precio NUMERIC(10,2)
);

CREATE TABLE stock (
    producto_id INT PRIMARY KEY REFERENCES productos(id),
    stock_total INT,
    stock_reservado INT DEFAULT 0
);

CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id),
    fecha DATE,
    estado VARCHAR(30) DEFAULT 'BORRADOR'
);

CREATE TABLE lineas_pedido (
    id SERIAL PRIMARY KEY,
    pedido_id INT REFERENCES pedidos(id),
    producto_id INT REFERENCES productos(id),
    cantidad INT
);

CREATE TABLE necesidades_compra (
    id SERIAL PRIMARY KEY,
    producto_id INT REFERENCES productos(id),
    cantidad INT,
    fecha DATE DEFAULT CURRENT_DATE,
    estado VARCHAR(30) DEFAULT 'PENDIENTE'
);

CREATE TABLE ordenes_fabricacion (
    id SERIAL PRIMARY KEY,
    producto_id INT REFERENCES productos(id),
    cantidad INT,
    fecha DATE DEFAULT CURRENT_DATE,
    estado VARCHAR(30) DEFAULT 'PENDIENTE'
);

CREATE TABLE tareas_logisticas (
    id SERIAL PRIMARY KEY,
    pedido_id INT REFERENCES pedidos(id),
    descripcion TEXT,
    estado VARCHAR(30) DEFAULT 'PENDIENTE'
);

CREATE TABLE auditoria (
    id SERIAL PRIMARY KEY,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    accion TEXT,
    detalle TEXT
);

-- =========================================================
-- DATOS EJEMPLO
-- =========================================================

INSERT INTO clientes (nombre, ciudad) VALUES
('Talleres Garcia', 'Vitoria'),
('Metal Norte', 'Bilbao'),
('Industrial Euskadi', 'Donostia');

INSERT INTO productos (nombre, tipo, precio) VALUES
('Maquina CNC X200', 'FABRICACION', 25000),
('Torno Industrial T500', 'FABRICACION', 18000),
('Taladro Industrial Z100', 'STOCK', 4500);

INSERT INTO stock (producto_id, stock_total, stock_reservado) VALUES
(1, 1, 0),
(2, 0, 0),
(3, 10, 2);

INSERT INTO pedidos (cliente_id, fecha, estado) VALUES
(1, CURRENT_DATE, 'BORRADOR'),
(2, CURRENT_DATE, 'BORRADOR'),
(3, CURRENT_DATE, 'BORRADOR');

INSERT INTO lineas_pedido (pedido_id, producto_id, cantidad) VALUES
(1, 1, 2),
(2, 2, 1),
(3, 3, 3);

-- =========================================================
-- PROCEDIMIENTO:
-- CONFIRMAR PEDIDO
-- =========================================================

CREATE OR REPLACE PROCEDURE confirmar_pedido(p_pedido_id INT)
LANGUAGE plpgsql
AS $$
DECLARE
    v_producto_id INT;
    v_cantidad INT;
    v_stock_disponible INT;
BEGIN

    -- Cambiar estado pedido
    UPDATE pedidos
    SET estado = 'CONFIRMADO'
    WHERE id = p_pedido_id;

    -- Recorrer líneas pedido
    FOR v_producto_id, v_cantidad IN
        SELECT producto_id, cantidad
        FROM lineas_pedido
        WHERE pedido_id = p_pedido_id
    LOOP

        -- Calcular stock disponible
        SELECT (stock_total - stock_reservado)
        INTO v_stock_disponible
        FROM stock
        WHERE producto_id = v_producto_id;

        -- =================================================
        -- SI HAY STOCK → RESERVAR
        -- =================================================

        IF v_stock_disponible >= v_cantidad THEN

            UPDATE stock
            SET stock_reservado = stock_reservado + v_cantidad
            WHERE producto_id = v_producto_id;

            INSERT INTO auditoria (accion, detalle)
            VALUES (
                'RESERVA STOCK',
                'Producto ' || v_producto_id ||
                ' reservado cantidad ' || v_cantidad
            );

        -- =================================================
        -- SI NO HAY STOCK → GENERAR FABRICACION
        -- =================================================

        ELSE

            INSERT INTO ordenes_fabricacion (
                producto_id,
                cantidad
            )
            VALUES (
                v_producto_id,
                v_cantidad
            );

            INSERT INTO auditoria (accion, detalle)
            VALUES (
                'GENERAR FABRICACION',
                'Producto ' || v_producto_id ||
                ' cantidad ' || v_cantidad
            );

        END IF;

    END LOOP;

    -- =====================================================
    -- CREAR TAREA LOGISTICA
    -- =====================================================

    INSERT INTO tareas_logisticas (
        pedido_id,
        descripcion
    )
    VALUES (
        p_pedido_id,
        'Preparar expedicion del pedido'
    );

    -- =====================================================
    -- AUDITORIA FINAL
    -- =====================================================

    INSERT INTO auditoria (accion, detalle)
    VALUES (
        'CONFIRMAR PEDIDO',
        'Pedido ' || p_pedido_id || ' confirmado'
    );

END;
$$;

-- =========================================================
-- TRIGGER:
-- AUDITORIA CAMBIO ESTADO PEDIDO
-- =========================================================

CREATE OR REPLACE FUNCTION trg_auditoria_estado_pedido()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

    INSERT INTO auditoria (accion, detalle)
    VALUES (
        'CAMBIO ESTADO',
        'Pedido ' || NEW.id ||
        ' estado ' || OLD.estado ||
        ' -> ' || NEW.estado
    );

    RETURN NEW;

END;
$$;

CREATE TRIGGER trigger_estado_pedido
AFTER UPDATE OF estado
ON pedidos
FOR EACH ROW
EXECUTE FUNCTION trg_auditoria_estado_pedido();

-- =========================================================
-- EJEMPLO DE USO
-- =========================================================

-- Confirmar pedido 1
CALL confirmar_pedido(1);

-- Ver stock
SELECT * FROM stock;

-- Ver ordenes fabricación
SELECT * FROM ordenes_fabricacion;

-- Ver tareas logísticas
SELECT * FROM tareas_logisticas;

-- Ver auditoría
SELECT * FROM auditoria;
