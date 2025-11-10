CREATE DATABASE IF NOT EXISTS sindcode;
USE sindcode;
show databases;
-- DROP DATABASE sindicode;
/*
  use o drop com muita cautela
*/
CREATE TABLE autor(   
   id INT PRIMARY KEY auto_increment,
   nome VARCHAR(80) NOT NULL,
   perfil TEXT NOT NULL
);
show tables;
CREATE TABLE categoria(
   id INT PRIMARY KEY auto_increment,
   nome VARCHAR(80) NOT NULL
);
CREATE TABLE noticia(
   id INT PRIMARY KEY auto_increment,
   titulo VARCHAR(90) NOT NULL,
   conteudo TEXT NOT NULL,
   data_publicacao DATETIME NOT NULL,
   destaque enum('0','1','2','3','4') NOT NULL DEFAULT '0',
   foto VARCHAR(60) NOT NULL,
   id_autor INT NOT NULL,
   id_categoria INT NOT NULL,   
   -- Restrições de Chave Estrangeira
   CONSTRAINT FK_Noticia_Autor
        FOREIGN KEY (id_autor)
        REFERENCES autor(id),
    CONSTRAINT FK_Noticia_Categoria
        FOREIGN KEY (id_categoria)
        REFERENCES categoria(id)     
);
# mostrar todas as tabelas
show tables;

# vamos simular a inserção de uma noticia?

describe autor;
INSERT INTO autor(nome,perfil)VALUES('Rômulo','professor de Java/Python/IA'); 
INSERT INTO autor(nome,perfil)VALUES('Ana','desenvolvedora Front-end'); 
INSERT INTO autor(nome,perfil)VALUES('Bruno','engenheiro de dados'); 
INSERT INTO autor(nome,perfil)VALUES('Carla','analista de segurança'); 
INSERT INTO autor(nome,perfil)VALUES('Daniel','arquiteto de Cloud AWS');

describe categoria;
INSERT INTO categoria(nome)VALUES('marfia chinesa'); 
INSERT INTO categoria(nome)VALUES('direito da mulher'); 

select * from categoria;
select * from autor;

describe noticia;

-- 1. Descreve a tabela noticia para ver suas colunas e restrições
DESCRIBE noticia;

---

-- 2. Insere uma Notícia com Destaque '0' (Padrão)
-- id_autor = 1 (Rômulo)
-- id_categoria = 1 (marfia chinesa)
INSERT INTO noticia (titulo, conteudo, data_publicacao, destaque, foto, id_autor, id_categoria)
VALUES (
    'Nova Pesquisa Sobre Crime Organizado',
    'Detalhes sobre a recente operação policial contra o crime organizado em nível internacional.',
    '2025-10-20 10:00:00',
    '0', -- Destaque Normal
    'foto_crime_org.jpg',
    1, -- id_autor: Rômulo
    1  -- id_categoria: marfia chinesa
);

---

-- 3. Insere uma Segunda Notícia com Destaque '3'
-- id_autor = 2 (Ana)
-- id_categoria = 2 (direito da mulher)
INSERT INTO noticia (titulo, conteudo, data_publicacao, destaque, foto, id_autor, id_categoria)
VALUES (
    'Avanços na Legislação de Direitos Femininos',
    'Análise das novas emendas e como elas impactam o direito da mulher no ambiente de trabalho.',
    '2025-10-20 14:30:00',
    '3', -- Destaque Alto
    'foto_direitos.jpg',
    2, -- id_autor: Ana
    2  -- id_categoria: direito da mulher
);

---

-- 4. Insere uma Terceira Notícia
-- id_autor = 5 (Daniel)
-- id_categoria = 1 (marfia chinesa)
INSERT INTO noticia (titulo, conteudo, data_publicacao, destaque, foto, id_autor, id_categoria)
VALUES (
    'Tecnologia e Segurança Pública',
    'Como a arquitetura de cloud computing está sendo usada para rastrear atividades ilícitas.',
    NOW(), -- Usa a data e hora atual do sistema
    '1', -- Destaque Moderado
    'foto_cloud_track.png',
    5, -- id_autor: Daniel
    1  -- id_categoria: marfia chinesa
);


show tables;
SELECT * FROM autor;
SELECT * FROM categoria;
SELECT * FROM noticia;

-- 5. Consulta para verificar as notícias inseridas
SELECT
    n.id,
    n.titulo,
    n.data_publicacao,
    n.destaque,
    a.nome AS autor,
    c.nome AS categoria
FROM
    noticia n
INNER JOIN
    autor a ON n.id_autor = a.id
INNER JOIN
    categoria c ON n.id_categoria = c.id;

SELECT * FROM noticia;




