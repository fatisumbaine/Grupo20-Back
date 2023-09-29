CREATE DATABASE IF NOT EXISTS teamhub;

USE teamhub;

CREATE TABLE users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(60) NOT NULL,
  name VARCHAR(60) NOT NULL,
  lastname VARCHAR(60) NOT NULL,
  password VARCHAR(220) NOT NULL,
  email VARCHAR(235) NOT NULL,
  profile_image VARCHAR(260) 
  );
  
  CREATE TABLE servers (
  server_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(60) NOT NULL,
  description TEXT,
  incon VARCHAR(235) 
  );
  
  CREATE TABLE channels (
  channel_id INT AUTO_INCREMENT PRIMARY KEY,
  server_id INT NOT NULL,
  name VARCHAR(60) NOT NULL,
  description TEXT,
  contraint fk_channel_server FOREIGN KEY (server_id) REFERENCES servers(server_id) ON DELETE
  );
  
  CREATE TABLE messages (
  mesagge_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  channel_id INT NOT NULL,
  content TEXT NOT NULL,
  creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  );