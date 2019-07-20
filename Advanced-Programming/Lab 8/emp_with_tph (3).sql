-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 16, 2017 at 11:31 AM
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
-- Table structure for table `con_emp_unionsubclass`
--

CREATE TABLE `con_emp_unionsubclass` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `contract_period` varchar(255) DEFAULT NULL,
  `pay_per_hour` float NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `con_emp_unionsubclass`
--

INSERT INTO `con_emp_unionsubclass` (`id`, `name`, `contract_period`, `pay_per_hour`) VALUES
(2, NULL, '1 year', 0.3),
(3, NULL, '1 year', 0.2),
(4, NULL, '2 years', 0.6);

-- --------------------------------------------------------

--
-- Table structure for table `emp_unionsubclass`
--

CREATE TABLE `emp_unionsubclass` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `emp_unionsubclass`
--

INSERT INTO `emp_unionsubclass` (`id`, `name`) VALUES
(5, 'name'),
(6, 'name'),
(7, 'name'),
(8, 'name');

-- --------------------------------------------------------

--
-- Table structure for table `hibernate_sequences`
--

CREATE TABLE `hibernate_sequences` (
  `sequence_name` varchar(255) NOT NULL,
  `next_val` bigint(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hibernate_sequences`
--

INSERT INTO `hibernate_sequences` (`sequence_name`, `next_val`) VALUES
('default', 9);

-- --------------------------------------------------------

--
-- Table structure for table `reg_emp_unionsubclass`
--

CREATE TABLE `reg_emp_unionsubclass` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `bonus` int(11) NOT NULL,
  `salary` float NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reg_emp_unionsubclass`
--

INSERT INTO `reg_emp_unionsubclass` (`id`, `name`, `bonus`, `salary`) VALUES
(1, NULL, 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `con_emp_unionsubclass`
--
ALTER TABLE `con_emp_unionsubclass`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `emp_unionsubclass`
--
ALTER TABLE `emp_unionsubclass`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hibernate_sequences`
--
ALTER TABLE `hibernate_sequences`
  ADD PRIMARY KEY (`sequence_name`);

--
-- Indexes for table `reg_emp_unionsubclass`
--
ALTER TABLE `reg_emp_unionsubclass`
  ADD PRIMARY KEY (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
