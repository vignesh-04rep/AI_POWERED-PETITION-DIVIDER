-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 13, 2025 at 08:23 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `empcomp`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `uname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`uname`, `password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `id` int(10) NOT NULL auto_increment,
  `cname` varchar(100) NOT NULL,
  `loction` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`id`, `cname`, `loction`, `email`, `phone`, `uname`, `password`) VALUES
(1, 'visacard', 'trichy', 'sundarv06@gmail.com', '7904461600', 'admin', '1234'),
(2, 'tcs', 'trichy', 'sundarv06@gmail.com', '9840234119', 'tcs', 'tcs');

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE `complaint` (
  `id` int(50) NOT NULL auto_increment,
  `uname` varchar(50) NOT NULL,
  `dept` varchar(50) NOT NULL,
  `ctype` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `details` varchar(50) NOT NULL,
  `image` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `urate` varchar(100) NOT NULL,
  `feed` varchar(100) NOT NULL,
  `oname` varchar(100) NOT NULL,
  `b1` varchar(1000) NOT NULL,
  `b2` varchar(1000) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`id`, `uname`, `dept`, `ctype`, `location`, `date`, `details`, `image`, `status`, `urate`, `feed`, `oname`, `b1`, `b2`) VALUES
(1, 'pandiyan', 'Public Transportation', 'normal', 'trichy', '2025-03-19', 'The water supply in our neighborhood is irregular ', 'Screenshot (2).png', 'complaint sent to officer', '', 'Medium Urgency', '', '', ''),
(2, 'sam', 'Energy', 'normal complaint', 'trichy', '2025-03-19', 'Our hospital is understaffed, and patients have to', 'Screenshot (7).png', 'complaint sent to officer', '', 'Medium Urgency', '', '', ''),
(3, 'sample', 'Public Safety', 'normal', 'trichy', '2025-04-13', 'test', 'banner33.jpg', 'complaint sent to officer', '', 'Medium Urgency', '', '', ''),
(4, 'sample', 'Infrastructure', 'normal', 'trichy', '2025-04-17', 'The classroom chairs are uncomfortable and need re', 'Screenshot (7).png', 'complaint sent to officer', '', 'High Urgency', '', '', ''),
(5, 'sample', 'Infrastructure', 'normal', 'trichy', '2025-04-18', 'The hostel staff are not friendly and lack basic h', 'Screenshot (10).png', 'complaint sent to officer', '', 'Medium Urgency', '', '', ''),
(6, 'sample', 'Staff', 'normal', 'trichy', '2025-04-17', 'The hostel staff are not friendly and lack basic h', 'aadhar card.png', 'complaint sent to officer', '', 'Medium Urgency', '', '', ''),
(7, 'sa', 'Infrastructure', 'normal', 'trichy', '2025-04-19', 'Hostel rooms are too small for two people.', 'banner33.jpg', 'complaint sent to officer', '', 'High Urgency', '', '', ''),
(8, 'sundar', 'Food', 'normal', 'trichy', '2025-05-07', 'The food in the canteen is too cold and tasteless.', 'Black_10.jpg', 'complaint sent to officer', '', 'Low Urgency', 'sam', '', ''),
(9, 'sundar', 'Food', 'crime', 'trichy', '2025-05-07', 'The food in the canteen is too cold and tasteless.', 'Black_18.jpg', 'complaint sent to officer', '', 'Low Urgency', 'sam', '', '82bc6500e89ddf04772a98b9a9063f67a1c4566e'),
(10, 'sundar', 'Food', 'crime', 'trichy', '2025-05-07', 'The food in the canteen is too cold and tasteless.', 'Black_18.jpg', 'complaint sent to officer', '', 'Low Urgency', 'sam', '82bc6500e89ddf04772a98b9a9063f67a1c4566e', '82bc6500e89ddf04772a98b9a9063f67a1c4566e'),
(11, 'sam123', 'Environment', 'normal', 'trichy', '2025-05-14', 'The water supply in the office building is inconsi', 'ep2d_diff_3scan_trace_p2_ADC_DFC_010.png', 'test', '', 'Low Urgency', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(50) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `qual` varchar(50) NOT NULL,
  `dept` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`id`, `name`, `gender`, `email`, `phone`, `qual`, `dept`, `address`, `place`, `uname`, `password`) VALUES
(1, 'sundar', 'male', 'sundarv06@gmail.com', '9840234119', 'be', 'Public Safety', 'trichy', 'trichy', 'sundar', 'sundar'),
(2, 'sundar', 'male', 'sundarv06@gmail.com', '9840234119', 'test', 'staff', 'trichy', 'trichy', 'staff', 'staff'),
(3, '', 'male', '', '', '', 'teset', '', '', '', ''),
(4, 'sam', 'male', 'sundarv06@gmail.com', '7904461600', 'be', 'Food', 'trichy', 'trichy', 'sam', 'sam');

-- --------------------------------------------------------

--
-- Table structure for table `job`
--

CREATE TABLE `job` (
  `id` int(50) NOT NULL auto_increment,
  `jname` varchar(100) NOT NULL,
  `cname` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `jtime` varchar(100) NOT NULL,
  `salary` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `skills` varchar(1000) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `job`
--

INSERT INTO `job` (`id`, `jname`, `cname`, `place`, `jtime`, `salary`, `details`, `skills`) VALUES
(1, 'Smart home services', 'visacard', 'trichy', '134', '1000', 'test', 'C++'),
(2, 'developer', 'tcs', 'trichy', 'full time', '10000', 'sample', 'python');

-- --------------------------------------------------------

--
-- Table structure for table `jobtemp`
--

CREATE TABLE `jobtemp` (
  `id` int(50) NOT NULL auto_increment,
  `jname` varchar(100) NOT NULL,
  `cname` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `jtime` varchar(100) NOT NULL,
  `salary` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `skills` varchar(1000) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `jobtemp`
--

INSERT INTO `jobtemp` (`id`, `jname`, `cname`, `place`, `jtime`, `salary`, `details`, `skills`) VALUES
(1, 'Smart home services', 'visacard', 'trichy', '134', '1000', 'test', 'C++'),
(2, 'Smart home services', 'visacard', 'trichy', '134', '1000', 'test', 'C++');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(50) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `name`, `gender`, `email`, `phone`, `address`, `place`, `uname`, `password`) VALUES
(1, 'pandiyan', 'male', 'sundarv06@gmail.com', '9840234119', 'trichy', 'trichy', 'pandiyan', 'pandiyan'),
(2, 'sam', 'male', 'sundarv06@gmail.com', '9840234119', 'TRICHY', 'trichy', 'sam', 'sam'),
(3, 'sample', 'male', 'sundarv06@gmail.com', '9840234119', 'trichy', 'trichy', 'sample', 'sample'),
(4, '', 'male', '', '', '', '', '', ''),
(5, 'sample', 'male', 'sundarv06@gmail.com', '7904461600', 'trichy', 'trichy', 'sample', 'sample'),
(6, 'sa', 'male', 'sundarv06@gmail.com', '7904461600', 'trichy', 'trichy', 'sa', 'sa'),
(7, 'sundar', 'male', 'sundarv06@gmail.com', '7904461600', 'trichy', 'trichy', 'sundar', 'sundar'),
(8, 'sam', 'male', 'sundarv06@gmail.com', '7904461600', 'trichy', 'trichy', 'sam123', 'sam123');

-- --------------------------------------------------------

--
-- Table structure for table `userfile`
--

CREATE TABLE `userfile` (
  `id` int(10) NOT NULL auto_increment,
  `uname` varchar(10) NOT NULL,
  `date` varchar(10) NOT NULL,
  `details` varchar(100) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `pkey` varchar(100) NOT NULL,
  `b1` varchar(500) NOT NULL,
  `b2` varchar(500) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=14 ;

--
-- Dumping data for table `userfile`
--

INSERT INTO `userfile` (`id`, `uname`, `date`, `details`, `fname`, `pkey`, `b1`, `b2`) VALUES
(1, 'sam', '2023-02-18', 'test', '13.jpg', '', '0', '3d3ba62367e9508fa0f187cfba969822afc7e4bf'),
(2, 'sam', '2023-02-23', 'test', '23.jpg', '', '3d3ba62367e9508fa0f187cfba969822afc7e4bf', 'b4e7fc4b1bd5b6a010ef6eaafffb1f0f15e31177'),
(3, 'sam', '2023-02-18', 'test', 'app.py', '', 'b4e7fc4b1bd5b6a010ef6eaafffb1f0f15e31177', '0eef25737ac690fa2dadfabe41109bc2920622ef'),
(4, 'sam', '2023-03-09', 'test', 'car1.png', '', '0eef25737ac690fa2dadfabe41109bc2920622ef', '25c529162090569d53f5312518eabdfb5d191cd7'),
(5, 'sam', '2023-03-11', 'test', 'coaches4.jpg', '', '25c529162090569d53f5312518eabdfb5d191cd7', '90450a1cb0aafbae814bf64c3855fe3259f07955'),
(6, 'admin', '2023-03-14', 'sample', '2.png', '', '90450a1cb0aafbae814bf64c3855fe3259f07955', 'e944d4310300f3c8c986f7ca6d2b8cb92795af2e'),
(7, 'admin34', '2023-03-24', 'test', 'sampletest.py', '', 'e944d4310300f3c8c986f7ca6d2b8cb92795af2e', 'd14bb763ca13745d778701d596981652d25e2d92'),
(8, 'admin32', '2023-03-30', 'sample', 'contact.html', '', 'd14bb763ca13745d778701d596981652d25e2d92', 'b788639ed9dd5830b831a519a3c524ba682926fb'),
(9, 'sss', '2024-02-21', 'test', 'best_model_101class.hdf5', '', 'b788639ed9dd5830b831a519a3c524ba682926fb', 'c5c11a137d54b12cefe8ff40d7483c03a1c96c5f'),
(10, 'aa', '2024-04-25', 'Sample', '1.docx', '', 'c5c11a137d54b12cefe8ff40d7483c03a1c96c5f', '3ce78facdd5e734b922312ad459b18c81a68992e'),
(11, 'aa', '2024-04-26', 'test', 'Screenshot (1).png', '', '3ce78facdd5e734b922312ad459b18c81a68992e', 'd896476f4aa8800d47f5f594aeb1585d6338a7b5'),
(12, 'admin', '2025-03-12', 'ikugjkhgo', 'Alluvial-soil-distribution-in-India.jpg', '', 'd896476f4aa8800d47f5f594aeb1585d6338a7b5', 'e2a95842071cc3517137f4be3d941204de94cafe'),
(13, 'sam', '2025-03-17', 'test', '1socialnetpy.sql', '', 'e2a95842071cc3517137f4be3d941204de94cafe', '4e442abf28b34e0d782ab49bb38e0d6714459e0b');

-- --------------------------------------------------------

--
-- Table structure for table `userfile1`
--

CREATE TABLE `userfile1` (
  `id` int(10) NOT NULL auto_increment,
  `uname` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `rname` varchar(100) NOT NULL,
  `Qualification` varchar(500) NOT NULL,
  `skills` varchar(500) NOT NULL,
  `maiid` varchar(100) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `file` varchar(500) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `userfile1`
--


-- --------------------------------------------------------

--
-- Table structure for table `userstatus`
--

CREATE TABLE `userstatus` (
  `name` varchar(10) NOT NULL,
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userstatus`
--

INSERT INTO `userstatus` (`name`, `status`) VALUES
('admin12', 'extraverte'),
('admin', 'dependable'),
('s1234', 'dependable'),
('admin12', 'extraverte'),
('admin', 'extraverte'),
('333', 'serious'),
('admin', 'dependable'),
('admin', 'extraverte'),
('admin', 'extraverte'),
('admin', 'dependable'),
('admin', 'extraverte'),
('admin', 'dependable');

-- --------------------------------------------------------

--
-- Table structure for table `userstatus1`
--

CREATE TABLE `userstatus1` (
  `uname` varchar(50) NOT NULL,
  `skills` varchar(1000) NOT NULL,
  `name` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userstatus1`
--

INSERT INTO `userstatus1` (`uname`, `skills`, `name`, `gender`, `email`, `phone`, `address`, `place`) VALUES
('admin', 'Fitness Marketing International Finance', '', '', '', '', '', ''),
('admin', 'Php Python Training Email Mobile Electrical Programming C++ Automation Java Javascript Rocket Html Github Research System Css C Technical', '', '', '', '', '', ''),
('admin', 'C++ Css Mobile Programming Technical Email System Html Php Github Research Rocket Automation C Java Electrical Javascript Training Python', 'sample', 'male', 'sundarv06@gmail.com', '9840234119', 'trichy', 'trichy'),
('admin', 'Java Research Php Technical Html Rocket System C++ C Mobile Electrical Python Automation Training Programming Javascript Css Github Email', 'sample', 'male', 'sundarv06@gmail.com', '9840234119', 'trichy', 'trichy'),
('admin', '', 'sample', 'male', 'sundarv06@gmail.com', '9840234119', 'trichy', 'trichy');
