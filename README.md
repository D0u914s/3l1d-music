# 3l1d Music - Streaming de Músicas

Uma aplicação web Django para streaming de músicas, desenvolvida com Python e Django.

## Funcionalidades

- Upload de músicas com capas
- Reprodução de músicas
- Biblioteca de músicas organizada
- Interface moderna e responsiva

## Tecnologias Utilizadas

- Python 3.x
- Django 5.1.6
- Bootstrap 5
- Font Awesome
- SQLite3

## Requisitos

- Python 3.x
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/3l1d-music.git
cd 3l1d-music
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Crie um superusuário:
```bash
python manage.py createsuperuser
```

6. Inicie o servidor:
```bash
python manage.py runserver
```

7. Acesse a aplicação em http://localhost:8080

## Estrutura do Projeto

```
3l1d-music/
├── media/
│   ├── covers/     # Imagens de capa das músicas
│   └── music/      # Arquivos MP3
├── music_stream/   # Aplicação principal
├── music_stream_project/  # Configurações do projeto
├── manage.py
└── requirements.txt
```

## Contribuição

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Seu Nome - [@seu_twitter](https://twitter.com/seu_twitter) - email@exemplo.com

Link do Projeto: [https://github.com/seu-usuario/3l1d-music](https://github.com/seu-usuario/3l1d-music) 