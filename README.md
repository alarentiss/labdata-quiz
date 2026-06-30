# Labdata Quiz - Gamificação de Marca

Quiz interativo sobre Inteligência Artificial criado para ativação de marca na Feira de Parceiros Arklok.

## 🎯 Características

- Quiz com 21 questões sobre IA e tecnologia
- Interface responsiva com cores da marca FIA (verde #084734 e #c3fa75)
- Resultado personalizado baseado no desempenho
- Sem dependências externas (apenas HTML, CSS e JavaScript)
- Deploy gratuito no Render

## 🚀 Como Usar Localmente

1. Clone este repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o servidor:
   ```bash
   python app.py
   ```
4. Abra no navegador: `http://localhost:5000`

## 📦 Estrutura do Projeto

```
labdata-quiz/
├── index.html          # Arquivo principal do quiz
├── app.py              # Servidor Flask
├── requirements.txt    # Dependências Python
├── Procfile            # Configuração para Render
├── .gitignore          # Arquivos ignorados no Git
└── README.md           # Este arquivo
```

## 🌐 Deploy no Render

1. Faça push do código para o GitHub
2. Acesse [render.com](https://render.com)
3. Conecte sua conta GitHub
4. Crie novo "Web Service"
5. Selecione este repositório
6. Configure:
   - **Name**: labdata-quiz
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
7. Clique em "Deploy"

Seu quiz estará disponível em: `https://labdata-quiz.onrender.com`

## 📝 Editando as Questões

As questões estão dentro do arquivo `index.html`, na seção `<script>`. Para adicionar, remover ou editar questões:

1. Abra `index.html` em um editor de texto
2. Localize o array `questions`
3. Adicione ou modifique conforme necessário
4. Salve e faça push para GitHub

Exemplo de estrutura de questão:
```javascript
{
    id: 1,
    text: "Pergunta aqui?",
    options: [
        { text: "Opção 1", correct: true },
        { text: "Opção 2", correct: false },
        { text: "Opção 3", correct: false }
    ]
}
```

## 🎨 Customizando as Cores

As cores podem ser alteradas no CSS (seção `<style>`):
- Verde profundo: `#084734`
- Verde decidido: `#c3fa75`

## 📊 Mensagens de Resultado

As mensagens finais estão configuradas na seção `resultMessages` do JavaScript. Cada mensagem corresponde a um nível de desempenho.

---

**Criado para FIA Business School - Labdata**
