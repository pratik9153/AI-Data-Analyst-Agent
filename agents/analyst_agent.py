import json

from langchain_openai import ChatOpenAI

from utils.config import (
    OPENAI_API_KEY,
    OPENAI_MODEL
)


# ==================================================
# LLM
# ==================================================

llm = ChatOpenAI(
    model=OPENAI_MODEL,
    api_key=OPENAI_API_KEY,
    temperature=0
)


# ==================================================
# UNDERSTAND USER QUESTION
# ==================================================

def understand_question(
    question,
    profile
):

    prompt = f"""
You are an AI Data Analyst.

You are analyzing a CSV dataset.

Dataset columns:
{profile["column_names"]}

Numeric columns:
{profile["numeric_columns"]}

Categorical columns:
{profile["categorical_columns"]}

User question:
{question}

Choose the most appropriate analysis.

Available analysis types:

1. statistics

Use for:
- average
- mean
- median
- minimum
- maximum
- general numerical statistics

2. group_analysis

Use for:
- comparing categories
- total sales by region
- profit by category
- average values by group

3. correlation

Use for:
- relationship between two numeric columns

4. column_summary

Use for:
- information about a column
- missing values
- unique values
- data type

5. top_categories

Use for:
- most common category
- most frequent values
- highest count categories

Return ONLY valid JSON.

Format:

{{
    "analysis_type": "statistics",
    "column1": "Sales",
    "column2": ""
}}

Rules:

- Do not calculate anything.
- Only identify the required analysis.
- Use exact column names from the dataset.
- Do not invent column names.
"""

    response = llm.invoke(
        prompt
    )

    text = response.content

    text = text.replace(
        "```json",
        ""
    )

    text = text.replace(
        "```",
        ""
    )

    return json.loads(
        text.strip()
    )


# ==================================================
# GENERATE AI INSIGHTS
# ==================================================

def generate_answer(
    question,
    analysis_result
):

    prompt = f"""
You are a professional AI Data Analyst.

User question:
{question}

Actual analysis result:
{analysis_result}

Create a useful analytical response.

Return ONLY valid JSON using exactly this structure:

{{
    "key_finding": "...",
    "evidence": "...",
    "interpretation": "...",
    "data_note": "..."
}}

Rules:

1. Use ONLY the provided analysis result.

2. Never invent numbers.

3. key_finding:
Directly answer the user's question.

4. evidence:
Mention the most important numbers,
categories, or results.

5. interpretation:
Explain what the result means
in simple business language.

6. data_note:
Mention a limitation only if it
is relevant to the analysis.

7. Do not repeat the user's question.

8. Do not give generic statements.

9. Keep the response concise.

10. Use professional but simple English.

11. If the result is insufficient to answer
the question, clearly say so.
"""

    response = llm.invoke(
        prompt
    )

    text = response.content

    text = text.replace(
        "```json",
        ""
    )

    text = text.replace(
        "```",
        ""
    )

    return json.loads(
        text.strip()
    )