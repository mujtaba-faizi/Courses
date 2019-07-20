-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 16, 2017 at 11:14 AM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `emp_with_tph`
--

-- --------------------------------------------------------

--
-- Table structure for table `emp_unionsubclass`
--

CREATE TABLE `emp_unionsubclass` (
  `DTYPE` varchar(31) NOT NULL,
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `contract_period` varchar(255) DEFAULT NULL,
  `pay_per_hour` float DEFAULT NULL,
  `bonus` int(11) DEFAULT NULL,
  `salary` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `emp_unionsubclass`
--

INSERT INTO `emp_unionsubclass` (`DTYPE`, `id`, `name`, `contract_period`, `pay_per_hour`, `bonus`, `salary`) VALUES
('Regular_Employee', 1, NULL, NULL, NULL, 0, 1),
('Contract_Employee', 2, NULL, '1 year', 0.3, NULL, NULL),
('Contract_Employee', 3, NULL, '1 year', 0.2, NULL, NULL),
('Contract_Employee', 4, NULL, '2 years', 0.6, NULL, NULL),
('Employee', 5, 'name', NULL, NULL, NULL, NULL),
('Employee', 6, 'name', NULL, NULL, NULL, NULL),
('Employee', 7, 'name', NULL, NULL, NULL, NULL),
('Employee', 8, 'name', NULL, NULL, NULL, NULL),
('Regular_Employee', 9, NULL, NULL, NULL, 0, 1),
('Contract_Employee', 10, NULL, '1 year', 0.3, NULL, NULL),
('Contract_Employee', 11, NULL, '1 year', 0.2, NULL, NULL),
('Contract_Employee', 12, NULL, '2 years', 0.6, NULL, NULL),
('Employee', 13, 'name', NULL, NULL, NULL, NULL),
('Employee', 14, 'name', NULL, NULL, NULL, NULL),
('Employee', 15, 'name', NULL, NULL, NULL, NULL),
('Employee', 16, 'name', NULL, NULL, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `emp_unionsubclass`
--
ALTER TABLE `emp_unionsubclass`
  ADD PRIMARY KEY (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
