-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 04, 2024 at 06:14 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `empoyee`
--

-- --------------------------------------------------------

--
-- Table structure for table `emp`
--

CREATE TABLE `emp` (
  `e_id` int(11) NOT NULL,
  `Designation` text NOT NULL,
  `Name` text NOT NULL,
  `doj` int(11) NOT NULL,
  `Experience` text NOT NULL,
  `Age` int(11) NOT NULL,
  `Proof` int(11) NOT NULL,
  `gender` text NOT NULL,
  `Email` text NOT NULL,
  `Contact` text NOT NULL,
  `Address` text NOT NULL,
  `Base_Pay` int(11) NOT NULL,
  `Base_Days` int(11) NOT NULL,
  `Medical` int(11) NOT NULL,
  `Convinence` int(11) NOT NULL,
  `P_F` int(11) NOT NULL,
  `Net_Salary` int(11) NOT NULL,
  `reciept` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `emp`
--

INSERT INTO `emp` (`e_id`, `Designation`, `Name`, `doj`, `Experience`, `Age`, `Proof`, `gender`, `Email`, `Contact`, `Address`, `Base_Pay`, `Base_Days`, `Medical`, `Convinence`, `P_F`, `Net_Salary`, `reciept`) VALUES
(12, 'snkw', 'snkw', 23, 'ndw', 23, 322, 'm', 'dsn@kkje.dej', '23232', 'kjfdsnfsd', 232, 34, 34, 343, 334, 7931, 'reciept'),
(45, '', '', 0, '', 0, 0, '', '', '', '', 3, 34, 3, 45, 34, 116, 'reciept'),
(122, 'software development', 'Snowil Tuscano', 12, '4', 19, 1233, '776888307', 'snowil@gmail,cin', '23223', 'swaapna purti khalr stop vatar', 120, 120, 3444, 200, 230, 17814, 'reciept'),
(154, 'CEO', 'snowil', 12, '2', 21, 1234, 'Male', 'snowil@fmail.di', '34435', 'virar', 220, 50, 500, 100, 250, 11350, 'reciept');

-- --------------------------------------------------------

--
-- Table structure for table `emp_salary`
--

CREATE TABLE `emp_salary` (
  `e_id` int(50) NOT NULL,
  `Designation` text NOT NULL,
  `Name` text NOT NULL,
  `doj` text NOT NULL,
  `Experience` int(50) NOT NULL,
  `Age` int(11) NOT NULL,
  `Proof` int(100) NOT NULL,
  `Gender` text NOT NULL,
  `Email` text NOT NULL,
  `Contact` int(50) NOT NULL,
  `Address` text NOT NULL,
  `Base_Pay` int(50) NOT NULL,
  `Base_Days` int(50) NOT NULL,
  `Medical` int(50) NOT NULL,
  `Convinence` int(50) NOT NULL,
  `P_F` int(50) NOT NULL,
  `Net_Salary` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `emp_salary`
--

INSERT INTO `emp_salary` (`e_id`, `Designation`, `Name`, `doj`, `Experience`, `Age`, `Proof`, `Gender`, `Email`, `Contact`, `Address`, `Base_Pay`, `Base_Days`, `Medical`, `Convinence`, `P_F`, `Net_Salary`) VALUES
(12, 'manager', '', '', 0, 0, 0, '', '', 0, '', 0, 0, 0, 0, 0, 0);


--
-- Indexes for table `emp`
--
ALTER TABLE `emp`
  ADD PRIMARY KEY (`e_id`),
  ADD KEY `Designation` (`Designation`(768));

--
-- Indexes for table `emp_salary`
--
ALTER TABLE `emp_salary`
  ADD PRIMARY KEY (`e_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `emp`
--
ALTER TABLE `emp`
  MODIFY `e_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3444;

--
-- AUTO_INCREMENT for table `emp_salary`
--
ALTER TABLE `emp_salary`
  MODIFY `e_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
