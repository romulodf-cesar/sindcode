CREATE database sindcode_v2;


use sindcode_v2;


CREATE TABLE IF NOT EXISTS associado(
	id_associado INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cpf VARCHAR(20) NOT NULL,
    rg VARCHAR(30),
    nome_completo VARCHAR(100) NOT NULL,
    nome_social VARCHAR(40),
    genero VARCHAR(1),
    data_nascimento DATE NOT NULL   
);

CREATE TABLE IF NOT EXISTS endereco(
	id_endereco INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	cep VARCHAR(15) NOT NULL,
    logradouro VARCHAR(100) NOT NULL,
    complemento VARCHAR(100),
    numero VARCHAR(20),
    cidade VARCHAR(80) NOT NULL,
    bairro VARCHAR(80) NOT NULL,
    estado VARCHAR(80) NOT NULL,
    uf VARCHAR(2) NOT NULL,
	 fk_endereco INT NOT NULL,    
    CONSTRAINT fk_associado_endereco FOREIGN KEY(fk_endereco) REFERENCES associado(id_associado)
);

CREATE TABLE IF NOT EXISTS autor(
	id_autor INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    perfil TEXT	NOT NULL,
    fk_endereco INT NOT NULL,
    CONSTRAINT fk_autor_endereco FOREIGN KEY(fk_endereco) REFERENCES endereco(id_endereco)
);

CREATE TABLE IF NOT EXISTS categoria(
	id_categoria INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL
);

CREATE TABLE IF NOT EXISTS noticia(
	id_noticia INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    conteudo TEXT NOT NULL,
    data_publicacao DATE NOT NULL,
    url_imagem_capa VARCHAR(100),
    destaque ENUM('0','1','2','3','4') NOT NULL DEFAULT '0',
    fk_autor INT NOT NULL,
    fk_categoria INT NOT NULL,
    CONSTRAINT fk_noticia_autor FOREIGN KEY(fk_autor) REFERENCES autor(id_autor),
    CONSTRAINT fk_noticia_categoria FOREIGN KEY(fk_categoria) REFERENCES categoria(id_categoria)
);
CREATE TABLE IF NOT EXISTS telefone(
	id_telefone INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    telefone VARCHAR(20),
    fk_telefone INT NOT NULL,
    CONSTRAINT fk_associado_telefone FOREIGN KEY(fk_telefone) REFERENCES associado(id_associado)
);

CREATE TABLE IF NOT EXISTS email(
	id_email INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    fk_email INT NOT NULL,
    CONSTRAINT fk_associado_email FOREIGN KEY(fk_email) REFERENCES associado(id_associado)
);