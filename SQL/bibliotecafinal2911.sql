-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: biblioteca
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `documento`
--

DROP TABLE IF EXISTS `documento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `documento` (
  `cod_doc` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(50) NOT NULL,
  `subtitulo` varchar(50) DEFAULT NULL,
  `autor` varchar(50) DEFAULT NULL,
  `editora` varchar(50) DEFAULT NULL,
  `volume` int DEFAULT NULL,
  `ano` int DEFAULT NULL,
  `num_paginas` int DEFAULT NULL,
  `local_publicacao` varchar(30) DEFAULT NULL,
  `edicao` int DEFAULT NULL,
  `tipo_documento` varchar(255) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`cod_doc`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documento`
--

LOCK TABLES `documento` WRITE;
/*!40000 ALTER TABLE `documento` DISABLE KEYS */;
INSERT INTO `documento` VALUES (1,'Harry Potter','e a Pedra Filosofal','JK Rowling','Rocco',123,2017,208,'None',1,'None','estoque'),(2,'Harry Potter','e o Cálice de Fogo','JK Rowling','Rocco',NULL,2017,480,NULL,1,NULL,'estoque'),(3,'Uma breve história do tempo','','Stephen Hawking','Intrínseca',NULL,2015,256,NULL,1,NULL,'estoque'),(4,'O diário de Anne Frank','','Anne Frank','Principis',NULL,2020,224,NULL,6,NULL,'emprestado'),(5,'Orgulho e Preconceito','','Jane Austen','Principis',NULL,2020,288,NULL,3,NULL,'estoque'),(6,'matheus','teteu','teteu','aquela',1,2006,546,'teste',1,'teste','emprestado'),(7,'matheus','teteu','teteu','aquela',1,2006,546,'teste',1,'teste','emprestado'),(8,'matheus','teteu','teteu','aquela',1,2006,546,'teste',1,'teste','emprestado'),(9,'matheus','teteu','teteu','aquela',1,2006,546,'teste',1,'teste','emprestado'),(10,'matheus','teteu','teteu','aquela',1,2006,546,'teste',1,'teste','emprestado'),(11,'matheus','teteu','teteu','aquela',1,2006,546,'teste',1,'teste','emprestado'),(12,'matheus','teteu','teteu','aquela',1,2006,546,'teste',1,'teste','emprestado'),(13,'teste','teste','teste','teste',234,234,234,'teste',3,'teste2','estoque'),(14,'teste543','rge','dfg','gdf',6,65,5,'fgh',6,'sfad','estoque'),(15,'t','t','t','t',1,2,2,'ts',1,'ts','estoque');
/*!40000 ALTER TABLE `documento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emprestimo`
--

DROP TABLE IF EXISTS `emprestimo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emprestimo` (
  `cod_emprestimo` int NOT NULL AUTO_INCREMENT,
  `cpf_socio` varchar(11) DEFAULT NULL,
  `cod_func` int DEFAULT NULL,
  `data_emprestimo` date DEFAULT NULL,
  `data_dev_max` date DEFAULT NULL,
  `data_devolucao` date DEFAULT NULL,
  `obs` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cod_emprestimo`),
  KEY `cpf_socio` (`cpf_socio`),
  KEY `cod_func` (`cod_func`),
  CONSTRAINT `emprestimo_ibfk_1` FOREIGN KEY (`cpf_socio`) REFERENCES `socio` (`cpf`),
  CONSTRAINT `emprestimo_ibfk_2` FOREIGN KEY (`cod_func`) REFERENCES `funcionario` (`cod_func`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emprestimo`
--

LOCK TABLES `emprestimo` WRITE;
/*!40000 ALTER TABLE `emprestimo` DISABLE KEYS */;
INSERT INTO `emprestimo` VALUES (1,'11122233310',10,'2021-10-12','2021-10-22','2021-10-23','teste'),(5,'22211133310',10,'2021-10-04','2021-10-30','2021-10-30',NULL),(6,'33311133312',12,'2021-10-30','2021-11-06','2021-11-01',NULL),(7,'55511133330',12,'2021-11-02',NULL,'2000-01-01','teste'),(8,'10654425990',1,'2000-01-01','2000-01-01','2000-01-01','teste'),(9,'10654425990',1,'2000-01-01','2021-11-28','2021-11-29','teste'),(10,'10654425990',1,'2000-01-01','2021-11-28','2021-11-29','teste'),(11,'10654425990',1,'2000-01-01','2021-11-28','2021-11-29','teste'),(12,'10654425990',1,'2000-01-01','2021-11-28','2021-11-29','teste'),(13,'10654425990',1,'2000-01-01','2021-11-28','2021-11-29','sem'),(14,'10654425990',1,'2000-01-01','2000-01-01',NULL,NULL),(15,'10654425990',1,'2000-01-01','2000-01-01',NULL,NULL),(16,'10654425990',1,'2000-01-01','2000-01-01',NULL,NULL),(17,'10654425990',1,'2000-01-01','2000-01-01',NULL,NULL),(18,'10654425990',1,'2000-01-01','2000-01-01',NULL,NULL);
/*!40000 ALTER TABLE `emprestimo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `endereco`
--

DROP TABLE IF EXISTS `endereco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `endereco` (
  `cep` int NOT NULL,
  `logradouro` varchar(30) DEFAULT NULL,
  `bairro` varchar(30) DEFAULT NULL,
  `cidade` varchar(30) DEFAULT NULL,
  `UF` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`cep`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `endereco`
--

LOCK TABLES `endereco` WRITE;
/*!40000 ALTER TABLE `endereco` DISABLE KEYS */;
INSERT INTO `endereco` VALUES (11250000,'as','teste2','as','gh'),(21250000,'dsa','asd','dsa','ds'),(61250000,'l,ppook','opp','l,popo','pp'),(80020180,'Rua Barão do Serro Azul','Centro','Curitiba','PR'),(80730210,'Rua Abrão Lerner','Campina do Siqueira','Curitiba','PR'),(81250000,'jb','cc','cwb','tt'),(81250001,'teste','teste','teste','tt'),(81250002,'teste','teste','teste','as'),(81250003,'teste','teste','teste','as'),(81250007,'teste','teste','teste','pr'),(81350000,'teste','teste','teste','tq'),(81540200,'Rua Barão de Monte Alegre','Jardim das Américas','Curitiba','PR'),(81925090,'sitio loko','rua giacolo','curitiba','pr'),(82025110,'Rua Antônio Falcão','Cascatinha','Curitiba','PR'),(82410270,'Rua Adolfo Lutz','Santa Felicidade','Curitiba','PR'),(91250000,'teste','teste','teste','tt'),(456789123,'gdf','fdgh','gjg','jh'),(987456111,'teste','teste','teste','ts');
/*!40000 ALTER TABLE `endereco` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionario`
--

DROP TABLE IF EXISTS `funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionario` (
  `cod_func` int NOT NULL AUTO_INCREMENT,
  `cpf` varchar(11) NOT NULL,
  `nomecompleto` varchar(50) NOT NULL,
  `cargo` varchar(20) DEFAULT NULL,
  `cep` int NOT NULL,
  `complemento` varchar(255) DEFAULT NULL,
  `numero_casa` int DEFAULT NULL,
  PRIMARY KEY (`cod_func`),
  KEY `cep` (`cep`),
  CONSTRAINT `funcionario_ibfk_1` FOREIGN KEY (`cep`) REFERENCES `endereco` (`cep`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionario`
--

LOCK TABLES `funcionario` WRITE;
/*!40000 ALTER TABLE `funcionario` DISABLE KEYS */;
INSERT INTO `funcionario` VALUES (1,'10654425990','matheus','admin',81250000,'sem',1600),(3,'999111315','Vânia Silva','Bilbiotecária',80730210,NULL,NULL),(4,'999111315','Vânia Silva','Bilbiotecária',80730210,NULL,NULL),(5,'999111315','Vânia Silva','Bilbiotecária',80730210,NULL,NULL),(7,'999111315','Vânia Silva','Bilbiotecária',80730210,NULL,NULL),(10,'99911133355','Vânia Silva','Bilbiotecária',80730210,NULL,NULL),(12,'88811133355','Carlos Cunha','Bibliotecário',82410270,NULL,NULL),(13,'10654425993','matheus','asda',81250007,'casa 7',NULL),(14,'10654425990','teste','teste',81250000,'teste',NULL),(15,'10654425990','teste','teste',81250000,'teste',NULL),(16,'10654425990','teste','teste',81250000,'teste',NULL),(17,'10654425990','teste','teste',81250000,'teste',NULL),(18,'10654425990','julia','teste',81250000,'casa 7',NULL),(19,'10654425990','julia','teste',81250000,'casa 7',NULL),(20,'10654425990','matheus ','teste',81250000,'casa 541',NULL),(21,'10654425990','matheus ','teste',81250000,'casa 541',NULL),(22,'10654425990','teste','teste',81250000,'teste',NULL),(23,'10654425901','nathalia','teste',11250000,'teste2',NULL),(24,'10654425901','nathalia','teste',11250000,'teste2',NULL),(25,'10653025990','nathalia f','teste',21250000,'casa t',NULL),(26,'10654425913','teteu','teste',987456111,'teste',NULL),(27,'10654425990','testeteste','testeteste',456789123,'gfh',NULL),(28,'12345678912','vinicius','chefe',81925090,'',NULL),(29,'4645645','teste','teste',81250000,'casa 2',NULL);
/*!40000 ALTER TABLE `funcionario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item` (
  `cod_item` int NOT NULL AUTO_INCREMENT,
  `cod_emprestimo` int NOT NULL,
  `cod_doc` int NOT NULL,
  `quantidade` int DEFAULT NULL,
  PRIMARY KEY (`cod_item`),
  KEY `cod_emprestimo` (`cod_emprestimo`),
  KEY `cod_doc` (`cod_doc`),
  CONSTRAINT `item_ibfk_1` FOREIGN KEY (`cod_emprestimo`) REFERENCES `emprestimo` (`cod_emprestimo`),
  CONSTRAINT `item_ibfk_2` FOREIGN KEY (`cod_doc`) REFERENCES `documento` (`cod_doc`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1,1,2,1),(2,5,3,1),(3,6,4,1),(4,7,5,1),(5,11,1,NULL),(6,11,3,NULL),(7,11,3,NULL),(11,15,1,NULL),(12,16,2,NULL),(13,17,3,NULL),(14,18,2,NULL);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socio`
--

DROP TABLE IF EXISTS `socio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `socio` (
  `cpf` varchar(11) NOT NULL,
  `nomecompleto` varchar(50) NOT NULL,
  `rg` varchar(15) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `sexo` varchar(2) DEFAULT NULL,
  `cep` int NOT NULL,
  `numero_casa` int DEFAULT NULL,
  `complemento` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cpf`),
  KEY `cep` (`cep`),
  CONSTRAINT `socio_ibfk_1` FOREIGN KEY (`cep`) REFERENCES `endereco` (`cep`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socio`
--

LOCK TABLES `socio` WRITE;
/*!40000 ALTER TABLE `socio` DISABLE KEYS */;
INSERT INTO `socio` VALUES ('1','teste','6','30265351','sd','m',81250000,1600,'asdgh'),('10654425417','matheus','564546','32065','ferna@','m',81250000,1456,'teste'),('10654425990','matheus f m','30265351','30265351','matheus@','m',81250000,1600,'c7'),('10654425998','matheus','564546','32065','ferna@','m',81250000,1456,'teste'),('1068725990','matheus','3216','30265351','matheus','m',81250000,1600,'sem'),('11122233310','Jessica Batista','1212123','999991111','jessicabatista@email.com','F',80730210,2,NULL),('12654425990','asd','5156','5619','asd','f',81250000,16501,'ytr'),('2','teste','6','30265351','sd','m',81250000,1600,'asd'),('20654325990','asd','841','65165','ferna','f',81250000,456,'teste'),('20654425990','gafdss','511','216','5asd','m',81250000,615,'asda'),('22211133310','Eduardo Henrique','1234567','988881111','eduhenrique@email.com','M',82410270,34,NULL),('33311133312','Bianca Antunes','1432345','988882222','bianca@email.com','F',82025110,902,NULL),('44411122241','Pedro Paiva','2345617','999993333','pedropaiva@email.com','M',80020180,1001,NULL),('45699','teste','1562','561','fas','m',81250000,54,'casa 7'),('4876521','asd','9154','91','asd','f',81250000,1600,'asd 7'),('5','teste','6','30265351','sd','m',81250000,1600,'asd'),('55511133330','Angelica Duarte','3456337','992121111','angelica@email.com','F',81540200,458,NULL),('6','teste','6','30265351','sd','m',81250000,1600,'asd'),('654677990','matheus','3216','30265351','matheus','m',81250000,1600,'sem'),('654876990','matheus','3216','30265351','matheus','m',81250000,1600,'sem'),('6568675990','matheus','3216','30265351','matheus','m',81250000,1600,'sem'),('6568725990','matheus','3216','30265351','matheus','m',81250000,1600,'sem'),('6568876990','matheus','3216','30265351','matheus','m',81250000,1600,'sem'),('676590','matheus','3216','30265351','matheus','m',81250000,1600,'sem'),('67659560','matheus','3216','30265351','matheus','m',81250000,1600,'sem'),('67665560','matheus','3216','30265351','matheus','m',81250000,1600,'sem'),('67965560','matheus','3216','30265351','matheus','m',81250000,1600,'sem');
/*!40000 ALTER TABLE `socio` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-29 23:34:35
