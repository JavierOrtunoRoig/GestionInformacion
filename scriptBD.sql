-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema rastreocovid19
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema rastreocovid19
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `rastreocovid19` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `rastreocovid19` ;

-- -----------------------------------------------------
-- Table `rastreocovid19`.`people`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rastreocovid19`.`people` (
  `ID` INT NOT NULL,
  `FIRSTNAME` VARCHAR(50) NULL DEFAULT NULL,
  `LASTNAME` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `rastreocovid19`.`friends`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rastreocovid19`.`friends` (
  `ID1` INT NOT NULL,
  `ID2` INT NOT NULL,
  PRIMARY KEY (`ID1`, `ID2`),
  CONSTRAINT `ID_1`
    FOREIGN KEY (`ID1`)
    REFERENCES `rastreocovid19`.`people` (`ID`),
  CONSTRAINT `ID_2`
    FOREIGN KEY (`ID2`)
    REFERENCES `rastreocovid19`.`people` (`ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `ID_1_idx` ON `rastreocovid19`.`friends` (`ID1` ASC) VISIBLE;

CREATE INDEX `ID_2_idx` ON `rastreocovid19`.`friends` (`ID2` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

INSERT INTO `rastreocovid19`.`people` (`ID`, `FIRSTNAME`,`LASTNAME` ) VALUES ('1', 'Amina Adballah', 'Arraff Al Omari');

INSERT INTO `rastreocovid19`.`people` (`ID`, `FIRSTNAME`,`LASTNAME` ) VALUES ('2', 'William ', 'Ahsbless');

INSERT INTO `rastreocovid19`.`people` (`ID`, `FIRSTNAME`,`LASTNAME` ) VALUES ('3', 'George P.', 'Burdell');

INSERT INTO `rastreocovid19`.`people` (`ID`, `FIRSTNAME`,`LASTNAME` ) VALUES ('4', 'Eddie', 'Burrup');

INSERT INTO `rastreocovid19`.`people` (`ID`, `FIRSTNAME`,`LASTNAME` ) VALUES ('5', 'Johnny', 'Chung');

INSERT INTO `rastreocovid19`.`friends` (`ID1`, `ID2` ) VALUES ('1', '2');

INSERT INTO `rastreocovid19`.`friends` (`ID1`, `ID2` ) VALUES ('3', '1');

INSERT INTO `rastreocovid19`.`friends` (`ID1`, `ID2` ) VALUES ('3', '2');