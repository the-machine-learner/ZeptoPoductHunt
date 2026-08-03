"""
Zepto Product Hunt Week – Main Streamlit Application Entrypoint.

Modularized Architecture:
- src.database: Products Catalogue & Persona Profiles
- src.backend: Groq LLM API Client & Shared Backend Initialization Pipeline
- src.frontend: React 18 Mobile Frame UI Component
"""

import streamlit as st
import json

from src.database.personas import PERSONAS
from src.database.products import PRODUCTS_MASTER
from src.backend.groq_client import generate_ai_clue, get_groq_api_key
from src.backend.session_pipeline import init_backend_session, advance_gameplay_stage
from src.frontend.react_app import render_react_mobile_app

# Page Configuration & Styling
st.set_page_config(
    page_title="Zepto Product Hunt - AI-Enabled MVP",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    header[data-testid="stHeader"] {
        display: none !important;
    }
    [data-testid="stAppViewContainer"] {
        padding: 0 !important;
        background-color: #0f172a !important;
        overflow: hidden !important;
    }
    .main .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
        margin-top: 0 !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }
    div[data-testid="stCustomComponentV1"], .element-container {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
    }
    iframe {
        display: block !important;
        margin: 0 auto !important;
        border: none !important;
    }
    /* Fix Sidebar Dropdown & Label Left Padding */
    div[data-testid="stSidebar"] div[data-baseweb="select"] > div {
        padding-left: 10px !important;
        padding-right: 10px !important;
        border-radius: 8px !important;
    }
    div[data-testid="stSidebar"] div[data-baseweb="select"] [data-testid="stMarkdownContainer"] p {
        font-size: 0.86rem !important;
        font-weight: 600 !important;
    }
    div[data-testid="stSidebar"] label p {
        font-size: 0.85rem !important;
        font-weight: 700 !important;
        margin-bottom: 4px !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# STREAMLIT SESSION STATE INITIALIZATION
# ---------------------------------------------------------
if "session_data" not in st.session_state:
    st.session_state.session_data = init_backend_session('arjun', 'flow1_tutorial')
if "demo_mode" not in st.session_state:
    st.session_state.demo_mode = "tour"
if "demo_key" not in st.session_state:
    st.session_state.demo_key = 0

# ---------------------------------------------------------
# SIDEBAR CONTROLS & PERSONA SELECTOR
# ---------------------------------------------------------
st.sidebar.title("🎯 Zepto Product Hunt")
st.sidebar.markdown("**AI-Enabled Category Discovery MVP**")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🚪 Select Entry Flow")

flow_choice = st.sidebar.radio(
    "Choose Flow:",
    ["Flow 1: Guided Tutorial (Demo Profile)", "Flow 2: Persona Explorer"],
    index=0 if st.session_state.session_data['entry_flow'] == 'flow1_tutorial' else 1
)

if flow_choice.startswith("Flow 1"):
    st.sidebar.info("🎓 **Flow 1: Guided Tutorial** uses default persona **Arjun Patel** to provide a consistent 11-step walkthrough for judges.")
    if st.sidebar.button("▶ Start Guided Tutorial", use_container_width=True, type="primary"):
        with st.spinner("⚡ AI Initializing Product Hunt Session for Arjun..."):
            st.session_state.session_data = init_backend_session('arjun', 'flow1_tutorial')
            st.session_state.demo_mode = "tour"
            st.session_state.demo_key += 1
            st.rerun()

else:
    st.sidebar.markdown("### 👤 Flow 2: Profile Selection")
    persona_options = {
        'arjun': "🎮 Arjun Patel (Gaming & Tech)",
        'ananya': "💄 Ananya Sharma (Beauty & Skincare)",
        'rohan': "🍕 Rohan Verma (Late-Night Munchies)",
        'priya': "🧺 Priya & Vikram (Household & Family)"
    }
    
    selected_p_key = st.sidebar.selectbox(
        "Select Persona Profile:",
        options=list(persona_options.keys()),
        format_func=lambda x: persona_options[x],
        index=list(persona_options.keys()).index(st.session_state.session_data['persona_key'])
    )
    
    p_info = PERSONAS[selected_p_key]
    st.sidebar.markdown(f"**Past Buys**: {', '.join(p_info['purchase_history'])}")
    st.sidebar.markdown(f"**AI Tone**: {p_info['tone']}")
    st.sidebar.markdown(f"**Suggested categories**: {', '.join(p_info['suggested_categories'])}")

    if st.sidebar.button("🚀 Launch Profile Hunt (AI)", use_container_width=True, type="primary"):
        with st.spinner(f"⚡ AI Crafting personalized clue for {p_info['name']}..."):
            st.session_state.session_data = init_backend_session(selected_p_key, 'flow2_profile')
            st.session_state.demo_mode = "normal"
            st.session_state.demo_key += 1
            st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔄 Continuous AI Gameplay Loop")
st.sidebar.caption("Simulate purchases to trigger progressive AI clue generation:")

curr_stage = st.session_state.session_data['hunt_stage']

if curr_stage == 1:
    if st.sidebar.button("🛒 Complete Purchase #1 (Unlock Clue 2)", use_container_width=True):
        with st.spinner("⚡ AI Generating Clue 2 (Simpler Hint)..."):
            st.session_state.session_data = advance_gameplay_stage(st.session_state.session_data, 2)
            st.session_state.demo_key += 1
            st.rerun()

elif curr_stage == 2:
    if st.sidebar.button("🛒 Complete Purchase #2 (Unlock Clue 3)", use_container_width=True):
        with st.spinner("⚡ AI Generating Clue 3 (Direct Actionable Clue)..."):
            st.session_state.session_data = advance_gameplay_stage(st.session_state.session_data, 3)
            st.session_state.demo_key += 1
            st.rerun()

else:
    st.sidebar.success("🎉 All 3 Hunt Stages Completed!")
    if st.sidebar.button("🔄 Reset Hunt Session", use_container_width=True):
        st.session_state.session_data = init_backend_session(st.session_state.session_data['persona_key'], st.session_state.session_data['entry_flow'])
        st.session_state.demo_key += 1
        st.rerun()

# ---------------------------------------------------------
# AI INSPECTOR & METADATA PANEL
# ---------------------------------------------------------
st.sidebar.markdown("---")
with st.sidebar.expander("⚡ Groq AI Live Inspector", expanded=False):
    latest_clue = st.session_state.session_data['clues'].get(curr_stage, {})
    st.markdown(f"**Model**: `{latest_clue.get('model', 'llama-3.3-70b-versatile')}`")
    st.markdown(f"**Latency**: `{latest_clue.get('latency_ms', 0)} ms`")
    st.markdown(f"**Active Stage**: Clue #{curr_stage} of 3")
    st.markdown(f"**Target Item**: `{st.session_state.session_data['target_prod']['name']}`")
    st.json(latest_clue)

# Prepare Payload for React App
s_data = st.session_state.session_data
curr_clue = s_data['clues'].get(s_data['hunt_stage'], {})

# Catalogue for persona
catalog_prods = [PRODUCTS_MASTER[pid] for pid in s_data['persona']['catalog_ids']]

react_session_payload = {
    'persona': s_data['persona'],
    'entry_flow': s_data['entry_flow'],
    'hunt_stage': s_data['hunt_stage'],
    'purchase_history': s_data['purchase_history'],
    'target_prod': s_data['target_prod'],
    'clue': curr_clue,
    'clues_history': s_data['clues'],
    'products': catalog_prods,
    'groq_api_key': get_groq_api_key()
}

# Render React Mobile UI Application
render_react_mobile_app(react_session_payload, st.session_state.demo_mode)
