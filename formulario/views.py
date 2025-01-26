from django.shortcuts import render
from .forms import FormularioForm
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from io import BytesIO

def formulario_view(request):
    sucesso = False  # Variável para verificar se o cadastro foi bem-sucedido
    
    if request.method == "POST":
        form = FormularioForm(request.POST, request.FILES)
        if form.is_valid():
            # Configurar as credenciais do Google Sheets e Google Drive
            scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
            client = gspread.authorize(credentials)

            # Abrir a planilha
            sheet = client.open("SensorVille").sheet1

            # Processar o arquivo enviado
            file = form.cleaned_data.get('file')
            image_url = None
            if file:
                # Preparar o upload do arquivo diretamente do request.FILES
                file_content = file.read()  # Ler o conteúdo do arquivo
                file_stream = BytesIO(file_content)  # Converter para BytesIO
                file_stream.seek(0)  # Garantir que o ponteiro esteja no início do arquivo

                # Fazer upload diretamente para o Google Drive
                drive_service = build('drive', 'v3', credentials=credentials)
                media = MediaIoBaseUpload(file_stream, mimetype=file.content_type, resumable=True)
                file_metadata = {'name': file.name, 'mimeType': file.content_type}
                drive_file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

                # Obter o link público do arquivo no Google Drive
                file_id = drive_file.get('id')
                drive_service.permissions().create(
                    fileId=file_id,
                    body={'role': 'reader', 'type': 'anyone'}
                ).execute()

                image_url = f"https://drive.google.com/uc?id={file_id}"

            # Adicionar os dados à planilha
            sheet.append_row([
                form.cleaned_data['name'],
                float(form.cleaned_data['value']),
                form.cleaned_data['date'].strftime('%Y-%m-%d'),
                image_url if image_url else "Sem imagem"
            ])
            
            sucesso = True  # Marcar que o cadastro foi bem-sucedido

    else:
        form = FormularioForm()

    return render(request, 'formulario.html', {'form': form, 'sucesso': sucesso})
