# Python PowerUp

Repositório agrupando vários projetos em Python. Cada pasta contém um projeto separado com seu próprio propósito, dependências e uso.

---

## 📂 Estrutura

```
python-powerup/
┣ projeto-1/
┣ projeto-2/
┣ projeto-3/
┣ projeto-4/
┗ README.md     # Este arquivo
```

---

## 🧩 Projetos

Aqui estão os projetos inclusos:

| Projeto | Descrição | Localização |
|---------|------------|-------------|
| **Projeto 1** | *Automação de tarefas (Pyautogui + Pandas)* | `projeto-1/` |
| **Projeto 2** | *Análise de dados* | `projeto-2/` |
| **Projeto 3** | *Inteligência artificial e previsões* | `projeto-3/` |
| **Projeto 4** | *Descreva aqui o que o Projeto 4 faz.* | `projeto-4/` |

---

## 🔧 Instalação Geral

Para usar qualquer um dos projetos:

1. Clone este repositório:

   ```bash
   git clone https://github.com/hemkdev/python-powerup.git
   ```

2. Entre na pasta do projeto que deseja executar:

   ```bash
   cd python-powerup/projeto-1
   ```

3. Crie um ambiente virtual (recomendado):

   ```bash
   python -m venv venv
   # ou no Windows:
   # py -m venv venv
   ```

4. Ative o ambiente virtual:

   - **Linux / macOS**:

     ```bash
     source venv/bin/activate
     ```

   - **Windows**:

     ```powershell
     venv\Scripts\activate
     ```

5. Instale as dependências específicas do projeto:

   ```bash
   pip install -r requirements.txt
   ```

---


## 💡 Boas práticas

- Sempre use ambientes virtuais separados para evitar conflito de dependências.  
- Teste com dados de entrada simples primeiro, para garantir que tudo está funcionando.  
- Documente as dependências específicas de cada projeto (versão do Python, bibliotecas, etc.).  
- Mantenha cada projeto isolado: se for possível, evite / minimize efeitos cruzados entre eles.
