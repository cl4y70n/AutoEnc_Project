# **AutoEnc — Sistema de Detecção de Fraudes com Autoencoders**

## **Descrição do Projeto**

O **AutoEnc** é um sistema de **detecção de fraudes financeiras** usando **Deep Learning não supervisionado**.
Ele identifica transações suspeitas com base em padrões aprendidos a partir de transações legítimas.

O projeto combina:

* **Autoencoders** para detectar anomalias pelo erro de reconstrução.
* **PCA (Principal Component Analysis)** para reduzir dimensionalidade e acelerar processamento.
* **K-Means** para criar clusters interpretáveis das transações.
* **Dashboard Streamlit** para visualização interativa de scores de anomalia e alertas.

---

## **Arquitetura do Projeto**

```
AutoEnc_Project/
│
├─ data/
│  ├─ raw/                  # Dados brutos de transações
│  ├─ processed/            # Dados limpos e normalizados
│  └─ features/             # Features extraídas e PCA
│
├─ src/
│  ├─ data_loader/          # Carregamento de dados
│  │  └─ load_data.py
│  ├─ preprocessing/        # Limpeza, normalização, feature engineering
│  │  └─ feature_engineering.py
│  ├─ models/               # Modelos Autoencoder, PCA e K-Means
│  │  ├─ autoencoder.py
│  │  ├─ pca_model.py
│  │  └─ kmeans_model.py
│  ├─ anomaly_detection/    # Cálculo de score e detecção de anomalias
│  │  └─ detect.py
│  ├─ evaluation/           # Métricas de performance
│  │  └─ evaluate.py
│  ├─ utils/                # Funções auxiliares
│  │  └─ helpers.py
│  └─ dashboard/            # Dashboard interativo
│     └─ app.py
│
├─ notebooks/               # EDA e análise exploratória
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ params.yaml              # Hiperparâmetros do Autoencoder, PCA e K-Means
└─ README.md
```

---

## **Tecnologias e Bibliotecas**

* **Python 3.10+**
* **Deep Learning:** PyTorch ou TensorFlow (Autoencoders)
* **Dimensionality Reduction:** PCA (scikit-learn)
* **Clustering:** K-Means (scikit-learn)
* **Data Handling:** Pandas, Numpy
* **Visualização:** Matplotlib, Seaborn, Plotly
* **Dashboard:** Streamlit
* **Deployment:** Docker + Docker Compose
* **MLOps (opcional):** MLflow para monitoramento de scores e modelos

---

## **Funcionalidades**

1. Carregamento de dados históricos de transações financeiras.
2. Pré-processamento e feature engineering (normalização, métricas de transações).
3. Redução de dimensionalidade via PCA.
4. Treinamento de Autoencoder em transações legítimas.
5. Detecção de anomalias pelo erro de reconstrução.
6. Clustering interpretável com K-Means.
7. Avaliação de performance com métricas: ROC-AUC, F1-score.
8. Dashboard Streamlit para visualização de resultados, alertas e distribuição de scores.

---

## **Pipeline de Desenvolvimento**

1. **Coleta de dados**: CSVs ou bancos de dados de transações em `data/raw/`.
2. **Pré-processamento e Feature Engineering**: limpeza de dados, normalização, extração de features.
3. **Redução de dimensionalidade**: aplicação de PCA.
4. **Treinamento do Autoencoder**: modelo não supervisionado treinado apenas com dados legítimos.
5. **Detecção de anomalias**: cálculo do erro de reconstrução e definição de threshold.
6. **Clustering interpretável**: aplicação de K-Means sobre embeddings ou features PCA.
7. **Avaliação**: métricas ROC-AUC, F1-Score e análise visual dos scores.
8. **Pipeline automatizado**: processa novos dados, gera scores e envia alertas.
9. **Dashboard**: visualização interativa e alertas de fraudes em tempo real.

---

## **Como Rodar Localmente**

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/autoenc-project.git
cd autoenc-project
```

### 2. Criar e ativar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Colocar dados de transações

* CSVs em `data/raw/`

### 5. Executar scripts de teste

```bash
python src/data_loader/load_data.py
python src/preprocessing/feature_engineering.py
python src/models/autoencoder.py
python src/models/pca_model.py
python src/models/kmeans_model.py
python src/anomaly_detection/detect.py
```

### 6. Rodar Dashboard Streamlit

```bash
streamlit run src/dashboard/app.py
```

---

## **Deploy com Docker**

1. Build da imagem:

```bash
docker build -t autoenc:latest .
```

2. Rodar via Docker Compose:

```bash
docker-compose up --build
```

3. Acesse o dashboard: `http://localhost:8501`

---

## **Contribuição**

1. Fork do repositório
2. Criar branch: `git checkout -b feature/nome-feature`
3. Commit: `git commit -m "Descrição da feature"`
4. Push: `git push origin feature/nome-feature`
5. Abrir Pull Request

---

## **Autor**

* **Clayton** – [GitHub](https://github.com/cl4y70n)


Quer que eu faça isso agora?
