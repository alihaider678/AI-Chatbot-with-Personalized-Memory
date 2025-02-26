# 🤖 AI Chatbot with Personalized Memory

## 📌 Overview
This project is an **AI-powered chatbot** that leverages:
- **Qdrant** as a vector database for storing and retrieving past conversations.
- **Hugging Face Sentence Transformers** for embedding and semantic search.
- **Gemini AI (Google Generative Language API)** for generating responses.

This chatbot can remember past conversations and respond with relevant contextual information.

---

## 🏗️ **Project Structure**
```
Task_Chatbot/
│── chatbot/
│   ├── bot.py             # Main chatbot execution file
│   ├── memory.py          # Memory storage & retrieval using Qdrant
│   ├── embedding.py       # Hugging Face embedding model for vector conversion
│   ├── gemini_ai.py       # Gemini AI API integration
│── tests/
│   ├── test_chatbot.py    # Unit tests for chatbot response verification
│   ├── test_memory.py     # Tests for memory storage and retrieval
│── .env                   # Stores API keys (DO NOT SHARE)
│── config.py              # Loads environment variables
│── requirements.txt       # Dependencies list
│── README.md              # This file
│── main.py                # (Optional) Entry point for running the chatbot
└── .gitignore             # Prevents sensitive files (e.g., venv) from being uploaded
```

---

## 🚀 **Setup & Installation**
### **1️⃣ Clone or Extract the Project**
If you received a **.zip file**, extract it.  
Otherwise, if hosted on GitHub, clone it:
```sh
git clone <repository_url>
cd Task_Chatbot
```

### **2️⃣ Create & Activate Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Configure Environment Variables**
Create a `.env` file in the root directory:
```
QDRANT_API_URL="https://your-qdrant-instance-url"
QDRANT_API_KEY="your-qdrant-api-key"
GEMINI_API_KEY="your-gemini-api-key"
```

### **5️⃣ Run the Chatbot**
```sh
python -m chatbot.bot
```

---

## 🎯 **How It Works**
1️⃣ **User inputs a message**  
2️⃣ **Embeddings**: The message is converted into a vector using **Hugging Face embeddings**  
3️⃣ **Memory Retrieval**: The vector is searched in **Qdrant** for similar past conversations  
4️⃣ **Response Generation**: **Gemini AI** uses the memory to generate an intelligent response  
5️⃣ **Response is returned to the user** 🎤  

---

## ✅ **Example Chat Interaction**
```
You: I am going to drink water.
Bot: Okay.

You: When did I last drink water?
Bot: Based on our previous conversation, you mentioned it on February 25th, 2025.

You: I plan to visit the park tomorrow.
Bot: That sounds like a nice plan. Enjoy your visit to the park!

You: What did I say about Mars?
Bot: I don't have any record of you mentioning Mars in our past conversations.
```

---

## 📌 **Testing the Chatbot**
To run unit tests:
```sh
pytest tests/
```

---

## ⚠️ **Notes**
- The **`venv/` folder is excluded** from version control (`.gitignore`).
- **Never share `.env` file publicly**, as it contains sensitive API keys.

---

## 💡 **Future Enhancements**
- [ ] Improve long-term memory recall  
- [ ] Add support for multiple users  
- [ ] Enhance response accuracy with fine-tuned models  

---

## 📜 **License**
This project is licensed under the **MIT License**.

---

## 👨‍💻 **Author**
**Ali Haider**  
GitHub: [alihaider678](https://github.com/alihaider678)  

---

🚀 **Now you can paste this into your `README.md` file in VS Code!** 🚀  
Let me know if you need any modifications! 🎯
