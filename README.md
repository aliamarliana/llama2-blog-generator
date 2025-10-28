# 🦙 LLaMA 2 Blog Generator

An **AI-powered blog generator** built with **LLaMA 2**, **LangChain**, and **Streamlit**.  
This app allows you to generate professional blogs tailored to specific audiences — such as *Researchers*, *Data Scientists*, or *Common Readers* — all powered by a local LLaMA 2 model.

---

## 🚀 Features
- 🧠 **LLaMA 2 integration** via `ctransformers` for efficient local inference  
- 🧩 **LangChain PromptTemplate** for dynamic and structured prompts  
- 💻 **Streamlit UI** for quick input and blog generation  
- ⚙️ **Offline support** — no API key or internet needed once the model is downloaded  
- ✍️ **Custom blog style and length control**

---

## 📦 Project Structure

```bash
llama2-blog-generator/
├── app.py # Main Streamlit app
├── requirements.txt # Dependencies
├── models/
│ └── llama-2-7b-chat.ggmlv3.q8_0.bin # LLaMA 2 model file (to be downloaded)
└── README.md
```


---

## 🪜 Setup Guide


### 1️⃣ Create and Activate Virtual Environment
Using conda:
```bash
conda create -p venv python==3.9 -y
conda activate ./venv
```

Or using venv (standard Python):
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```


### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```


### 3️⃣ Download the LLaMA 2 Model
Download the **LLaMA 2 7B Chat GGML** model from Hugging Face(requires account acceptance).

Example:
```bash
llama-2-7b-chat.ggmlv3.q8_0.bin
```

Once downloaded, place it under the `/models` directory:

Example:
```bash
models/llama-2-7b-chat.ggmlv3.q8_0.bin
```


### ▶️ Run the App
Launch Streamlit:
```bash
streamlit run app.py
```

---

## 🧠 How It Works
1. User Input — Enter a blog topic, desired word count, and target audience.
2. Prompt Template — LangChain constructs a structured prompt.
3. LLaMA 2 Generation — The ctransformers library loads the quantized model and generates the text locally.
4. Display — Streamlit shows the final blog output interactively.


---

## 🎥 Code Reference
This project was **inspired by the tutorial by Krish Naik**:  
🔗 [Complete Langchain GEN AI Crash Course With 6 End To End LLM Projects With OPENAI,LLAMA2,Gemini Pro](https://www.youtube.com/watch?v=aWKrL4z5H6w&t=8263s)
