from django.db import models

# estudar o que é ORM (object-relation-mapper)
# herança: uma classe herda de outra e implementa suas próprias características
# Filho(Pai) - utilizo o sinal de (   ) para herança
class Categoria(models.Model): #a classe é um conjunto de objetos
          #toda classe começa com letra Maíscula(PascalCase)
          nome = models.CharField(max_length=80,null=False, blank=False)

          # max_lenght: é o número limite de caracteres
          # null: nenhuma informação
          # blank: string vazia " "
          def __str__(self):
               return f"Categoria [nome={self.nome}]"


# Django ORM

# Python e Flask: SQLAlchemy
# Python e Django : Django ORM
# Java: Hibernate
# C#: Entity Framework
# PHP : Doctrine

# vantagem:
"""
  - Usar a linguagem de fluência
  - Migração (migrar de um banco MySQL para um SQLServer)
  - Menos erros (conexão, segurança entre outros)
  - Toolkit extra interação com banco de dados
"""
# desvantagem
"""
  - Sistemas legados poder ser um problema
  - Iniciantes criar uma  ilusão (não precisa estudar SQL)
"""


