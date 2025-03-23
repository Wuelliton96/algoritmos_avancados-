# 🌀 Sort Algorithms com Python + Jaeger

Este projeto implementa algoritmos de ordenação clássicos (como Bubble Sort, Quick Sort e Merge Sort) em **Python**, utilizando o padrão de projeto **Strategy**.  
As execuções dos algoritmos são rastreadas com **OpenTelemetry** e os dados são visualizados com o **Jaeger**.

---

## 🛠 Pré-requisitos

- [Docker](https://www.docker.com/) instalado na sua máquina

---

## 🚀 Como Rodar o Projeto

### 1. Construa a imagem da aplicação

```bash
docker build -t sort-app .
```

### 2. Rode a aplicação Python

```bash
docker run --name sort-app --network host sort-app
```

### 3. Rode o Jaeger em outro terminal

```bash
docker run -d --name jaeger \
  -e COLLECTOR_ZIPKIN_HOST_PORT=:9411 \
  -p 6831:6831/udp \
  -p 16686:16686 \
  jaegertracing/all-in-one:1.52
```

---

## 📊 Visualizar os Traces no Jaeger

1. Acesse o Jaeger no navegador:

```
http://localhost:16686
```

2. Em **Service**, selecione `sort-service`.

3. Clique em **Find Traces** para visualizar:
   - Algoritmo utilizado (ex: `sort_BubbleSort`)
   - Tempo de execução
   - Tamanho do array
   - Resultado ordenado (opcional)


---

## 🧹 Parar e Limpar os Containers

```bash
docker stop sort-app jaeger
docker rm sort-app jaeger
```

---

## 👨‍💻 Integrantes

- ALEXANDRE TESSARO VIEIRA  
- EDSON BORGES POLUCENA  
- LEONARDO PEREIRA BORGES  
- RICHARD SCHMITZ RIEDO  
- WUELLITON CHRISTIAN DOS SANTOS  
