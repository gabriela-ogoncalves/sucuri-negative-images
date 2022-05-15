# Imagens negativas com Sucuri 
[![Python 3.8.10](https://img.shields.io/badge/python-3.8.10-blue.svg)](https://www.python.org/downloads/release/python-360/)

### Trabalho realizado por: 
- Caio Saud
- Carolina Carvalhosa
- Gabriela Gonçalves

## Descrição

Utilizamos a biblioteca Sucuri para transformar imagens coloridas em imagens negativas para a matéria de Sistemas Distribuídos.


## Instalação

1. Instalar a [Python Imaging Library](https://pillow.readthedocs.io/en/stable/installation.html) através dos comandos:

    ```
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade Pillow
    ```

2. Instalar as dependências necessárias para rodar o projeto:

    ```
    pip install numpy scikit-image
    ```


## Rodando o Projeto

Já existem imagens dentro da pasta `imgs`, mas, caso queira, é possível adicionar novas.

Para rodar o projeto, execute o comando abaixo.

```
python3 main.py 1
```

Observe que a pasta [negative_images](./negative_imgs/) está inicialmente vazia, pois o processo para torná-las negativas ainda não foi iniciado. Após rodar o comando, as imagens negativas serão inseridas automaticamente nessa pasta. 

> O argumento passado é o número de workers. No caso do exemplo, temos apenas 1.

> Testado em distribuição Debian GNU/Linux 


## Resultados

Segue abaixo um exemplo do resultado obtido.

<div style="width: 100%; display:flex; justify-content:center; text-align:center">
    <div>
        <strong>Antes</strong><br>
        <img src="./docs/original_image.jpeg" width="350" alt="Antes">
    </div>
    <div>
        <strong>Depois</strong><br>
        <img src="./docs/negative_image.png" width="350" alt="Depois">
    </div>
</div>
