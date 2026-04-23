# 💰 MoneyMind AI Chatbot

## 📌 Overview

MoneyMind is a personal finance advisory chatbot built using **TF-IDF and cosine similarity**.
It answers common financial queries and provides interactive calculators for better financial planning.

---

## 🚀 Features

* 🤖 FAQ-based chatbot (15+ financial queries)
* 🧠 NLP-powered query matching (TF-IDF + cosine similarity)
* 🔤 Typo handling using fuzzy matching (difflib)
* 💡 Alias mapping for financial acronyms
* 🧮 Financial calculators:

  * EMI Calculator
  * SIP Calculator
  * Savings Goal Calculator
* ⚠️ Fallback handling for unknown queries
* 🎨 Interactive UI built with Streamlit

---

## 🧠 How It Works

1. User enters a query
2. Input is normalized and cleaned
3. Typo correction using fuzzy matching
4. Text converted into vectors using TF-IDF
5. Cosine similarity finds the closest FAQ
6. If similarity < threshold → fallback response
7. Otherwise → return matched answer

---

## 📂 Project Structure

```
MoneyMind-Chatbot/
│
├── chatbot.py                    # Main Streamlit application
├── P8_Chatbot_FAQ_Bank.csv       # FAQ dataset
├── requirements.txt              # Dependencies
├── README.md                     # Documentation
```

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* Pandas

---

## ▶️ Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/MoneyMind-Chatbot.git
cd MoneyMind-Chatbot

pip install -r requirements.txt
streamlit run chatbot.py
```

---

## 🧪 Sample Test Cases

| Input             | Output                 |
| ----------------- | ---------------------- |
| what is sip       | Correct answer         |
| sipp              | Correct (typo handled) |
| what is repo rate | Correct                |
| random text       | Fallback response      |

---

## 📊 Accuracy

* Tested on 10 queries
* Achieved ~80–85% accuracy

---

## ⚠️ Limitations

* Does not understand deep context (TF-IDF limitation)
* Limited to predefined dataset
* No personalization of financial advice

---

## 🔮 Future Improvements

* Use advanced NLP models (BERT / LLM like GPT)
* Expand dataset
* Add multilingual support
* Deploy with database backend

---

## 🎯 Conclusion

This project demonstrates a hybrid approach combining:

* NLP-based retrieval system
* Rule-based financial tools

to build a practical personal finance chatbot.

---

## 👩‍💻 Author

Ashna Sharma

---
