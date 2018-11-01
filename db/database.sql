SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

CREATE TABLE IF NOT EXISTS `mydb`.`gebruiker` (
  `id` VARCHAR(45) NOT NULL,
  `gebruikersnaam` INT NOT NULL,
  `wachtwoord` VARCHAR(64) NOT NULL,
  `telegram_id` VARCHAR(50) NULL,
  `adres` VARCHAR(64) NULL,
  `huisnummer` VARCHAR(5) NULL,
  `toevoeging` VARCHAR(5) NULL,
  `postcode` VARCHAR(7) NULL,
  `stad` VARCHAR(64) NULL,
  `land` VARCHAR(64) NULL,
  UNIQUE INDEX `telegram_id_UNIQUE` (`telegram_id` ASC),
  UNIQUE INDEX `gebruikersnaam_UNIQUE` (`gebruikersnaam` ASC),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`fiets` (
  `fietscode` INT NOT NULL,
  `locatie` VARCHAR(45) NULL,
  `in_stalling` TINYINT(1) NULL,
  `gebruiker_id` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`fietscode`),
  INDEX `fk_fiets_gebruiker_idx` (`gebruiker_id` ASC),
  CONSTRAINT `fk_fiets_gebruiker`
  FOREIGN KEY (`gebruiker_id`)
  REFERENCES `mydb`.`gebruiker` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
