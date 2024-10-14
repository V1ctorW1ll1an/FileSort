<p align="center">
  <img src="https://github.com/V1ctorW1ll1an/FileSort/blob/main/assets/img.webp" alt="FileSort Logo" width="400"/>
</p>

---

# FileSort

O **FileSort** foi criado para facilitar a organização de arquivos em diretórios, separando-os automaticamente com base em suas extensões. O projeto utiliza Python para realizar operações de movimentação de arquivos, aplicando práticas eficientes de manipulação de arquivos e pastas.

## Propósito

O projeto foi desenvolvido com o intuito de aprender e aplicar:

- Manipulação de arquivos e diretórios utilizando `pathlib` e `shutil`
- Argumentos de linha de comando com `argparse`
- Gerenciamento de exceções e logging em operações com arquivos
- Organização de arquivos em subdiretórios automaticamente
- Práticas de logging detalhadas com registro de erros

## Requisitos

- **Python 3.12.2** (especificado no `.python-version` via `pyenv`)
- **Bibliotecas padrão do Python** (sem dependências externas)

## Como Utilizar

### 1. Clonar o repositório

```bash
git clone git@github.com:V1ctorW1ll1an/FileSort.git
cd filesort
```

### 2. Criar o ambiente virtual

Crie o ambiente virtual para o projeto da seguinte maneira:

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual

- **Linux/MacOS**:

  ```bash
  source venv/bin/activate
  ```

- **Windows**:

  ```bash
  venv\Scripts\activate
  ```

### 4. Instalar dependências (se necessário)

Não há dependências externas a serem instaladas, apenas as bibliotecas padrão do Python.

### 5. Executar o programa

Para organizar os arquivos de uma pasta com base nas suas extensões, passe o caminho como argumento:

```bash
python main.py --path="<caminho-da-pasta>"
```

O programa moverá todos os arquivos para subpastas nomeadas de acordo com suas extensões. Se o arquivo não tiver uma extensão, ele será ignorado.

### 6. Logging

Todas as operações realizadas, assim como erros e exceções, serão registradas no arquivo `file_operations.log` para fins de monitoramento e auditoria.

## Estrutura do Projeto

- **main.py**: O script principal que organiza os arquivos.
- **file_operations.log**: Arquivo de log onde as operações e erros são registrados.

## Como Contribuir

Contribuições são sempre bem-vindas! Siga os passos abaixo para colaborar:

1. Faça um **fork** do projeto
2. Crie uma **branch** para sua feature ou correção:
   ```bash
   git checkout -b minha-feature
   ```
3. **Commit** suas alterações:
   ```bash
   git commit -m "Adicionando uma nova feature"
   ```
4. Envie para o **branch** principal:
   ```bash
   git push origin minha-feature
   ```
5. Abra um **pull request**

Sinta-se à vontade para abrir **issues** caso encontre bugs ou tenha sugestões de melhorias!

## Licença

Este projeto é livre para uso educacional. Utilize-o para aprender, modificar e compartilhar!

---

Este `README.md` fornece uma visão geral clara do projeto **FileSort**, explica como configurá-lo e executá-lo, além de incluir instruções de contribuição.
