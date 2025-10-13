import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.providers.google_gla import GoogleGLAProvider

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_KEY")

# Initialize model
model = GeminiModel(
    "gemini-2.5-flash",
    provider=GoogleGLAProvider(api_key=api_key)
)

# Define input type
class InputType(BaseModel):
    question: str
    words: int


def count_words(text):
    return len(text.split())


# Base system prompt (unchanged)
BASE_PROMPT = (
    "You are an expert UPSC Mains aspirant trained in analytical answer writing. "
    "For every question provided, write a structured, high-quality UPSC-style answer "
    "with the following format and guidelines:\n\n"

    "1️⃣ Introduction:\n"
    "- Maximum 2 lines only.\n"
    "- Must include a definition, data, background information, or current affairs reference.\n\n"

    "2️⃣ Body:\n"
    "- Divide the answer into subheadings derived logically from the question itself.\n"
    "- Each subheading should cover a unique dimension of the topic such as causes, effects, challenges, opportunities, limitations, strengths, way forward, etc.\n"
    "- Each subheading must contain *at least 4 succinct bullet points* explaining the concept clearly.\n"
    "- Use diverse perspectives (historical, economic, political, social, environmental, ethical, administrative, technological, etc.) wherever relevant.\n"
    "- Incorporate data, examples, and references from authentic sources such as NITI Aayog reports, Economic Survey, PIB, government committees "
    "(e.g., Kasturirangan, Punchhi, Sarkaria), scholars, thinkers, and newspapers like The Hindu or Indian Express.\n"
    "- Use crisp and exam-oriented language suitable for UPSC Mains answers.\n\n"

    "3️⃣ Conclusion:\n"
    "- Maximum 2 lines only.\n"
    "- Should have a tone of optimism and vision.\n"
    "- May include: a quote by an expert, reference to a government committee, SDG goal, government policy, or reform recommendation to enrich the answer.\n\n"

    "🧠 Additional Instructions:\n"
    "- The total answer must be more than {words} words.\n"
    "- Maintain a balanced and objective tone.\n"
    "- Avoid repetition and verbosity.\n"
    "- Use short, impactful sentences suitable for exam writing. without use of * or any symbols\n"
    "- Tailor the structure to reflect UPSC Mains best practices for GS and optional papers.\n\n"
    "Now, write a complete answer to the following UPSC question:\n"
    "❓ {question}\n"
)

# Streamlit configuration
icon_path = os.path.join(os.path.dirname(__file__), "/Users/laleet/Documents/agent/logo.png")

st.set_page_config(page_title="UPSC Answer Generator", page_icon=icon_path, layout="wide")
# Custom CSS for footer at bottom
st.markdown("""
    <style>
    /* General page layout fix */
    .stApp {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }

    /* Main content expands */
    .block-container {
        flex: 1 0 auto;
    }

    /* Footer always at bottom */
    footer {
        visibility: hidden;
    }
    .custom-footer {
        visibility: visible;
        position: relative;
        bottom: 0;
        left: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        background-color: #f5f5f5;
        border-top: 1px solid #ddd;
        color: #555;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🎯 𝚄𝙿𝚂𝙲 Mains Answer Generator")
st.markdown("Generate structured, high-quality UPSC Mains-style answers using Gemini.")

# Sidebar inputs
st.sidebar.header("Enter Question Details")
question = st.sidebar.text_area("Enter your UPSC Question:", height=150)
words = st.sidebar.number_input("Word Limit (e.g., 400)", min_value=100, max_value=800, step=50, value=400)

generate_button = st.sidebar.button("✨ Generate Answer")

# Generate answer
if generate_button:
    if not api_key:
        st.error("❌ API key not found! Please set GEMINI_KEY in your .env file.")
    elif not question.strip():
        st.warning("⚠️ Please enter a UPSC question.")
    else:
        with st.spinner("Generating structured UPSC answer..."):
            system_prompt = BASE_PROMPT.format(question=question, words=words)
            agent = Agent(
                model,
                deps_type=InputType,
                output_type=str,
                system_prompt=system_prompt
            )

            result = agent.run_sync(question, deps=InputType(question=question, words=words))
            answer_text = result.output.strip()
            total_words = count_words(answer_text)

            st.success(f"✅ Answer generated successfully! ({total_words} words)")
            st.markdown("###Generated UPSC Answer")
            st.markdown(f"**Question:** {question}")
            st.write(answer_text)

            # Download button
            st.download_button(
                label="⬇️ Download Answer as Text File",
                data=answer_text,
                file_name=f"UPSC_Answer_{words}words.txt",
                mime="text/plain"
            )

# Custom footer (always at bottom)
st.markdown("""
    <div class="custom-footer">
        Built with ❤️ using Streamlit and Gemini 2.5 Flash | © 2025 UPSC AI Answer Assistant
    </div>
""", unsafe_allow_html=True)