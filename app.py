from flask import Flask
import os

app = Flask(__name__, static_folder=None)

@app.route('/')
def index():
    # Encontra o caminho do arquivo index.html
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return html_content, 200, {'Content-Type': 'text/html; charset=utf-8'}
    except FileNotFoundError:
        return f"Erro: arquivo index.html não encontrado", 404
    except Exception as e:
        return f"Erro ao ler o arquivo: {str(e)}", 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
