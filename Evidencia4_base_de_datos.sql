
CREATE TABLE Conectividad (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL
);

CREATE TABLE Tipo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL
);

CREATE TABLE NivelTinta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nivel VARCHAR(50) NOT NULL
);

CREATE TABLE PapelTipo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL
);

CREATE TABLE Impresora (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estado INT NOT NULL,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    tipo_id INT,
    conectividad_id INT,
    nivel_tinta_id INT,
    paginas_impresas INT,
    papel_tipo_id INT,
    FOREIGN KEY (tipo_id) REFERENCES Tipo(id),
    FOREIGN KEY (conectividad_id) REFERENCES Conectividad(id),
    FOREIGN KEY (nivel_tinta_id) REFERENCES NivelTinta(id),
    FOREIGN KEY (papel_tipo_id) REFERENCES PapelTipo(id)
);

-- Insertar datos en la tabla Conectividad
INSERT INTO Conectividad (tipo) VALUES ('WiFi');
INSERT INTO Conectividad (tipo) VALUES ('USB');
INSERT INTO Conectividad (tipo) VALUES ('Bluetooth');

-- Insertar datos en la tabla Tipo
INSERT INTO Tipo (tipo) VALUES ('Laser');
INSERT INTO Tipo (tipo) VALUES ('Inkjet');

-- Insertar datos en la tabla NivelTinta
INSERT INTO NivelTinta (nivel) VALUES ('Alto');
INSERT INTO NivelTinta (nivel) VALUES ('Medio');
INSERT INTO NivelTinta (nivel) VALUES ('Bajo');

-- Insertar datos en la tabla PapelTipo
INSERT INTO PapelTipo (tipo) VALUES ('A4');
INSERT INTO PapelTipo (tipo) VALUES ('A3');
INSERT INTO PapelTipo (tipo) VALUES ('Carta');

-- Insertar datos en la tabla Impresora
INSERT INTO Impresora (estado, marca, modelo, tipo_id, conectividad_id, nivel_tinta_id, paginas_impresas, papel_tipo_id)
VALUES (1, 'Epson', 'L365', 1, 1, 2, 150, 1);

INSERT INTO Impresora (estado, marca, modelo, tipo_id, conectividad_id, nivel_tinta_id, paginas_impresas, papel_tipo_id)
VALUES (2, 'HP', 'OfficeJet Pro', 2, 2, 1, 200, 1);

INSERT INTO Impresora (estado, marca, modelo, tipo_id, conectividad_id, nivel_tinta_id, paginas_impresas, papel_tipo_id)
VALUES (3, 'Canon', 'Pixma', 2, 3, 3, 75, 2);

INSERT INTO Impresora (estado, marca, modelo, tipo_id, conectividad_id, nivel_tinta_id, paginas_impresas, papel_tipo_id)
VALUES (4, 'Brother', 'HL-L2350DW', 1, 1, 1, 500, 3);

INSERT INTO Impresora (estado, marca, modelo, tipo_id, conectividad_id, nivel_tinta_id, paginas_impresas, papel_tipo_id)
VALUES (5, 'Samsung', 'Xpress M2020W', 1, 2, 2, 300, 1);


-- Consultas Sql
SELECT * FROM impresora

SELECT estado AS Estado_de_funcionamiento, marca, modelo FROM Impresora
SELECT * FROM Impresora WHERE modelo LIKE "L%" AND estado = 1
SELECT i.marca, i.modelo, c.tipo FROM impresora i JOIN conectividad c ON i.id = c.id
SELECT marca, paginas_impresas FROM impresora WHERE paginas_impresas >= 200

SELECT * FROM papelTipo
SELECT i.marca, i.modelo, p.tipo FROM impresora i JOIN papelTipo p ON i.id = p.id





