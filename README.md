# 🤖 AI Data Analyst Agent

An AI-powered data analysis application that allows users to upload a CSV dataset, explore the data, create visualizations, and ask questions in natural language.

The project demonstrates how an **AI Agent can understand a user's question, select an appropriate analysis tool, execute the analysis using Python and Pandas, and generate a natural-language explanation of the result.**

---

## 🚀 Project Overview

The **AI Data Analyst Agent** combines:

* Python
* Pandas
* Streamlit
* OpenAI
* LangChain
* Data Analysis Tools
* Data Visualization
* Data Validation and Profiling

The main goal of the project is to understand the basic architecture of a **tool-using AI Agent**.

The agent does not perform numerical calculations itself. Instead:

1. The LLM understands the user's question.
2. The LLM identifies the required analysis.
3. The appropriate Python/Pandas tool performs the actual calculation.
4. The result is sent back to the LLM.
5. The LLM explains the result in simple language.

---

# 🏗️ Project Architecture

```text
                    ┌──────────────────────┐
                    │        User          │
                    │                      │
                    │ Upload CSV / Ask     │
                    │      Question        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Streamlit UI      │
                    │                      │
                    │ Upload + Analysis    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Data Loader      │
                    │                      │
                    │      Pandas          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Data Validator    │
                    │                      │
                    │ Check dataset        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Data Profiler     │
                    │                      │
                    │ Rows / Columns       │
                    │ Types / Missing      │
                    │ Numeric / Categorical│
                    └──────────┬───────────┘
                               │
                               ▼
                 ┌──────────────────────────────┐
                 │     AI Data Analyst Agent   │
                 │                              │
                 │ Understand User Question     │
                 └──────────────┬───────────────┘
                                │
                                ▼
                 ┌──────────────────────────────┐
                 │     Select Analysis Tool     │
                 └──────────────┬───────────────┘
                                │
             ┌──────────────────┼──────────────────┐
             │                  │                  │
             ▼                  ▼                  ▼
      ┌─────────────┐    ┌─────────────┐   ┌──────────────┐
      │ Statistics  │    │ Data        │   │ Visualization│
      │ Tool        │    │ Analysis    │   │ Tool         │
      │             │    │ Tool        │   │              │
      │ Mean        │    │ Group       │   │ Histogram    │
      │ Median      │    │ Analysis    │   │ Bar Chart    │
      │ Min / Max   │    │ Top Values  │   │ Scatter Plot │
      │ Correlation │    │ Column Info │   │              │
      └──────┬──────┘    └──────┬──────┘   └──────┬───────┘
             │                  │                  │
             └──────────────────┼──────────────────┘
                                │
                                ▼
                    ┌──────────────────────┐
                    │   Analysis Result    │
                    │                      │
                    │ Python / Pandas      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │         LLM          │
                    │                      │
                    │ Generate Explanation │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     AI Insights      │
                    │                      │
                    │ Key Finding          │
                    │ Evidence             │
                    │ Interpretation        │
                    │ Data Note             │
                    └──────────────────────┘
```

---

# 🔄 AI Agent Tool Workflow

The core agent workflow is:

```text
User Question
      │
      ▼
Understand Question
      │
      ▼
Select Analysis
      │
      ├──────────────► Statistics
      │
      ├──────────────► Group Analysis
      │
      ├──────────────► Correlation
      │
      ├──────────────► Column Summary
      │
      └──────────────► Top Categories
                         │
                         ▼
                  Pandas Analysis
                         │
                         ▼
                  Analysis Result
                         │
                         ▼
                     LLM
                         │
                         ▼
                  AI Explanation
```

### Example

User asks:

> "Which region has the highest sales?"

The agent follows:

```text
Question
   ↓
Understand Question
   ↓
group_analysis
   ↓
Pandas groupby()
   ↓
Calculate sales by region
   ↓
Find highest region
   ↓
LLM explains result
   ↓
AI Insight
```

The important point is that **Pandas performs the actual calculation**, while the LLM handles understanding and explanation.

---

# 🧰 Available Tools

The project contains three main tool modules.

## 1. Statistics Tool

File:

```text
tools/statistics.py
```

Provides:

* Mean
* Median
* Minimum
* Maximum
* Count
* Correlation

Example questions:

```text
What is the average sales?

What is the maximum profit?

What is the relationship between sales and profit?
```

---

## 2. Data Analysis Tool

File:

```text
tools/data_analysis.py
```

Provides:

* Column summary
* Group analysis
* Top categories

Example questions:

```text
Which region has the highest sales?

Which category generates the most profit?

What are the most common products?
```

---

## 3. Visualization Tool

File:

```text
tools/visualization.py
```

Provides:

* Histogram
* Bar Chart
* Scatter Plot

These tools use Matplotlib to create visual representations of the dataset.

---

# 📊 Application Features

### 📂 CSV Upload

Upload a CSV dataset directly through the Streamlit interface.

### 📊 Data Explorer

View:

* Number of rows
* Number of columns
* Duplicate rows
* Missing values
* Dataset preview
* Column information
* Data types
* Unique values

### 📈 Visualizations

Create:

* Histograms
* Bar charts
* Scatter plots

### 🧠 AI Data Analyst

Ask natural-language questions about your dataset.

For example:

```text
What is the average sales?

Which region has the highest sales?

Which category generates the most profit?

What is the relationship between discount and profit?
```

### 🔍 Data Quality

Check:

* Missing values
* Duplicate rows
* Data types

### 💡 AI Insights

The AI generates:

* Key Finding
* Evidence
* Interpretation
* Data Note

---

# 📁 Project Structure

```text
AI Data Analyst Agent/
│
├── app.py
│
├── agents/
│   ├── __init__.py
│   └── analyst_agent.py
│
├── tools/
│   ├── __init__.py
│   ├── statistics.py
│   ├── data_analysis.py
│   └── visualization.py
│
├── data_processing/
│   ├── __init__.py
│   ├── loader.py
│   ├── profiler.py
│   └── validator.py
│
├── visualization/
│   ├── __init__.py
│   └── charts.py
│
├── utils/
│   ├── __init__.py
│   ├── config.py
│   ├── logger.py
│   └── exceptions.py
│
├── data/
│   ├── uploads/
│   └── outputs/
│
├── tests/
│   ├── test_profiler.py
│   └── test_tools.py
│
├── .github/
│   └── workflows/
│       └── main.yml
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🧩 Technology Stack

| Technology     | Purpose               |
| -------------- | --------------------- |
| Python         | Core programming      |
| Pandas         | Data analysis         |
| NumPy          | Numerical operations  |
| Matplotlib     | Visualization         |
| Streamlit      | Web interface         |
| OpenAI         | LLM                   |
| LangChain      | LLM integration       |
| python-dotenv  | Environment variables |
| Pytest         | Testing               |
| GitHub Actions | CI/CD                 |

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/pratik9153/AI-Data-Analyst-Agent
```

### 2. Navigate to the project

```bash
cd "AI Data Analyst Agent"
```

### 3. Create virtual environment

```bash
python -m venv venv
```

### 4. Activate environment

Windows:

```cmd
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

Never commit your `.env` file to GitHub.

The project already includes `.env` in `.gitignore`.

---

# ▶️ Run the Application

Run:

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

# 🧪 Testing

Run the tests using:

```bash
pytest
```

The project also includes GitHub Actions for automated testing.

```text
.github/
└── workflows/
    └── main.yml
```

---

# 🧠 What I Learned From This Project

This project helped me understand how an **AI Agent** works in a practical application.

### AI Agent Concepts

* LLM-based question understanding
* Tool selection
* Tool execution
* Passing results back to an LLM
* Natural-language response generation
* Structured AI outputs

### Data Engineering / ML Concepts

* CSV data loading
* Data validation
* Data profiling
* Missing-value analysis
* Duplicate detection
* Pandas-based analysis
* Data visualization

### Application Development

* Streamlit
* Modular Python architecture
* Exception handling
* Logging
* Environment variables
* Testing
* GitHub Actions

---

# 🎯 Key Learning

The most important concept learned from this project is:

```text
LLM ≠ Calculator
```

The LLM understands **what needs to be done**, while Python/Pandas performs the **actual data analysis**.

```text
LLM
 ↓
Understand
 ↓
Choose Tool
 ↓
Python Tool
 ↓
Calculate
 ↓
Result
 ↓
LLM
 ↓
Explain
```

This is the basic foundation of building **tool-using AI Agents**.

---

# 🔮 Future Improvements

Possible future improvements include:

* More data-analysis tools
* SQL database support
* More visualization types
* RAG-based business documentation
* Advanced agent workflows
* Multi-agent systems
* Agentic AI workflows
* Evaluation and monitoring
* Cloud deployment

---

# 👨‍💻 Author

**Pratik Choudhary**

MCA (AI/ML) Student

Interested in:

* Machine Learning
* Deep Learning
* NLP
* Generative AI
* RAG
* AI Agents
* MLOps

---

## ⭐ Project Summary

**AI Data Analyst Agent** is a practical AI application that combines an LLM with Python data-analysis tools to allow users to interact with CSV datasets using natural language.

The project demonstrates the fundamental workflow of a **tool-using AI Agent**:

```text
Understand → Select Tool → Execute → Analyze → Explain
```
