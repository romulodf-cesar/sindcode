from django.db import models

class Categoria(models.Model):
       nome = models.CharField(max_length=80,null=False, blank=False)
       def __str__(self):
           return f"Categoria [nome={self.nome}]"

class Autor(models.Model):
       nome = models.CharField(max_length=80,null=False, blank=False)
       perfil = models.TextField()
       def __str__(self):
            return self.nome+self.perfil

class Noticia(models.Model):
       titulo = models.CharField(max_length=90,null=False,blank=False)
       conteudo = models.TextField(null=False,blank=False)
       # Define a data e hora na criação do objeto, útil para publicações
       data_publicacao = models.DateTimeField(auto_now_add=True)
       destaque = models.CharField(
           max_length=2,
           choices=[
               ('0', '0'),
               ('1', '1'),
               ('2', '2'),
               ('3', '3'),
               ('4', '4'),
               ('5', '5')  # <--- MUST BE ADDED TO CHOICES
           ],
           default='5',  # <--- DEFAULT VALUE SET HERE
           null=False,
           blank=False
       )
       foto = models.CharField(max_length=60,null=True,blank=True)
       autor = models.ForeignKey(
              Autor,
              on_delete=models.CASCADE,  # Se o Autor for deletado, todas as suas notícias também serão.
              related_name='noticias_autor',  # Nome do relacionamento reverso (autor.noticias.all())
              null=False,  # criar campo autor_id

        )
       # relacionamento de 1:N
       categoria = models.ForeignKey(
             Categoria,
             on_delete=models.CASCADE,  # Se a Categoria for deletada, todas as notícias dessa categoria também serão.
             related_name='noticias_categoria',  # Nome do relacionamento reverso (categoria.noticias.all())
             null=False,  # criar campo categoria_id

        )
       def __str__(self):
            return self.titulo

    
# estudar o que é ORM (object-relation-mapper)# herança: uma classe herda de outra e implementa suas próprias características
# Filho(Pai) - utilizo o sinal de (   ) para herança
#a classe é um conjunto de objetos
 #toda classe começa com letra Maíscula(PascalCase)
        # max_lenght: é o número limite de caracteres
          # null: nenhuma informação
          # blank: string vazia " "   

# Django ORM

# Python e Flask: SQLAlchemy
# Python e Django : Django ORM
# Java: Hibernate
# C#: Entity Framework
# PHP : Doctrine



# vantagem:
"""
  # Usar a linguagem de fluência
  # Migração (migrar de um banco MySQL para um SQLServer)
  # Menos erros (conexão, segurança entre outros)
  # Toolkit extra interação com banco de dados
"""
# desvantagem
"""


  Sistemas legados poder ser um problema
  Iniciantes criar uma  ilusão (não precisa estudar SQL)
  O campo 'id' com chave primária (Primary Key) é criado
 automaticamente pelo Django, a menos que você defina um.
     Se quiser ser explícito e refletir INT(11), pode fazer:
     id = models.AutoField(primary_key=True)
     Mas é mais comum e recomendado deixar o padrão.
         # O equivalente ao VARCHAR(80)
        # Recomenda-se adicionar blank=True ou null=True se for opcional
        
           # O equivalente ao TEXT no MySQL
        # O campo TextField é usado para grandes quantidades de texto.
        # Recomenda-se adicionar blank=True ou null=True se for opcional
         #class Meta:
        # Define o nome da tabela no banco de dados,
        # útil se for diferente do padrão 'appname_autor'
        #db_table = 'autor'

        # Define o nome que o objeto terá no admin e em outras partes do Django
        #verbose_name = 'Autor'
        #verbose_name_plural = 'Autores'
       # pass
         # Representação em string do objeto, útil no console e no Django Admin
# CLASSE NOTICIA

 # O campo 'id' (INT(11)) é criado automaticamente como Primary Key pelo Django.
   # O equivalente ao TEXT
       # class Meta:
    #     # Define o nome da tabela no banco de dados se precisar ser diferente de 'appname_noticia'
    #     db_table = 'noticia'
    #     verbose_name = 'Notícia'
    #     verbose_name_plural = 'Notícias'
     # Representação em string do objeto, útil no console e no Django Admin

"""


