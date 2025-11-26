## 🚀 MÓDULO: Desenvolvimento de Sistemas (200h)

Este repositório documenta o progresso e o material desenvolvido para a Unidade Curricular (UC) de **Desenvolvimento de Sistemas** do **Curso Técnico em Desenvolvimento de Sistemas** do SENAI-DF.

A UC visa aplicar metodologias ágeis e tecnologias modernas para a criação de um sistema web completo.

### 🛠️ Tecnologias e Ferramentas

| Categoria | Tecnologia | Ícone |
| :--- | :--- | :--- |
| **Linguagem** | Python | <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" height="20"/> |
| **Framework** | Django | <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white" alt="Django" height="20"/> |
| **Banco de Dados** | MySQL (ou equivalente) | <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white" alt="MySQL" height="20"/> |
| **Versionamento** | Git & GitHub | <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git" height="20"/> <img src="https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white" alt="GitHub" height="20"/> |
| **Gestão Ágil** | Scrum & Jira | <img src="https://img.shields.io/badge/Scrum-004A7F?style=flat-square&logo=scrumalliance&logoColor=white" alt="Scrum" height="20"/> <img src="https://img.shields.io/badge/Jira-0052CC?style=flat-square&logo=jira&logoColor=white" alt="Jira" height="20"/> |

---

### 📚 Diário de Bordo da UC

#### **Aula 1: Introdução à Metodologia e Ambientação**

| Tópico | Detalhes |
| :--- | :--- |
| **Foco da UC** | Subfunção 2.1 e Padrão de Desempenho 2.1.1 (Conhecimento 1.0) |
| **Metodologia** | Estudo e aplicação do **SCRUM** como Metodologia de Desenvolvimento de Sistemas. |
| **Projeto-Alvo** | Criação de um site completo para a **SindCode**, incluindo módulos de: <br> - Benefícios <br> - Notícias <br> - Galeria |
| **Fundamentos** | Revisão e discussão sobre Paradigmas de Programação (Estruturado, Orientado a Objetos e Funcional). |
| **Ambientação Django/Python** | Preparação inicial do ambiente de desenvolvimento. |
| **Configurações** | Definição de Idioma (`LANGUAGE_CODE`) e Fuso Horário (`TIME_ZONE`). |
| **Comandos Essenciais** | `django-admin help` <br> `django-admin startproject setup .` |

---

#### **Aula 2: Ferramentas de Gestão e Segurança do Ambiente**

| Tópico | Detalhes |
| :--- | :--- |
| **Ferramentas Ágeis** | Análise e configuração de ferramentas para suporte ao SCRUM: **Jira** (abordando SCRUM completo e Kanban reduzido), **Trello**, **Notion**, **GitHub Project**, **Azure Boards/DevOps**. |
| **Segurança** | Implementação de boas práticas para gerenciamento de credenciais. |
| **Variáveis de Ambiente** | Configuração de variáveis sensíveis utilizando o arquivo `.env`. |
| **SECRET KEY** | Geração e isolamento da `SECRET_KEY` do Django. |
| **Dependências** | Instalação da biblioteca `python-dotenv`. |
| **Código-Chave** | Importação e carregamento da variável de ambiente: <br>```python\nfrom dotenv import load_dotenv\n# pip install python-dotenv\nload_dotenv()\nSECRET_KEY = str(os.getenv("SECRET_KEY"))\n``` |



#### **Aula 3: Boas práticas**

- 3.1: boas práticas  da subfunção 2.1
- 4.4: controle de versão da subfunção 2.1
- Entre no site para gerar gitignore: https://www.toptal.com/developers/gitignore/api/django
- Entre no github e crie novo repositório: https://github.com/romulodf-cesar/sindcode
- Usar commit especificando a tarefa do SCRUM: git commit -m "<<codigo-task>> <<mensagem>> <<#status>>"
- Aprendi a vincular o post-it
- Aprender Django Apps
- O aplicativo do Django é como se fosse um módulo

#### ** Aula 4: DRY (Don't Repeat Yourself) - Não seja repetitivo"

- index - noticias (principal)
- index - associados
- extends
- include
- partials

#### ** Aula 5: Aplicando Estilos"

- Um projeto Django é formado por um ou vários aplicativos
- O Django nasceu para gerenciar conteúdo (indicado para portais e notícias)
- O Django é usando por grandes empresas (Netflix, Spotify, Instagram)
- O Django é seguro , pyhton, simples, prático, rápido
- O Django é integrado (Admin,Segurança,Templates)
- O Django é dívidido em camadas
  - MVT (Model, View, Template)
- Model é o modelo da aplicação
- View é o controlador (requisições [request-response (HTTP)])
- Template é a parte visual do sistema (HTML,CSS,ASSETS, STYLES,JS,BOOTSTRAP)
- https://tailwindcss.com/ pode ser utilizado em uma camada junto com DTL
- DTL (Django Template Language) - {%        %}
- Aprendemos a configurar URLs e executar aplicação com servidor local
- Aprendemos sobre HTML e suas principais TAGS
- Aprendemos um pouco sobre cores e psicologia das cores e identidade visual
- Aprendemos sobre div e sobre o uso de HTML header, main e footer
- Aprendemos um pouco sobre fórmularios HTML
- Aprendemos a gerar um layout com Gemini Canvas
- Referência Layout: https://gemini.google.com/share/907d04b81dd0
- GitHub do projeto: https://github.com/romulodf-cesar/sindcode
-   /* 1. Definição das Cores Customizadas Bootstrap (Azul Escuro e Ciano) */
        :root {
           --bs-primary: #004080; /* Azul Escuro (Principal) */
           --bs-info: #00bcd4;    /* Azul Ciano/Teal (Destaque) */
           --bs-body-bg: #f8f9fa; /* Fundo Levemente Acinzentado */
           --bs-font-sans-serif: 'Inter', sans-serif;
        }


#### ** Módulo 2 -  Django ORM e ADMIN"

##### ** Aula 6 -  Trabalhar com Dados
- Apresentação -ok
- Preparar o ambiente -ok 
- Nomes Dinâmicos -ok
- Banco de Dados - ok
- ORM no Django -ok
- Criar dados - ok 
- Models no Django - ok
- Migrations - ok

##### ** Aula 7 -  Admin
- Acessar o banco - ok
- Passar referência - ok
- CRUD no Admin - ok
- Incluir Categoria - ok
- Makemigrations e migrate - ok

Exercício: considerando que você já sabe incluir uma categoria, considere o modelo MER
do nosso banco de dados e implemente VOCÊ SOZINHO a entidade Autor.

Considerando nosso contexto a tabela Autor deverá nessa versão ter três campos
id, nome, perfil.

##### ** Admin Avançado

- Personalizar admin - pendente (ok) - estudo dirigido.
- Funcionalidade de publicação - 
- (0 - destaque principal, 1,2,3,4 (destaque secundário) 5 geral)
- Incrementar o index (deixar o site bonito)



##### ** Imagens e Filtros

- Caminho para fotos (Galeria de Fotos) - ok
  - Noticia - ok
- Imagem "not found" - ok
- Alterar a imagem no template - ok

#### ** Mecanismo de busca

- Funcionalidade de buscar -ok
- View de buscar - ok
- Autenticação e Autorização (Django Admin) - pendente


#### ** Conclusão 

- Concluir - ok
- Tirando dúvidas - ok
- Provinha prática teorica de POO - ok
- Apresentação do Sistema
- GitHub - pendente
- Linkedin - pendente
- Vercel e Django - pendente


# 📝 Checklist de Avaliação e Progresso do Projeto SindCode

Este checklist acompanha o progresso de aprendizado e implementação do projeto, organizado por aulas e módulos.

---

## 🚀 Aula 1: Introdução à Metodologia e Ambientação

| Tópico | Detalhes | Status |
| :--- | :--- | :--- |
| **Foco da UC** | Compreensão da Subfunção 2.1 e Padrão de Desempenho 2.1.1 (Conhecimento 1.0). | [ ] |
| **Metodologia** | Estudo e aplicação do **SCRUM**. | [ ] |
| **Projeto-Alvo** | Conhecimento dos módulos do site SindCode (Benefícios, Notícias, Galeria). | [ ] |
| **Fundamentos** | Revisão de Paradigmas de Programação (Estruturado, OO, Funcional). | [ ] |
| **Ambientação** | Preparação inicial do ambiente **Django/Python**. | [ ] |
| **Configurações** | Definição de `LANGUAGE_CODE` e `TIME_ZONE`. | [ ] |
| **Comandos** | Execução e entendimento de `django-admin startproject`. | [ ] |

---

## 🔒 Aula 2: Ferramentas de Gestão e Segurança do Ambiente

| Tópico | Detalhes | Status |
| :--- | :--- | :--- |
| **Ferramentas Ágeis** | Análise e configuração de ferramentas (Jira/Kanban, Trello, Notion, etc.). | [ ] |
| **Segurança** | Implementação de boas práticas para gerenciamento de credenciais. | [ ] |
| **Variáveis de Ambiente** | Configuração de variáveis sensíveis utilizando o arquivo `.env`. | [ ] |
| **SECRET_KEY** | Geração e isolamento da `SECRET_KEY` do Django. | [ ] |
| **Dependências** | Instalação da biblioteca `python-dotenv`. | [ ] |
| **Código-Chave** | Importação e carregamento da variável de ambiente no `settings.py`. | [ ] |

---

## 🛠️ Aula 3: Boas Práticas e Controle de Versão

| Tópico | Detalhes | Status |
| :--- | :--- | :--- |
| **Boas Práticas** | Implementação das boas práticas da subfunção 2.1. | [ ] |
| **Controle de Versão** | Geração e configuração do arquivo `.gitignore` (toptal API). | [ ] |
| **GitHub** | Criação do repositório (`romulodf-cesar/sindcode`) e vinculação do projeto. | [ ] |
| **Commits** | Uso de commits especificando a tarefa do SCRUM (`git commit -m "<> <> <<#status>>"`). | [ ] |
| **Django Apps** | Compreensão da função de um **aplicativo (módulo)** no Django. | [ ] |

---

## 🔄 Aula 4: DRY (Don't Repeat Yourself)

| Tópico | Detalhes | Status |
| :--- | :--- | :--- |
| **Princípio DRY** | Entendimento e aplicação do conceito **"Não seja repetitivo"**. | [ ] |
| **Templates** | Uso da tag `{% extends %}` para herança de templates (estrutura principal). | [ ] |
| **Templates** | Uso da tag `{% include %}` para inclusão de componentes (partials). | [ ] |
| **Partials** | Identificação e criação de blocos reutilizáveis (como header, footer, etc.). | [ ] |

---

## 🎨 Aula 5: Aplicando Estilos

| Tópico | Detalhes | Status |
| :--- | :--- | :--- |
| **Arquitetura** | Compreensão do modelo **MVT (Model, View, Template)**. | [ ] |
| **Camada View** | Entendimento do fluxo de requisições `request-response (HTTP)`. | [ ] |
| **Camada Template** | Uso de HTML, CSS, JS, Bootstrap e Tailwind CSS (opcional). | [ ] |
| **DTL** | Aplicação e uso da **Django Template Language** (`{% %}`). | [ ] |
| **URLs** | Configuração das URLs e execução da aplicação com servidor local. | [ ] |
| **Layout** | Geração e implementação do layout base (Referência Layout: [Gemini Canvas](https://gemini.google.com/share/907d04b81dd0)). | [ ] |
| **Estilos Custom** | Definição das Cores Customizadas Bootstrap (variáveis `--bs-primary`, `--bs-info`). | [ ] |

---

## 💾 Módulo 2 - Aula 6: Trabalhar com Dados

| Tópico | Detalhes | Status |
| :--- | :--- | :--- |
| **ORM** | Entendimento de como funciona o **ORM no Django**. | [ ] |
| **Models** | Criação dos **Models** (entidades de dados) no Django. | [ ] |
| **Migrations** | Execução de `makemigrations` e `migrate`. | [ ] |
| **Dados** | Criação e manipulação básica de dados no banco. | [ ] |

---

## 👑 Módulo 2 - Aula 7: Admin

| Tópico | Detalhes | Status |
| :--- | :--- | :--- |
| **Acesso ao Banco** | Acesso e compreensão da interface Admin. | [ ] |
| **CRUD** | Implementação e teste de operações CRUD no Admin. | [ ] |
| **Categorias** | Inclusão da entidade Categoria no Admin. | [ ] |
| **Exercício - Autor** | Implementação da entidade **Autor** (`id`, `nome`, `perfil`) de forma autônoma. | [ ] |

---

## ➕ Tópicos Avançados e Conclusão

| Tópico | Detalhes | Status |
| :--- | :--- | :--- |
| **Admin Avançado** | Personalização da interface Admin e funcionalidade de publicação. | [ ] |
| **Index** | Incremento e melhoria visual do template `index`. | [ ] |
| **Imagens** | Configuração do caminho e exibição de fotos (Galeria/Notícia) e imagem "not found". | [ ] |
| **Mecanismo de Busca** | Implementação da funcionalidade e da View de busca. | [ ] |
| **Segurança** | Estudo e aplicação de Autenticação e Autorização (Django Admin). | [ ] |
| **Conclusão** | Realização da provinha prática/teórica de POO. | [ ] |
| **Próximos Passos** | Planejamento de deploy (Vercel e Django) e atualização de perfis (GitHub, LinkedIn). | [ ] |

