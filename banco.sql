
CREATE DATABASE IF NOT EXISTS `teste`
USE `teste`;

CREATE TABLE IF NOT EXISTS `pessoa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `descricao` text,
  PRIMARY KEY (`id`)
);

INSERT INTO `pessoa` (`nome`, `descricao`) VALUES
	('renan', 'teste'),
	('joao', 'aaaa'),
	('maria', 'sla');