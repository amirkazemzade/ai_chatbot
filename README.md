# AI Chatbot (Telegram Bot with TF-IDF & Cosine Similarity)

This repository contains a **Python-based Telegram chatbot** that retrieves responses using a **Vector Space Model (VSM)** powered by **TF-IDF weighting** and **Cosine Similarity**.  
In addition to general conversational capabilities, the bot includes a **context-aware shopping list manager** that supports multi-turn interactions.

---

## Overview

The chatbot matches user messages against a predefined dataset of requests stored in a SQLite database. Each request is represented as a TF-IDF vector, and incoming queries are compared against all stored requests using cosine similarity to determine the most relevant response.

The system also maintains user conversation history to enable state-based features such as guided shopping list creation.

---

## Key Features

- **Vector Space Search**
  - Uses TF-IDF (Term Frequency–Inverse Document Frequency)
  - Cosine Similarity for semantic matching
  - Automatically selects the most relevant predefined response

- **Context-Aware Conversation**
  - Maintains per-user history
  - Supports multi-turn dialogs
  - Handles sequential questions such as product name → quantity

- **Shopping List Management**
  - Create and manage a personal shopping list per user
  - Add products and quantities via natural conversation
  - View the full shopping list on request

- **Repository Pattern**
  - Clean separation between data access and business logic
  - SQLite-based persistence layer
  - Modular and extensible architecture

- **Data Management Utilities**
  - Import requests and responses from Excel files
  - Automatically compute TF, IDF, TF-IDF, and vector lengths
  - Update database tables consistently

---

## Project Structure

```
amirkazemzade-ai_chatbot/
├── telegram_api.py
├── constants.py
├── requirements.txt
├── database.sqlite
├── datasource/
├── logic/
├── utility/
└── test/
```

---

## Dependencies

- Python 3.x  
- pyTelegramBotApi  
- openpyxl  

Install dependencies:

```bash
pip install pyTelegramBotApi openpyxl
```

---

## Configuration

Edit `constants.py` and set your Telegram Bot token:

```python
API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```

---

## Database Initialization & Training

Run the following scripts **in order**:

```bash
python utility/import_requests_from_excel.py
python utility/import_responses_from_excel.py
python utility/update_word_by_request.py
python utility/update_word.py
python utility/calculate_tfidf.py
python utility/update_request.py
```

---

## Running the Bot

```bash
python telegram_api.py
```

---

## Bot Commands

- `/start` – Initialize user and shopping list
- General chat – TF-IDF + cosine similarity response
- Shopping list – Multi-step product and quantity flow

---
