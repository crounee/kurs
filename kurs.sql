-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Дек 01 2021 г., 16:04
-- Версия сервера: 8.0.24
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `kurs`
--

-- --------------------------------------------------------

--
-- Структура таблицы `brigades`
--

CREATE TABLE `brigades` (
  `code_brigades` int NOT NULL,
  `code_employee_1` int NOT NULL,
  `code_employee_2` int NOT NULL,
  `code_employee_3` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `brigades`
--

INSERT INTO `brigades` (`code_brigades`, `code_employee_1`, `code_employee_2`, `code_employee_3`) VALUES
(1, 1, 2, 3),
(2, 3, 2, 1),
(3, 8, 2, 6),
(4, 3, 5, 8),
(5, 3, 1, 8);

-- --------------------------------------------------------

--
-- Структура таблицы `customers`
--

CREATE TABLE `customers` (
  `code_customer` int NOT NULL,
  `fio` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `adres` text NOT NULL,
  `phone` int NOT NULL,
  `passport` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `customers`
--

INSERT INTO `customers` (`code_customer`, `fio`, `adres`, `phone`, `passport`) VALUES
(1, 'Первый Заказчик', 'Ул Первого заказчика', 51354, 123456),
(2, 'Второй Заказчик', 'Ул Второго Заказчика', 53135, 24346),
(3, 'Третий Заказчик', 'Ул Третьего Заказчика', 3524245, 658234),
(4, 'Четвертый Заказчик', 'Ул Четвертых Заказчиков', 72392, 9235868),
(5, 'Пятый Заказчик', 'Ул Пятых Заказчиков', 652358, 64789632);

-- --------------------------------------------------------

--
-- Структура таблицы `materials`
--

CREATE TABLE `materials` (
  `code_material` int NOT NULL,
  `name` text NOT NULL,
  `packaging` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `coast` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `materials`
--

INSERT INTO `materials` (`code_material`, `name`, `packaging`, `description`, `coast`) VALUES
(1, 'Железо', 'Бумага', 'Железяка обычная', 1500),
(2, 'Медь', 'Бумага', 'Медь обычная', 5600),
(3, 'Дерево', 'бумага', 'Обычное дерево', 6000),
(4, 'Доски', 'бумага', 'Обычные доски', 5000),
(5, 'Алюминий', 'бумага', 'Обычный Алюминий', 4560);

-- --------------------------------------------------------

--
-- Структура таблицы `orders`
--

CREATE TABLE `orders` (
  `code_customer` int NOT NULL,
  `code_type` int NOT NULL,
  `code_brigades` int NOT NULL,
  `coast` int NOT NULL,
  `date_start` date NOT NULL,
  `date_end` date NOT NULL,
  `completion_mark` text NOT NULL,
  `pay_mark` text NOT NULL,
  `code_staff` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `orders`
--

INSERT INTO `orders` (`code_customer`, `code_type`, `code_brigades`, `coast`, `date_start`, `date_end`, `completion_mark`, `pay_mark`, `code_staff`) VALUES
(1, 1, 1, 54324, '2021-12-01', '2021-12-02', 'yes', 'yes', 4),
(2, 2, 2, 63343, '2021-12-03', '2021-12-04', 'yes', 'yes', 2),
(3, 3, 3, 62413, '2021-12-05', '2021-12-06', 'yes', 'yes', 3),
(4, 4, 4, 673134, '2021-12-08', '2021-12-09', 'yes', 'yes', 4),
(5, 5, 5, 73132, '2021-12-10', '2021-12-11', 'yes', 'yes', 5);

-- --------------------------------------------------------

--
-- Структура таблицы `positions`
--

CREATE TABLE `positions` (
  `code_position` int NOT NULL,
  `name_position` text NOT NULL,
  `salary` int NOT NULL,
  `responsibilities` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `requirements` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `positions`
--

INSERT INTO `positions` (`code_position`, `name_position`, `salary`, `responsibilities`, `requirements`) VALUES
(1, 'Грузчик', 1000, 'Грузить', 'Образование грузчика'),
(2, 'Укладчик', 1500, 'Укладывать', 'Образование укладчика'),
(3, 'Директор', 5000, 'Следить за точкой', 'Высш образование'),
(4, 'Проверщик заказов', 3000, 'Проверять заказы', 'Образование проверщика заказов'),
(5, 'Выдача заказов', 2500, 'Выдавать заказы', 'Образование Выдачи заказов');

-- --------------------------------------------------------

--
-- Структура таблицы `staff`
--

CREATE TABLE `staff` (
  `code_staff` int NOT NULL,
  `fio` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `age` int NOT NULL,
  `gender` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `adres` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `phone` int NOT NULL,
  `passport` int NOT NULL,
  `code_position` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `staff`
--

INSERT INTO `staff` (`code_staff`, `fio`, `age`, `gender`, `adres`, `phone`, `passport`, `code_position`) VALUES
(1, 'Великий Грузчик', 25, 'муж', 'ул Грузчиков', 1234, 53423, 1),
(2, 'Боб Грузчиков', 23, 'муж', 'Ул Молодых Грузчиков', 1321, 5231, 1),
(3, 'Боб Директоров', 19, 'муж', 'Ул Супер Директоров', 88888, 88888, 3),
(4, 'Василий Укладчиков', 27, 'муж', 'Ул Укладчиков', 543123, 1242435, 2),
(5, 'Арсений Проверяльщиков', 45, 'муж', 'Ул Проверяльщиков', 562133, 231432, 4),
(6, 'Эль Хмельной', 73, 'муж', 'Ул Эля', 5555, 4554, 3),
(7, 'Семен Проверяльщиков', 23, 'муж', 'Ул Проверяльщиков', 12312, 32532, 4),
(8, 'Гавриил Укладчиков', 25, 'муж', 'Ул Укладчиков', 756734, 534537, 4),
(9, 'Олег Выдавалов', 57, 'муж', 'Ул Выдавальщиков', 765324, 542345458, 5),
(10, 'Семен Выдавалов', 32, 'муж', 'Ул Выдавальщиков', 756721, 432421, 5);

-- --------------------------------------------------------

--
-- Структура таблицы `types_of_works`
--

CREATE TABLE `types_of_works` (
  `code_type` int NOT NULL,
  `name` text NOT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `coast_of_work` int NOT NULL,
  `code_material_1` int NOT NULL,
  `code_material_2` int NOT NULL,
  `code_material_3` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `types_of_works`
--

INSERT INTO `types_of_works` (`code_type`, `name`, `description`, `coast_of_work`, `code_material_1`, `code_material_2`, `code_material_3`) VALUES
(1, 'Пилка металла', 'Пилка металла', 30000, 1, 2, 3),
(2, 'Пилка дерева', 'Пилка дерева', 25000, 5, 4, 3),
(3, 'Сварка Металла', 'Сварка Металла', 63000, 5, 2, 1),
(4, 'Пилка Алюминия', 'Пилка Алюминия', 35000, 5, 4, 2),
(5, 'Пилка досок', 'Пилка досок', 45000, 4, 3, 1);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `brigades`
--
ALTER TABLE `brigades`
  ADD PRIMARY KEY (`code_brigades`),
  ADD KEY `code_employee_1` (`code_employee_1`),
  ADD KEY `code_employee_2` (`code_employee_2`),
  ADD KEY `code_employee_3` (`code_employee_3`);

--
-- Индексы таблицы `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`code_customer`);

--
-- Индексы таблицы `materials`
--
ALTER TABLE `materials`
  ADD PRIMARY KEY (`code_material`);

--
-- Индексы таблицы `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`code_customer`),
  ADD KEY `orders_ibfk_1` (`code_type`),
  ADD KEY `code_brigades` (`code_brigades`),
  ADD KEY `code_staff` (`code_staff`);

--
-- Индексы таблицы `positions`
--
ALTER TABLE `positions`
  ADD PRIMARY KEY (`code_position`);

--
-- Индексы таблицы `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`code_staff`),
  ADD KEY `code_position` (`code_position`);

--
-- Индексы таблицы `types_of_works`
--
ALTER TABLE `types_of_works`
  ADD PRIMARY KEY (`code_type`),
  ADD KEY `code_material_1` (`code_material_1`),
  ADD KEY `code_material_2` (`code_material_2`),
  ADD KEY `code_material_3` (`code_material_3`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `brigades`
--
ALTER TABLE `brigades`
  MODIFY `code_brigades` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `materials`
--
ALTER TABLE `materials`
  MODIFY `code_material` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `positions`
--
ALTER TABLE `positions`
  MODIFY `code_position` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `staff`
--
ALTER TABLE `staff`
  MODIFY `code_staff` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT для таблицы `types_of_works`
--
ALTER TABLE `types_of_works`
  MODIFY `code_type` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `brigades`
--
ALTER TABLE `brigades`
  ADD CONSTRAINT `brigades_ibfk_1` FOREIGN KEY (`code_employee_1`) REFERENCES `staff` (`code_staff`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `brigades_ibfk_2` FOREIGN KEY (`code_employee_2`) REFERENCES `staff` (`code_staff`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `brigades_ibfk_3` FOREIGN KEY (`code_employee_3`) REFERENCES `staff` (`code_staff`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`code_type`) REFERENCES `types_of_works` (`code_type`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`code_brigades`) REFERENCES `brigades` (`code_brigades`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`code_staff`) REFERENCES `staff` (`code_staff`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orders_ibfk_4` FOREIGN KEY (`code_customer`) REFERENCES `customers` (`code_customer`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `staff`
--
ALTER TABLE `staff`
  ADD CONSTRAINT `staff_ibfk_1` FOREIGN KEY (`code_position`) REFERENCES `positions` (`code_position`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `types_of_works`
--
ALTER TABLE `types_of_works`
  ADD CONSTRAINT `types_of_works_ibfk_1` FOREIGN KEY (`code_material_1`) REFERENCES `materials` (`code_material`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `types_of_works_ibfk_2` FOREIGN KEY (`code_material_2`) REFERENCES `materials` (`code_material`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `types_of_works_ibfk_3` FOREIGN KEY (`code_material_3`) REFERENCES `materials` (`code_material`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
