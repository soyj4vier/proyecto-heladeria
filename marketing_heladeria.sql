-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 11-12-2025 a las 13:18:55
-- Versión del servidor: 8.3.0
-- Versión de PHP: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `marketing_heladeria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `aplicacion_reportepromocion`
--

DROP TABLE IF EXISTS `aplicacion_reportepromocion`;
CREATE TABLE IF NOT EXISTS `aplicacion_reportepromocion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre_archivo` varchar(255) COLLATE utf8mb3_spanish_ci NOT NULL,
  `fecha_generacion` datetime(6) NOT NULL,
  `promocion_id` bigint NOT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `aplicacion_reportepromocion_promocion_id_92dfba91` (`promocion_id`),
  KEY `aplicacion_reportepromocion_usuario_id_52032570` (`usuario_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb3_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb3_spanish_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add cliente', 7, 'add_cliente'),
(26, 'Can change cliente', 7, 'change_cliente'),
(27, 'Can delete cliente', 7, 'delete_cliente'),
(28, 'Can view cliente', 7, 'view_cliente'),
(29, 'Can add Promocion', 8, 'add_promocion'),
(30, 'Can change Promocion', 8, 'change_promocion'),
(31, 'Can delete Promocion', 8, 'delete_promocion'),
(32, 'Can view Promocion', 8, 'view_promocion'),
(33, 'Can add Producto', 9, 'add_producto'),
(34, 'Can change Producto', 9, 'change_producto'),
(35, 'Can delete Producto', 9, 'delete_producto'),
(36, 'Can view Producto', 9, 'view_producto'),
(37, 'Can add Tipo Promocion', 10, 'add_tipodescuento'),
(38, 'Can change Tipo Promocion', 10, 'change_tipodescuento'),
(39, 'Can delete Tipo Promocion', 10, 'delete_tipodescuento'),
(40, 'Can view Tipo Promocion', 10, 'view_tipodescuento'),
(41, 'Can add Producto en promoción', 11, 'add_productopromocion'),
(42, 'Can change Producto en promoción', 11, 'change_productopromocion'),
(43, 'Can delete Producto en promoción', 11, 'delete_productopromocion'),
(44, 'Can view Producto en promoción', 11, 'view_productopromocion'),
(45, 'Can add Detalle promocion', 12, 'add_detallepromocion'),
(46, 'Can change Detalle promocion', 12, 'change_detallepromocion'),
(47, 'Can delete Detalle promocion', 12, 'delete_detallepromocion'),
(48, 'Can view Detalle promocion', 12, 'view_detallepromocion'),
(49, 'Can add Movimiento puntos', 13, 'add_movimientopuntos'),
(50, 'Can change Movimiento puntos', 13, 'change_movimientopuntos'),
(51, 'Can delete Movimiento puntos', 13, 'delete_movimientopuntos'),
(52, 'Can view Movimiento puntos', 13, 'view_movimientopuntos'),
(53, 'Can add reporte promocion', 14, 'add_reportepromocion'),
(54, 'Can change reporte promocion', 14, 'change_reportepromocion'),
(55, 'Can delete reporte promocion', 14, 'delete_reportepromocion'),
(56, 'Can view reporte promocion', 14, 'view_reportepromocion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb3_spanish_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb3_spanish_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb3_spanish_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb3_spanish_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb3_spanish_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$mpVMSTDmq7nlRUPjbRTH1k$byPN8Dyl9EXafINMEknv2DtSUgEln9GzKp+l6/fLDts=', '2025-12-11 02:20:17.864155', 1, 'administrador', '', '', 'admin@mail.com', 1, 1, '2025-10-06 00:02:34.282258'),
(2, 'pbkdf2_sha256$600000$oXXkS7VrdMSLdxRZHXcIp8$lNktXZoMg9dnNJE/w9LPECG7CUJEWrem9PIzbshFk8Y=', '2025-11-29 22:11:11.923248', 0, 'Javier', 'Javier', 'Pérez', 'javier.perez80@inacapmail.cl', 0, 1, '2025-11-29 22:10:04.000000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

DROP TABLE IF EXISTS `cliente`;
CREATE TABLE IF NOT EXISTS `cliente` (
  `run` int NOT NULL,
  `nombre` varchar(30) COLLATE utf8mb3_spanish_ci NOT NULL,
  `apellido_paterno` varchar(30) COLLATE utf8mb3_spanish_ci NOT NULL,
  `apellido_materno` varchar(30) COLLATE utf8mb3_spanish_ci NOT NULL,
  `puntos` int NOT NULL,
  PRIMARY KEY (`run`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`run`, `nombre`, `apellido_paterno`, `apellido_materno`, `puntos`) VALUES
(123456789, 'javier', 'pérez', 'villalobos', 15),
(123456780, 'pedro', 'gómez', 'zambra', 0),
(113456789, 'felipe', 'toro', 'varela', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb3_spanish_ci,
  `object_repr` varchar(200) COLLATE utf8mb3_spanish_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8mb3_spanish_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2025-10-06 00:08:02.530865', '10', 'Estado de la promocion True, empezo 2025-10-05 y terminará 2025-10-15', 1, '[{\"added\": {}}]', 8, 1),
(2, '2025-10-06 00:08:58.475516', '10', 'Descuento año nuevo', 1, '[{\"added\": {}}]', 10, 1),
(3, '2025-10-07 20:40:00.251271', '123456789', 'El cliente 123456789 tiene la cantidad de puntos de: 34567', 1, '[{\"added\": {}}]', 7, 1),
(4, '2025-10-07 20:41:19.837230', '22', 'El cliente Vicky Tiene -67 a la fecha de 2025-10-07 20:41:19.831852+00:00', 1, '[{\"added\": {}}]', 13, 1),
(5, '2025-10-07 20:41:39.837155', '17', 'El producto ingresado es Producto y el precio es 308765', 1, '[{\"added\": {}}]', 9, 1),
(6, '2025-10-07 20:42:48.072559', '11', 'Estado de la promocion True, empezo 2025-10-07 y terminará 2025-10-24', 1, '[{\"added\": {}}]', 8, 1),
(7, '2025-10-07 20:43:04.412047', '17', 'ProductoPromocion object (17)', 1, '[{\"added\": {}}]', 11, 1),
(8, '2025-10-07 20:44:08.444693', '11', 'Estado de la promocion True, empezo 2025-10-07 y terminará 2025-10-24 - 1098', 1, '[{\"added\": {}}]', 12, 1),
(9, '2025-11-05 03:20:55.799319', '23', 'El cliente Vicky Tiene -7 a la fecha de 2025-11-05 03:20:55.790005+00:00', 1, '[{\"added\": {}}]', 13, 1),
(10, '2025-11-29 22:10:05.312034', '2', 'Javier', 1, '[{\"added\": {}}]', 4, 1),
(11, '2025-11-29 22:10:27.956340', '2', 'Javier', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\"]}}]', 4, 1),
(12, '2025-12-11 03:40:48.076905', '51', 'El producto ingresado es descuento año nuevo y el precio es 5000', 3, '', 9, 1),
(13, '2025-12-11 03:40:48.081906', '50', 'El producto ingresado es café helado y el precio es 1800', 3, '', 9, 1),
(14, '2025-12-11 03:40:48.081906', '49', 'El producto ingresado es jugo natural y el precio es 1200', 3, '', 9, 1),
(15, '2025-12-11 03:40:48.082908', '48', 'El producto ingresado es paleta artesanal y el precio es 900', 3, '', 9, 1),
(16, '2025-12-11 03:40:48.082908', '47', 'El producto ingresado es galleta helada y el precio es 1500', 3, '', 9, 1),
(17, '2025-12-11 03:40:48.082908', '46', 'El producto ingresado es brownie helado y el precio es 2800', 3, '', 9, 1),
(18, '2025-12-11 03:40:48.083908', '45', 'El producto ingresado es smoothie tropical y el precio es 2000', 3, '', 9, 1),
(19, '2025-12-11 03:40:48.083908', '44', 'El producto ingresado es copa helada y el precio es 1800', 3, '', 9, 1),
(20, '2025-12-11 03:40:48.083908', '43', 'El producto ingresado es banana split y el precio es 3500', 3, '', 9, 1),
(21, '2025-12-11 03:40:48.084905', '42', 'El producto ingresado es milkshake frutilla y el precio es 2600', 3, '', 9, 1),
(22, '2025-12-11 03:40:48.084905', '41', 'El producto ingresado es milkshake chocolate y el precio es 2600', 3, '', 9, 1),
(23, '2025-12-11 03:40:48.084905', '40', 'El producto ingresado es milkshake vainilla y el precio es 2500', 3, '', 9, 1),
(24, '2025-12-11 03:40:48.084905', '39', 'El producto ingresado es topping frutilla y el precio es 200', 3, '', 9, 1),
(25, '2025-12-11 03:40:48.085904', '38', 'El producto ingresado es topping chocolate y el precio es 200', 3, '', 9, 1),
(26, '2025-12-11 03:40:48.085904', '37', 'El producto ingresado es topping manjar y el precio es 200', 3, '', 9, 1),
(27, '2025-12-11 03:40:48.085904', '36', 'El producto ingresado es barquillo doble y el precio es 500', 3, '', 9, 1),
(28, '2025-12-11 03:40:48.085904', '35', 'El producto ingresado es barquillo simple y el precio es 300', 3, '', 9, 1),
(29, '2025-12-11 03:40:48.086904', '34', 'El producto ingresado es helado mixto y el precio es 1300', 3, '', 9, 1),
(30, '2025-12-11 03:40:48.086904', '33', 'El producto ingresado es helado de vainilla y el precio es 1000', 3, '', 9, 1),
(31, '2025-12-11 03:40:48.086904', '32', 'El producto ingresado es helado de frutilla y el precio es 1100', 3, '', 9, 1),
(32, '2025-12-11 03:40:48.086904', '31', 'El producto ingresado es helado de chocolate y el precio es 1200', 3, '', 9, 1),
(33, '2025-12-11 03:40:48.087906', '30', 'El producto ingresado es Helado de piña y el precio es 1000', 3, '', 9, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'aplicacion', 'cliente'),
(8, 'aplicacion2', 'promocion'),
(9, 'aplicacion2', 'producto'),
(10, 'aplicacion2', 'tipodescuento'),
(11, 'aplicacion2', 'productopromocion'),
(12, 'aplicacion2', 'detallepromocion'),
(13, 'aplicacion', 'movimientopuntos'),
(14, 'aplicacion', 'reportepromocion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb3_spanish_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb3_spanish_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-10-06 00:00:43.694440'),
(2, 'auth', '0001_initial', '2025-10-06 00:00:44.610231'),
(3, 'admin', '0001_initial', '2025-10-06 00:00:44.917568'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-10-06 00:00:44.938252'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-10-06 00:00:44.944784'),
(6, 'aplicacion', '0001_initial', '2025-10-06 00:00:44.955263'),
(7, 'aplicacion', '0002_alter_cliente_options', '2025-10-06 00:00:44.959267'),
(8, 'aplicacion2', '0001_initial', '2025-10-06 00:00:44.973388'),
(9, 'aplicacion2', '0002_producto_tipodescuento_alter_promocion_options_and_more', '2025-10-06 00:00:45.505073'),
(10, 'contenttypes', '0002_remove_content_type_name', '2025-10-06 00:00:45.596123'),
(11, 'auth', '0002_alter_permission_name_max_length', '2025-10-06 00:00:45.646010'),
(12, 'auth', '0003_alter_user_email_max_length', '2025-10-06 00:00:45.696247'),
(13, 'auth', '0004_alter_user_username_opts', '2025-10-06 00:00:45.707559'),
(14, 'auth', '0005_alter_user_last_login_null', '2025-10-06 00:00:45.766979'),
(15, 'auth', '0006_require_contenttypes_0002', '2025-10-06 00:00:45.768979'),
(16, 'auth', '0007_alter_validators_add_error_messages', '2025-10-06 00:00:45.775982'),
(17, 'auth', '0008_alter_user_username_max_length', '2025-10-06 00:00:45.826512'),
(18, 'auth', '0009_alter_user_last_name_max_length', '2025-10-06 00:00:45.865577'),
(19, 'auth', '0010_alter_group_name_max_length', '2025-10-06 00:00:45.909839'),
(20, 'auth', '0011_update_proxy_permissions', '2025-10-06 00:00:45.922840'),
(21, 'auth', '0012_alter_user_first_name_max_length', '2025-10-06 00:00:45.971158'),
(22, 'sessions', '0001_initial', '2025-10-06 00:00:46.022398'),
(23, 'aplicacion', '0003_movimientopuntos', '2025-10-06 01:22:02.792077'),
(24, 'aplicacion', '0004_alter_cliente_options_alter_movimientopuntos_options', '2025-11-26 00:38:15.493689'),
(25, 'aplicacion2', '0003_promocion_usos', '2025-11-26 00:38:15.577630'),
(26, 'aplicacion', '0005_alter_cliente_table_reportepromocion', '2025-11-26 01:26:02.197500'),
(27, 'aplicacion2', '0004_alter_detallepromocion_valor_descuento_and_more', '2025-12-08 21:35:22.218272'),
(28, 'aplicacion2', '0005_remove_productopromocion_producto_and_more', '2025-12-11 03:01:58.365118');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8mb3_spanish_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb3_spanish_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2s9uvk5lj4j78rrpmruc7lnxp49d8n35', '.eJxVjMEOwiAQBf-FsyHQAgsevfcbCAuLVA0kpT0Z_9026UGvb2bem_mwrcVvnRY_J3Zlkl1-NwzxSfUA6RHqvfHY6rrMyA-Fn7TzqSV63U7376CEXvbaAKkEVojB2TyCVmgNksouQDbBAOqIkAeNIhk3ktAjkNgTl6XUxlr2-QLTqzdo:1v6E9P:zJ2aX-43NpkDmTQ02ZTfOUEicaIjpHP3ldNVv0lLMFE', '2025-10-21 20:19:11.337242'),
('g4d59ariu4qv0mu3reyifvsd6v7v8cc5', '.eJxVjEEOwiAQRe_C2pBCQQaX7nsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3ERSpx-N8L44LqDdMd6azK2ui4zyV2RB-1yaomf18P9OyjYy7eONjPlIdEQQQEAeuNAY2Kk0SqXwers2aJhfybvnQcyoyVtWRljlBLvD_zGN7w:1vRfPo:kMydTm7jjfYjnUE5o7gKFRTQlcRHeo5u0cZpRxQbJbE', '2025-12-19 23:40:44.553253'),
('w9dn2s2a1n9gvixdcdw8uvgikvtlo2kr', '.eJxVjEEOwiAQRe_C2pBCQQaX7nsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3ERSpx-N8L44LqDdMd6azK2ui4zyV2RB-1yaomf18P9OyjYy7eONjPlIdEQQQEAeuNAY2Kk0SqXwers2aJhfybvnQcyoyVtWRljlBLvD_zGN7w:1vKPeC:Qw29kUKPANea3USKxZLHdzghvzbXbRCFI8cvO01LaTg', '2025-11-29 23:25:36.001221'),
('lzm731emz03vwj38sv0u8s7y3mewsnsw', '.eJxVjEEOwiAQRe_C2pBCQQaX7nsGMgODVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3ERSpx-N8L44LqDdMd6azK2ui4zyV2RB-1yaomf18P9OyjYy7eONjPlIdEQQQEAeuNAY2Kk0SqXwers2aJhfybvnQcyoyVtWRljlBLvD_zGN7w:1vTWHx:PTNv66-agPHVjeav4ntBM-ajd6Rl1IX-bvtK7mVJETs', '2025-12-25 02:20:17.874175');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `movimiento_puntos`
--

DROP TABLE IF EXISTS `movimiento_puntos`;
CREATE TABLE IF NOT EXISTS `movimiento_puntos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `puntos` int NOT NULL,
  `descripcion` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  `cliente_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `movimiento_puntos_cliente_id_7cddf5bb` (`cliente_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `movimiento_puntos`
--

INSERT INTO `movimiento_puntos` (`id`, `fecha`, `puntos`, `descripcion`, `cliente_id`) VALUES
(1, '2025-12-11 13:15:52.325820', 15, 'Transacción con promoción \'descuento 2x1\' y producto \'café helado\'', 123456789);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

DROP TABLE IF EXISTS `producto`;
CREATE TABLE IF NOT EXISTS `producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8mb3_spanish_ci NOT NULL,
  `precio` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id`, `nombre`, `precio`) VALUES
(1, 'café helado', 5000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `promocion`
--

DROP TABLE IF EXISTS `promocion`;
CREATE TABLE IF NOT EXISTS `promocion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8mb3_spanish_ci NOT NULL,
  `descripcion` longtext COLLATE utf8mb3_spanish_ci NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `usos` int NOT NULL,
  `codigo_promocional` varchar(20) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `tipo_descuento` varchar(10) COLLATE utf8mb3_spanish_ci NOT NULL,
  `valor_descuento` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `promocion`
--

INSERT INTO `promocion` (`id`, `nombre`, `descripcion`, `fecha_inicio`, `fecha_fin`, `activo`, `usos`, `codigo_promocional`, `tipo_descuento`, `valor_descuento`) VALUES
(1, 'descuento año nuevo', 'solo aplica en año nuevo', '2025-12-31', '2026-01-03', 1, 0, '111', 'dinero', 500),
(2, 'descuento 2x1', 'si lleva dos de un producto paga uno', '2025-12-12', '2025-12-17', 1, 1, '112', 'dinero', 300);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
