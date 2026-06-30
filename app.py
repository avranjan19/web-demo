import os
import glob
import time
from pathlib import Path

import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

CORPUS_DIR = Path(__file__).parent / "corpus"
MAX_CORPUS_CHARS = 32000
LANDING_PAGE_URL = "https://fincompli.in"  # update to your live GoHighLevel page

st.set_page_config(page_title="FinCompliOS — Regulatory Q&A", layout="centered")

SYSTEM_PROMPT = """You are a compliance assistant for Indian banks and NBFCs.
Answer ONLY using the regulatory documents provided in the context below.

Rules:
1. Be precise and direct.
2. Cite every fact with the source document name in this format: [Source: filename]
3. If the answer is not in the provided context, say exactly:
   "This isn't covered in the indexed regulations for this demo. The production
   system indexes the full RBI, SEBI, IRDAI, and CERT-In corpus."
4. Never speculate beyond what the documents state.
5. Use plain English — the reader is a compliance officer, not a lawyer.
6. State specific deadlines, thresholds, and penalties explicitly when present."""

SUGGESTED_QUESTIONS = [
    "What is the maximum time we have to notify CERT-In of a cybersecurity breach?",
    "Does RBI require payment transaction data to be stored in India?",
    "What does the DPDP Act say about transferring customer data outside India?",
    "What IT security controls does RBI require for internet banking?",
    "What is RBI's requirement for audit log retention in core banking systems?",
]


@st.cache_resource(show_spinner=False)
def load_corpus() -> str:
    files = sorted(glob.glob(str(CORPUS_DIR / "*.md")))
    if not files:
        return ""
    per_file_limit = MAX_CORPUS_CHARS // len(files)
    parts = [open(p, encoding="utf-8").read()[:per_file_limit] for p in files]
    return "\n\n".join(parts)


@st.cache_resource(show_spinner=False)
def get_client() -> Groq:
    api_key = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
    if not api_key:
        st.error("GROQ_API_KEY is not set. Add it to .env locally or to Streamlit Cloud secrets.")
        st.stop()
    return Groq(api_key=api_key)


def ask(question: str, corpus: str, client: Groq) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1024,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Regulatory documents:\n{corpus}\n\nQuestion: {question}"},
        ],
    )
    return response.choices[0].message.content


# ---- UI ----

st.title("FinCompliOS")
st.caption("Real-time regulatory intelligence for Indian banks and NBFCs — live demo")

corpus = load_corpus()
if not corpus:
    st.warning(
        "No regulatory corpus found. Run `python scripts/build_corpus.py` first "
        "to scrape the demo documents via Apify."
    )
    st.stop()

client = get_client()

with st.sidebar:
    st.subheader("Try asking")
    for q in SUGGESTED_QUESTIONS:
        if st.button(q, use_container_width=True, key=q):
            st.session_state.pending_question = q
    st.divider()
    st.caption(
        "This demo covers 5 indexed regulations (RBI IT framework, CERT-In 2025, "
        "DPDP Act, RBI data localization, RBI cloud framework) for illustration. "
        "The production platform covers the full regulatory corpus and connects "
        "to your bank's live compliance event stream."
    )
    st.link_button("Request a pilot", LANDING_PAGE_URL, use_container_width=True)

if "history" not in st.session_state:
    st.session_state.history = []
if "pending_question" not in st.session_state:
    st.session_state.pending_question = None

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.session_state.pending_question or st.chat_input(
    "Ask a question about RBI, CERT-In, SEBI, or DPDP compliance..."
)
st.session_state.pending_question = None

if question:
    st.session_state.history.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching the regulatory corpus..."):
            start = time.time()
            answer = ask(question, corpus, client)
            elapsed = time.time() - start
        st.markdown(answer)
        st.caption(f"Answered in {elapsed:.1f}s")

    st.session_state.history.append({"role": "assistant", "content": answer})

st.divider()
st.caption(
    "FinCompliOS is in early access. Built by a senior fintech engineer with "
    f"15 years in banking infrastructure. [Request access for your bank or NBFC]({LANDING_PAGE_URL})."
)
