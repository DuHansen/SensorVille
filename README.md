# DEPENDÊNCIAS

Instale o Django:
```sh
pip install django
gspread: Facilita o trabalho com o Google Sheets.

oauth2client: Gerencia a autenticação para APIs do Google.

sh
pip install gspread oauth2client
Pillow: Para lidar com arquivos de imagem.

sh
pip install pillow
Python-Decouple: Para gerenciar variáveis de ambiente, como as credenciais.

sh
pip install python-decouple
ARQUITETURA
meu_projeto/                 # Diretório raiz do projeto
├── credentials.json         # Arquivo JSON com as credenciais do Google Sheets
├── manage.py                # Arquivo principal para executar comandos Django
├── requirements.txt         # Lista de dependências do projeto
├── .env                     # Arquivo para variáveis de ambiente (opcional)
├── meu_projeto/             # Diretório do projeto Django
│   ├── __init__.py          # Arquivo que define o pacote Python
│   ├── asgi.py              # Configuração para ASGI (opcional)
│   ├── settings.py          # Configurações globais do projeto
│   ├── urls.py              # Rotas principais do projeto
│   ├── wsgi.py              # Configuração para WSGI (servidor de produção)
│   └── templates/           # Diretório de templates globais (opcional)
│       └── base.html        # Template base para herança (opcional)
├── formulario/              # App Django para o formulário
│   ├── migrations/          # Migrações de banco de dados do app
│   │   └── __init__.py      # Arquivo que define o pacote Python
│   ├── __init__.py          # Arquivo que define o pacote Python
│   ├── admin.py             # Configuração do admin do Django
│   ├── apps.py              # Configuração do app
│   ├── models.py            # Definição de modelos (opcional)
│   ├── forms.py             # Definição do formulário Django
│   ├── views.py             # Lógica de exibição do app
│   ├── urls.py              # Rotas do app
│   ├── static/              # Arquivos estáticos (CSS, JS, imagens)
│   │   ├── css/
│   │   │   └── style.css    # Estilos para o formulário
│   │   └── js/
│   │       └── script.js    # Scripts JavaScript (opcional)
│   └── templates/           # Templates específicos do app
│       └── formulario/
│           └── index.html   # Página do formulário
└── db.sqlite3               # Banco de dados SQLite (padrão do Django)
Instale Django:
sh
pip install django
Crie o projeto:
sh
django-admin startproject meu_projeto .
Crie o app:
sh
python manage.py startapp formulario
Iniciar projeto:
sh
python manage.py runserver
Como gerar a chave de uma conta de serviço:
Siga os passos abaixo para gerar as credenciais corretas:

Acesse o Console do Google Cloud:

Vá para o Google Cloud Console.

Ative a API do Google Sheets e a API do Google Drive:

Se você ainda não fez isso, ative as APIs necessárias para interagir com o Google Sheets e o Google Drive. Vá para APIs & Services > Library. Pesquise por Google Sheets API e Google Drive API. Ative ambas as APIs.

Crie uma conta de serviço:

No Console do Google Cloud, vá para IAM & Admin > Service Accounts. Clique em Create Service Account. Dê um nome e uma descrição à sua conta de serviço (por exemplo, SensorVille Service Account). Clique em Create e, na próxima tela, selecione a função Project > Editor (ou outra função apropriada dependendo do seu uso). Clique em Done para finalizar a criação da conta de serviço.

Gerar a chave da conta de serviço:

Na lista de contas de serviço, encontre a que você acabou de criar. Clique em Actions > Create Key. Selecione o formato JSON e clique em Create. O arquivo de chave será baixado automaticamente. Este é o arquivo que você usará no seu projeto.

Compartilhe sua planilha com a conta de serviço:

Abra a planilha do Google Sheets onde você deseja salvar os dados. No Google Sheets, clique em Compartilhar no canto superior direito. Adicione o e-mail da conta de serviço (ele estará no arquivo JSON que você gerou, algo como your-service-account@your-project-id.iam.gserviceaccount.com). Dê permissões de Editor para essa conta de serviço.