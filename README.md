# GestureFlow: Controle do Spotify por Gestos com YOLOv8

<div align="center">
  <img src="https://github.com/R1chardJr/YOLOV8-Gesture-Based-Media-Control/blob/main/gif_example.gif" width="500">
</div>
<p align="center">
  GIF de exemplo de funcionamento do projeto
</p>

## 📖 Sobre o Projeto

O **GestureFlow** é uma aplicação de Visão Computacional desenvolvida em Python que permite ao usuário controlar o player de música do Spotify através de gestos com a mão, capturados em tempo real por uma webcam. O projeto utiliza o modelo de detecção de objetos **YOLOv8** para reconhecer os gestos e se comunica diretamente com a **API do Spotify** para executar os comandos, criando uma experiência de Interação Humano-Computador fluida e intuitiva.

Este projeto foi desenvolvido como um trabalho final de Redes Neurais, explorando o ciclo de vida completo de um projeto de Machine Learning, desde a coleta e anotação de dados até o treinamento do modelo e a criação de uma aplicação funcional. 

## ✨ Funcionalidades

* **Detecção em Tempo Real:** Reconhece gestos a partir do feed de uma webcam com alta velocidade e precisão.
* **Controle de Reprodução:**
    * **Play/Pause (Punho fechado ✊):** Inicia ou pausa a música atual.
    * **Próxima Faixa(Joinha 👍):** Pula para a próxima música da playlist ou álbum.
    * **Faixa Anterior(Mão aberta com os 5 dedos esticados 🖐):** Volta para a música anterior.
* **Interface Visual:** Exibe o feed da câmera com caixas delimitadoras (bounding boxes) e rótulos sobre os gestos detectados, fornecendo feedback visual instantâneo.
* **Integração Robusta:** Comunica-se diretamente com a API do Spotify, funcionando mesmo que o aplicativo não esteja em foco.

## 🛠️ Tecnologias Utilizadas

A arquitetura do projeto foi construída utilizando um conjunto de ferramentas modernas para Deep Learning e desenvolvimento de aplicações:

| Ferramenta          | Descrição                                                                                             |
| :------------------ | :---------------------------------------------------------------------------------------------------- |
| **Python** | Linguagem principal para toda a lógica do projeto.                                                    |
| **YOLOv8** | Modelo de Deep Learning de ponta para a detecção de objetos (gestos) em tempo real.                   |
| **PyTorch** | Framework que serve como base para o treinamento e inferência do YOLOv8.                              |
| **OpenCV** | Biblioteca essencial para captura da webcam, manipulação de imagens e exibição da interface visual.   |
| **Roboflow** | Plataforma utilizada para a anotação e pré-processamento do dataset de imagens customizado.           |
| **Spotipy** | Wrapper Python para a API do Spotify, simplificando a autenticação (OAuth 2.0) e os comandos.         |
| **Python-Dotenv** | Para gerenciamento seguro das credenciais da API, carregando-as a partir de um arquivo `.env`.        |
| **Google Colab** | Ambiente de nuvem utilizado para o treinamento do modelo com aceleração por GPU.                      |

## ⚙️ Configuração e Instalação

Siga os passos abaixo para executar o projeto localmente.

#### **Pré-requisitos**
* Python 3.9+
* Uma conta no Spotify (Premium é recomendado para total funcionalidade da API)
* Uma webcam conectada

#### **Passos de Instalação**

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/R1chardJr/YOLOV8-Gesture-Based-Media-Control.git
    cd YOLOV8-Gesture-Based-Media-Control
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente
    python -m venv venv
    # Ativar no Windows
    .\venv\Scripts\activate
    # Ativar no macOS/Linux
    source venv/bin/activate
    ```


3.  **Configure a API do Spotify:**
    * Vá até o [Spotify for Developers Dashboard](https://developer.spotify.com/dashboard) e crie um novo App.
    * Copie seu **Client ID** e **Client Secret**.
    * Em "Edit Settings", adicione o seguinte **Redirect URI**: `http://127.0.0.1:8888/callback` e salve.

4.  **Configure as Variáveis de Ambiente:**
    * Na raiz do projeto, crie um arquivo chamado `.env`.
    * Abra o arquivo `.env` e preencha com suas credenciais do Spotify:
        ```env
        SPOTIPY_CLIENT_ID="SEU_CLIENT_ID_AQUI"
        SPOTIPY_CLIENT_SECRET="SEU_CLIENT_SECRET_AQUI"
        SPOTIPY_REDIRECT_URI="[http://127.0.0.1:8888/callback](http://127.0.0.1:8888/callback)"
        ```

## 🚀 Como Usar

1.  **Abra o Spotify:** Certifique-se de que o Spotify está aberto e tocando uma música em algum dispositivo (computador, celular, etc.).
2.  **Execute o script principal:** Com seu ambiente virtual ativado, rode o comando:
    ```bash
    python hand_control_spotify.py
    ```
3.  **Autorize a Aplicação:** Na primeira vez que rodar, uma janela do navegador abrirá pedindo para você autorizar o acesso à sua conta do Spotify. Faça o login e aprove.
4.  **Controle com Gestos:** Posicione sua mão em frente à webcam e use os gestos treinados para controlar a música.
5.  **Encerrar:** Pressione a tecla `Esc` para fechar a janela e encerrar o programa.

## 🧠 Treinamento do Modelo

O modelo `best.pt` incluído neste repositório foi treinado em um dataset customizado. O processo foi o seguinte:
1.  **Coleta de Dados:** Centenas de imagens de 3 gestos (`next`, `play_pause`, `previous`) foram capturadas.
2.  **Anotação:** As imagens foram anotadas na plataforma **Roboflow**, onde caixas delimitadoras foram desenhadas для cada gesto.
3.  **Pré-processamento:** O dataset foi pré-processado com um *resize* para 640x640 pixels e *data augmentation* para aumentar a robustez do modelo.
4.  **Treinamento:** O modelo `yolov8n` foi treinado por 50 épocas no Google Colab, utilizando a técnica de *fine-tuning*. O modelo final alcançou uma métrica **mAP50 de 0.995**, indicando altíssima precisão na identificação dos gestos.

## 📄 Documentação e Referências

Para uma análise mais aprofundada da metodologia, dos desafios encontrados e dos resultados detalhados deste projeto, consulte o artigo científico elaborado como parte do trabalho:

* **[Artigo Completo: Desenvolvimento de um Sistema de Controle de Mídia por Gestos com YOLOv8 e API do Spotify](https://github.com/R1chardJr/YOLOV8-Gesture-Based-Media-Control/blob/main/Artigo_ProjetoFinal_Redes_Neurais_Richard.pdf)**

O artigo aborda em detalhes a fundamentação teórica, a arquitetura do sistema, o processo de treinamento do modelo e a análise dos resultados obtidos.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---
Feito com ❤️ por **Richard Junior**.
