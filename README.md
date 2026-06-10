# SPS GenAI Assignment

## Features

- Bigram text generation API
- Word embedding API using spaCy
- FastAPI backend
- Docker deployment

## Run Locally

```bash
uv sync
uv run fastapi dev main.py
```

## Run with Docker

```bash
docker build -t sps-genai .
docker run -p 8000:8000 sps-genai
```

## API Endpoints

### POST /generate

Generate text using a bigram language model.

Example:

```json
{
  "start_word": "the",
  "length": 5
}
```

### POST /embedding

Return word embeddings using spaCy.

Example:

```json
{
  "word": "apple"
}
```
