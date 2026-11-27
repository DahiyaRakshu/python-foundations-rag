# Python Foundations Knowledge Bot

A small Streamlit RAG chatbot about Python fundamentals. It indexes the included public-domain sample guides when no user files are uploaded. Visitors provide their own Gemini API key and may upload PDFs, TXT, or Markdown files. The key and uploaded text are used in session memory and are not saved by this app.

## Extra feature

**Suggested questions:** four topic-specific sidebar buttons populate the chat with useful starter questions.

## Run locally

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

Get a Gemini key from [Google AI Studio](https://aistudio.google.com/). Do not commit a key.

## Sample knowledge base and sources

The two concise study guides in `knowledge_base/` were written for this project from general Python language knowledge; they are not copied from a third-party work. To expand the set to the assignment's suggested page count, replace or supplement them with openly licensed/selectable-text documents and record their exact source links here.

- `python_core.md` — original overview of variables, built-in types, operators, conditionals, and loops.
- `python_functions.md` — original overview of functions, collections, exceptions, and modules.

## How it works

Text is split into overlapping chunks, embedded with Gemini, kept in an in-memory FAISS index, and retrieved for each question. Gemini receives only the retrieved excerpts with a grounded prompt and citation numbers. This is a learning project; inspect retrieved sources when an answer looks wrong.

## Test evidence

See [`tests.md`](tests.md). Results are a test plan/template and have not been executed against a Gemini key; replace the observed result and status after running each question in the app.

## Builder reflection

**Why does the bot sometimes miss a fact even when it is present in the knowledge base?**
A search system retrieves a limited number of text chunks. If the wording differs, a useful passage is split across chunks, or the selected chunks rank poorly, the model may never see the fact. The Sources panel helps identify this retrieval issue.

**What change would you try first if sources are right but the answer is wrong?**
I would make the instructions more explicit and ensure the model cites each claim from the supplied excerpts. Then I would rerun the same question and check whether the grounded answer improves.
