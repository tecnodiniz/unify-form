# UnifyForm

Um sistema simples para unificar formulários de diferentes fontes usando inteligência artificial.

## Sobre o Projeto

UnifyForm é uma aplicação web desenvolvida com Flask que permite aos usuários:

1. Fazer upload de múltiplos formulários (PDF, DOCX, DOC)
2. Extrair automaticamente perguntas e campos desses documentos
3. Gerar um formulário unificado combinando as perguntas de todos os documentos
4. Exportar o formulário unificado em diferentes formatos (DOCX, XLSX, HTML)
5. Preencher o formulário online

O sistema utiliza inteligência artificial (OpenAI) para extrair perguntas dos documentos e gerar formulários unificados de forma inteligente.

## Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Processamento de Documentos**: PyPDF2, python-docx
- **Exportação de Arquivos**: XlsxWriter, reportlab
- **IA**: OpenAI API

## Requisitos

- Python 3.7+
- Chave de API da OpenAI (opcional, mas recomendada para melhores resultados)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/formularios-simples_IA.git
   cd formularios-simples_IA
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv

   # No Windows
   venv\Scripts\activate

   # No Linux/Mac
   source venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requiriments.txt
   ```

4. Configure as variáveis de ambiente:
   Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
   ```
   SECRET_KEY=sua_chave_secreta
   OPENAI_API_KEY=sua_chave_api_openai
   ```

## Executando o Projeto

1. Inicie o servidor Flask:

   ```bash
   python run.py
   ```

2. Acesse a aplicação em seu navegador:
   ```
   http://localhost:5000
   ```

## Estrutura do Projeto

```
formularios-simples_IA/
├── app/                    # Pasta principal da aplicação
│   ├── forms/              # Formulários gerados
│   ├── uploads/            # Arquivos enviados pelos usuários
│   ├── img/                # Imagens da aplicação
│   ├── main/               # Blueprint principal da aplicação
│   │   └── routes.py       # Rotas da aplicação
│   ├── services/           # Serviços e utilitários
│   │   ├── extract.py      # Extração de perguntas de documentos
│   │   ├── generate.py     # Geração dos formulários unificados
│   │   ├── storage.py      # Manipulação de dados persistentes
│   │   └── utils.py        # Funções utilitárias
│   ├── static/             # Arquivos estáticos (CSS, JS, imagens)
│   ├── templates/          # Templates HTML
│   ├── __init__.py         # Inicialização da aplicação
│   └── config.py           # Configurações da aplicação
├── venv/                   # Ambiente virtual Python
├── .env                    # Variáveis de ambiente (não versionado)
├── .gitignore              # Arquivos ignorados pelo git
├── requiriments.txt        # Dependências do projeto
├── run.py                  # Script para executar a aplicação
└── README.md               # Este arquivo
```

## Funcionalidades

### 1. Upload de Formulários

- Faça upload de múltiplos arquivos de diferentes seguradoras ou fontes
- Suporte para arquivos PDF, DOCX e DOC

### 2. Extração de Perguntas

- Extração automática de perguntas e campos dos documentos
- Utiliza IA para identificar perguntas relevantes

### 3. Geração de Formulário Unificado

- Combinação inteligente de perguntas de diferentes fontes
- Eliminação de perguntas duplicadas ou similares
- Organização lógica das seções e campos

### 4. Exportação de Formulários

- Exportação em formato DOCX (Microsoft Word)
- Exportação em formato XLSX (Microsoft Excel)
- Exportação em formato HTML para preenchimento online

### 5. Preenchimento Online

- Interface web para preenchimento do formulário unificado
- Compartilhamento do link do formulário com clientes

## Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request
