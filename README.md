# Flashcard Generator 🧠

An AI-powered Flashcard Generator that creates simple and easy-to-understand flashcards using a Hugging Face AI model.

## 🚀 Features

* Generate flashcards on any topic
* Choose the number of flashcards
* Uses Hugging Face Inference API
* Built with FastAPI
* Simple REST API
* Environment variables used for API token security

## 🛠️ Technologies Used

* Python
* FastAPI
* Hugging Face
* InferenceClient
* Google Gemma 2 2B
* Uvicorn
* python-dotenv

## 📁 Project Structure

```text
flashcard-generator/
│
├── app.py
├── main.py
├── README.md
├── .gitignore
├── .env
└── venv/
```

> `.env` and `venv/` are ignored by Git and are not uploaded to GitHub.

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd flashcard-generator
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn huggingface_hub python-dotenv
```

## 🔑 Environment Variables

Create a `.env` file in the project folder:

```env
HF_TOKEN=your_huggingface_token
```

Replace `your_huggingface_token` with your Hugging Face access token.

## ▶️ Run the API

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

API will run at:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

## 📌 API Endpoint

### Generate Flashcards

```text
POST /generate-flashcards
```

Parameters:

```text
topic = Python
count = 3
```

Example:

```text
/generate-flashcards?topic=Python&count=3
```

## 📖 Example Response

```json
{
  "topic": "Python",
  "count": 3,
  "flashcards": "Q: What is Python?\nA: A high-level programming language."
}
```

## 👨‍💻 Author

Vikash Kumar

---

⭐ If you find this project useful, feel free to star the repository!

