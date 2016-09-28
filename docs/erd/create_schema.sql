-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema rent_kitten
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema rent_kitten
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `rent_kitten` DEFAULT CHARACTER SET utf8 ;
USE `rent_kitten` ;

-- -----------------------------------------------------
-- Table `rent_kitten`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rent_kitten`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(45) NOT NULL,
  `lastname` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(256) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rent_kitten`.`pricing`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rent_kitten`.`pricing` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `types` VARCHAR(45) NOT NULL,
  `price` INT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rent_kitten`.`cat`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rent_kitten`.`cat` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `breed` VARCHAR(45) NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `user_id` INT NOT NULL,
  `pricing_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cat_user1_idx` (`user_id` ASC),
  INDEX `fk_cat_pricing1_idx` (`pricing_id` ASC),
  CONSTRAINT `fk_cat_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `rent_kitten`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cat_pricing1`
    FOREIGN KEY (`pricing_id`)
    REFERENCES `rent_kitten`.`pricing` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rent_kitten`.`invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rent_kitten`.`invoice` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `price` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_invoice_user1_idx` (`user_id` ASC),
  CONSTRAINT `fk_invoice_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `rent_kitten`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rent_kitten`.`address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rent_kitten`.`address` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `street` VARCHAR(256) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `zip` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_address_user1_idx` (`user_id` ASC),
  CONSTRAINT `fk_address_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `rent_kitten`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
