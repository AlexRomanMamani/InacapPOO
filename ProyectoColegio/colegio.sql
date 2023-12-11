-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 11-12-2023 a las 17:44:16
-- Versión del servidor: 8.0.30
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `colegio`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acceso`
--

CREATE TABLE `acceso` (
  `codigo_acceso` int NOT NULL,
  `nombre_acceso` varchar(15) NOT NULL,
  `activo_acceso` tinyint NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `acceso`
--

INSERT INTO `acceso` (`codigo_acceso`, `nombre_acceso`, `activo_acceso`) VALUES
(1, 'Administrador', 1),
(2, 'Docente', 1),
(3, 'Alumno', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumno_asignatura`
--

CREATE TABLE `alumno_asignatura` (
  `codigo_usuario` int NOT NULL,
  `codigo_asignatura` int NOT NULL,
  `nota1` decimal(2,1) DEFAULT '0.0',
  `nota2` decimal(2,1) DEFAULT '0.0',
  `nota3` decimal(2,1) DEFAULT '0.0',
  `asistencia` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `alumno_asignatura`
--

INSERT INTO `alumno_asignatura` (`codigo_usuario`, `codigo_asignatura`, `nota1`, `nota2`, `nota3`, `asistencia`) VALUES
(5, 2, 5.0, 6.0, 7.0, 60),
(5, 3, 0.0, 0.0, 0.0, 0),
(7, 2, 6.0, 6.0, 6.0, 0),
(10, 3, 0.0, 0.0, 0.0, 20),
(12, 4, 0.0, 0.0, 0.0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignatura`
--

CREATE TABLE `asignatura` (
  `codigo_asignatura` int NOT NULL,
  `nombre_asignatura` varchar(45) NOT NULL,
  `horas_asignatura` int NOT NULL,
  `activo_asignatura` tinyint NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `asignatura`
--

INSERT INTO `asignatura` (`codigo_asignatura`, `nombre_asignatura`, `horas_asignatura`, `activo_asignatura`) VALUES
(2, 'POO', 45, 1),
(3, 'Bases de Datos Relacionales', 40, 1),
(4, 'Administración', 45, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `docente_asignatura`
--

CREATE TABLE `docente_asignatura` (
  `codigo_usuario` int NOT NULL,
  `codigo_asignatura` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `docente_asignatura`
--

INSERT INTO `docente_asignatura` (`codigo_usuario`, `codigo_asignatura`) VALUES
(8, 2),
(6, 3),
(14, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `codigo_usuario` int NOT NULL,
  `nombre_usuario` varchar(20) NOT NULL,
  `apellido_usuario` varchar(20) NOT NULL,
  `nick_usuario` varchar(50) NOT NULL,
  `password_usuario` varchar(32) NOT NULL,
  `hash_password_usuario` varchar(32) NOT NULL,
  `codigo_acceso` int NOT NULL,
  `activo_usuario` tinyint NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`codigo_usuario`, `nombre_usuario`, `apellido_usuario`, `nick_usuario`, `password_usuario`, `hash_password_usuario`, `codigo_acceso`, `activo_usuario`) VALUES
(1, 'Administrador', 'Administrador', 'admin', 'admin123456', 'a66abb5684c45962d887564f08346e8d', 1, 1),
(2, 'Admin2', 'Admin2', 'admin2', 'asdasd1', 'e341450e51b6ae4f266c8963f88f825e', 1, 1),
(4, 'Admin3', 'Admin3', 'asd', 'asd', '7815696ecbf1c96e6894b779456d330e', 1, 1),
(5, 'Alex', 'Mamani', 'amamani', 'amamani', 'ae344670e57a148cfa656b37883ec8cd', 3, 1),
(6, 'Ademar', 'Araya', 'aaraya', 'aaraya', 'dad61250ab2c4e8912ec547580efbe45', 2, 1),
(7, 'Luis', 'Pinedo', 'lpinedo', 'lpinedo', '6a7a4826d22099d2c6931e106f98c895', 3, 1),
(8, 'Fernando', 'Reveco', 'freveco', 'freveco', '1ea51a2e48cceea3de0fea13cf047317', 2, 1),
(9, 'Patricio', 'Soto', 'psoto', 'psoto', 'f9b77295e98f8268d2ae937e9c073a76', 2, 1),
(10, 'Carlos', 'Perea', 'cperea', 'cperea', '8ab24d8452ecd03112fd684799669c88', 3, 1),
(11, 'Francisco', 'Vergara', 'fvergara', 'fvergara', '2324b950d0d5ebd965d4153384461301', 3, 1),
(12, 'Bastian', 'Vergara', 'bvergara', 'bvergara', '83c08162383bea710545aa6a10a73193', 3, 1),
(13, 'Luis', 'Monsalve', 'lmonsalve', 'lmonsalve', '3362157db3794a4319873f76d8c8d807', 2, 1),
(14, 'Igor', 'Caceres', 'icaceres', 'icaceres', 'ff93cdc0ea0fd21a89fed2cf408d41eb', 2, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `acceso`
--
ALTER TABLE `acceso`
  ADD PRIMARY KEY (`codigo_acceso`);

--
-- Indices de la tabla `alumno_asignatura`
--
ALTER TABLE `alumno_asignatura`
  ADD PRIMARY KEY (`codigo_usuario`,`codigo_asignatura`),
  ADD KEY `fk_alumno_asignatura_asignatura1_idx` (`codigo_asignatura`);

--
-- Indices de la tabla `asignatura`
--
ALTER TABLE `asignatura`
  ADD PRIMARY KEY (`codigo_asignatura`);

--
-- Indices de la tabla `docente_asignatura`
--
ALTER TABLE `docente_asignatura`
  ADD PRIMARY KEY (`codigo_usuario`,`codigo_asignatura`),
  ADD KEY `fk_table1_asignatura1_idx` (`codigo_asignatura`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`codigo_usuario`,`codigo_acceso`),
  ADD KEY `fk_user_access_idx` (`codigo_acceso`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `acceso`
--
ALTER TABLE `acceso`
  MODIFY `codigo_acceso` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `asignatura`
--
ALTER TABLE `asignatura`
  MODIFY `codigo_asignatura` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `codigo_usuario` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alumno_asignatura`
--
ALTER TABLE `alumno_asignatura`
  ADD CONSTRAINT `fk_alumno_asignatura_asignatura1` FOREIGN KEY (`codigo_asignatura`) REFERENCES `asignatura` (`codigo_asignatura`),
  ADD CONSTRAINT `fk_alumno_asignatura_usuario1` FOREIGN KEY (`codigo_usuario`) REFERENCES `usuario` (`codigo_usuario`);

--
-- Filtros para la tabla `docente_asignatura`
--
ALTER TABLE `docente_asignatura`
  ADD CONSTRAINT `fk_table1_asignatura1` FOREIGN KEY (`codigo_asignatura`) REFERENCES `asignatura` (`codigo_asignatura`),
  ADD CONSTRAINT `fk_table1_usuario1` FOREIGN KEY (`codigo_usuario`) REFERENCES `usuario` (`codigo_usuario`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `fk_user_access` FOREIGN KEY (`codigo_acceso`) REFERENCES `acceso` (`codigo_acceso`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
