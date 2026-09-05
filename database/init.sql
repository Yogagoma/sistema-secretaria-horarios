-- Tabla representantes
CREATE TABLE IF NOT EXISTS Representantes(
	id INT PRIMARY KEY,
	cedula VARCHAR(10) UNIQUE,
	nombre_completo VARCHAR(70) NOT NULL,
	telefono VARCHAR(20) NOT NULL,
	direccion VARCHAR(70) NOT NULL
);


-- Tabla alumnos
CREATE TABLE IF NOT EXISTS Alumnos(
	ID_alumno INT PRIMARY KEY,
	CI_representante VARCHAR(10),
	cedula_escolar VARCHAR(20) UNIQUE NOT NULL,
	nombre_completo VARCHAR(70) NOT NULL,
	fecha_nacimiento DATE NOT NULL,
	grado INT,
	seccion VARCHAR(1),

	-- Restriccion de grado
	CONSTRAINT anio CHECK(grado >= 1 AND grado <= 6),
	
	-- Rango de secciones(Desde la A hasta la D)
	CONSTRAINT letra_seccion CHECK(seccion IN ('A', 'B', 'C', 'D')),

	-- Clave foranea: Cedula del representante establece relacion 1:N entre representante y alumno
	CONSTRAINT cedula_representante FOREIGN KEY(CI_representante) REFERENCES Representantes(cedula)
);

-- Tabla profesores
CREATE TABLE IF NOT EXISTS Profesores(
	ID_profesor INT PRIMARY KEY,
	cedula VARCHAR(10) UNIQUE,
	nombre_completo VARCHAR(70) NOT NULL,
	especialidad VARCHAR(20) NOT NULL,
	telefono VARCHAR(20) NOT NULL,
	salario_base DECIMAL(6,2),

	-- Validacion de salario
	CONSTRAINT chk_salario CHECK(salario_base >= 0)
);

-- Tabla materias
CREATE TABLE Materias(
	ID_materia INT PRIMARY KEY,
	nombre VARCHAR(30) UNIQUE NOT NULL
);

-- Tabla puente para relacion N:M entre alumno y materia
CREATE TABLE alumno_cursa_materia(
	CI_alumno VARCHAR(20),
	ID_materia INT,
	periodo_escolar VARCHAR(10) NOT NULL,
	grado INT,
	seccion VARCHAR(1),

	-- Clave primaria compuesta: Un alumno puede ver varias materias en un periodo
	PRIMARY KEY (CI_alumno, ID_materia, periodo_escolar),

	-- Relaciones
	CONSTRAINT FK_Alumno FOREIGN KEY (CI_alumno) REFERENCES Alumnos(cedula_escolar),
	CONSTRAINT FK_Materia FOREIGN KEY (ID_materia) REFERENCES Materias(ID_materia)
);

-- Tabla puente para relacion N:M entre profesor y materia
CREATE TABLE profesor_imparte_materia(
	CI_profesor VARCHAR(10),
	ID_materia INT,
	grado INT,
	seccion VARCHAR(1),

	-- Clave primaria compuesta: Un profesor puede dar varias materias/grados/secciones
	PRIMARY KEY (CI_profesor, ID_materia, grado, seccion),

	-- Relaciones
	CONSTRAINT FK_Profesor FOREIGN KEY (CI_profesor) REFERENCES Profesores(cedula),
	CONSTRAINT FK_Materia_profesor FOREIGN KEY (ID_materia) REFERENCES Materias(ID_materia)
);

