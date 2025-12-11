from django import forms


class AssociadoForm(forms.Form):
    GENERO_CHOICES = (
        ('', 'Escolha um Genero'),
        ('F', 'Mulher'),
        ('M', 'Homem'),
        ('NB', 'Não Binário'),
        ('O', 'Outro'),
        ('PND', 'Prefiro Não Declarar'),
    )

    nome_completo = forms.CharField(
        label="Usuário (tudo junto, sem espaço)",
        required=True,
        max_length=100,
        error_messages={'required': ''},  # Adicionei uma mensagem
    )

    nome_social = forms.CharField(
        label="Nome social (como você prefere ser chamado (a)",
        required=False,
        max_length=100,
        error_messages={'required': ''},  # Adicionei uma mensagem
    )

    # --- CAMPO 3: IDENTIDADE DE GÊNERO ---
    identidade_genero = forms.ChoiceField(
        label='Qual sua identidade de gênero?',
        choices=GENERO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
        error_messages={'required': ''}
    )

    # Campo para a opção 'Outro'
    genero_outro = forms.CharField(
        label='Selecione "Outro" acima e especifique',
        max_length=100,
        required=False,
        help_text='Use apenas se a opção "Outro" tiver sido selecionada.',
        error_messages={'required': ''}
    )

    email = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Digite seu e-mail'
                                       }),
        error_messages={'required': ''}
    )

    senha_1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
        error_messages={'required': ''}
    )

    senha_2 = forms.CharField(
        label='Confirmação de Senha',  # Ajustei o label para melhor clareza
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme sua senha',
            }
        ),
        error_messages={'required': ''}
    )

    # o Django só entende se seguir o padrão
    # clean e o nome do campo que você quer..
    def clean_nome_completo(self):
        nome = self.cleaned_data.get("nome_completo")
        if nome:
            nome = nome.strip()
            # O trecho abaixo estava verificando se a string vazia "" está em 'nome'.
            # Para verificar se há espaços em branco, o correto é verificar ' ' (espaço).
            # Se a intenção é que seja tudo junto, sem espaços, use:
            if ' ' in nome:
                raise forms.ValidationError("não pode ter espaço em branco")
            return nome
        else:
            # Se o campo for obrigatório, esta validação não será acionada se estiver vazio
            # porque o `required=True` já cuidará disso, mas é bom manter a consistência.
            return nome

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_2
class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100
    )

    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput()
    )