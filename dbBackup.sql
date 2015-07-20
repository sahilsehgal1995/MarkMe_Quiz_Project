-- MySQL dump 10.13  Distrib 5.5.43, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: users
-- ------------------------------------------------------
-- Server version	5.5.43-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `questions` (
  `qno` varchar(200) NOT NULL,
  `question` varchar(3250) DEFAULT NULL,
  `option1` varchar(3250) DEFAULT NULL,
  `option2` varchar(3250) DEFAULT NULL,
  `option3` varchar(3250) DEFAULT NULL,
  `option4` varchar(3250) DEFAULT NULL,
  `correct_answer` varchar(3250) DEFAULT NULL,
  PRIMARY KEY (`qno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES ('1','The set of physical addresses is called','Disk Space','Address Space','Pages','Frames','Address Space'),('10','The simplest way to determine cache locations in which to store memory blocks is the,','Associative Mapping technique','Direct Mapping technique','Set-Associative Mapping technique','Indirect Mapping technique','Direct Mapping technique'),('11','Which one of the following CPU registers holds the address of the instructions (instructions in the program stored in memory) to be executed next?','MAR (Memory address register)','PC (Program Counter).','MBR (Memory Buffer Register)','AC (Accumulator)','PC (Program Counter).'),('2','The number of 256*4 RAM chips required to construct 2KB CACHE is','8','4','32','16','16'),('3','What is the name of device that is allowed to initiate data transfer on the bus?','Bus Master','Bus Arbitration','Bus Cycle','Bus Request','Bus Master'),('4','The DMA transfer technique where transfer of one word data at a time is called','Cycle stealing','Memory stealing','Hand-shaking','Inter-leaving','Cycle stealing'),('5','What are the building blocks of combinational circuits?','Flip-flops','Logic gates','Latches','Registers','Logic gates'),('6','The correspondence between the main memory blocks and those in the cache is specified by a','Miss penalty','Replacement algorithms','Hit rate','Mapping functions.','Mapping functions.'),('7','What is the word size of a 8086 processor?','8 bits','16 bits','32 bits','64 bits','16 bits'),('8','Cycle stealing is/are used in which concept?','Programmed I/O','DMA','Interrupts','All of the above.','DMA'),('9','64K memory contains how many words of 8 bits each?','65,536','64,536','65,436','65,546','65,536');
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(32500) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('sahilsehgal1995','$5$rounds=80000$aWCp','sahilsehgal1995@gmail.com','sahil sehgal'),('ue138001','$5$rounds=80000$MVyx9liKpvk0BeR/$kNqjx04l03jTeCpOiv8GkzYhs/yu2NSM7X8VwcKwKz.','myaashish@live.com','Aashish Parmar'),('sahil','$5$rounds=80000$WzZasqqWe3UIvte4$OQ0h7AyZGf.sNXhBxwJTMj9fEhLTo.P1Mk.UHo4mOJ/','sahilsehgal1995@gmail.com','sahil sehgal'),('aashish','$5$rounds=80000$9vgGtHNMDRuUTgAH$tlNiROoLoeM2VhUT60z7cRFWDwBQiy62R3IRS6NufL.','my_aashish@live.com','aashish parmar');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-07-20 23:13:54
