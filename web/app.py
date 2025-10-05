import streamlit as st
from pathlib import Path

# ------------------ PAGE / THEME ------------------
st.set_page_config(page_title="ExoVet", page_icon="🪐", layout="wide", initial_sidebar_state="collapsed")

# Hide default Streamlit header/footer/hamburger
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bitcount+Prop+Double+Ink&display=swap');
/* Hide Streamlit chrome */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Hide multipage sidebar (Streamlit "Pages" list) so only the top nav is available */
/* Use several selectors for cross-version compatibility */
[data-testid="stSidebarNav"]{ display: none !important; }
div[aria-label^="App pages"]{ display: none !important; }
section[aria-label^="Pages"]{ display: none !important; }
[data-testid="stSidebar"] { width: 0 !important; min-width: 0 !important; }

.block-container {padding-top: 0rem; padding-bottom: 2rem;}

/* ===== Sticky Header ===== */
.site-header{
  position: sticky; top: 0; z-index: 999;
  background: rgba(255,255,255,0.92);
  backdrop-filter: blur(6px);
  border-bottom: 1px solid #eaeaea;
  padding: .6rem 0 .6rem 0;
}
@media (prefers-color-scheme: dark){
  .site-header{ background: rgba(13,17,23,0.75); border-bottom: 1px solid rgba(255,255,255,0.08); }
}

/* Topbar layout */
.topbar{ display:flex; align-items:center; justify-content:space-between; gap:16px; }

/* Brand: logo + name */
.brand{ display:flex; align-items:center; gap:12px; }
.brand-logo{
    height:64px;                   /* logo size */
    transform: translateY(4px);    /* nudge slightly down without affecting other layout */
}
.brand-name{
    font-family: 'Bitcount Prop Double Ink', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
    font-weight:900;
    font-size:1.8rem;              /* bigger brand text */
    letter-spacing:.2px;
    line-height:1;
    margin:0;
}

/* Nav: evenly spaced buttons */
.nav{
  display:grid;
  grid-auto-flow:column;
  grid-auto-columns:1fr;         /* each item same width */
  gap:12px;
  min-width:420px;               /* make room so they spread nicely */
}
.nav .stButton>button{
  width:100%;
  border:1px solid rgba(127,127,127,.25);
  background:transparent;
  padding:.5rem 1rem;
  border-radius:10px;
  font-weight:600;
}
.nav .stButton>button:hover{ background:rgba(127,127,127,.12); }
.nav .stButton>button:focus{ outline:2px solid rgba(99,102,241,.45); }

/* Content width */
.main-wrap{ max-width:1200px; margin:0 auto; }
</style>
""", unsafe_allow_html=True)

# ------------------ STATE / ROUTER ------------------
PAGES = ["Home", "Education", "Play", "Results"]
if "page" not in st.session_state:
    st.session_state.page = "Home"

def goto(page: str):
    st.session_state.page = page

# ------------------ HEADER (LOGO + NAV) ------------------
# Locate logo relative to this file so paths work regardless of cwd
logo_path = Path(__file__).parent / "logo.png"
logo_url_override = ""  # or put a URL string here

with st.container():
    st.markdown('<div class="site-header"><div class="topbar">', unsafe_allow_html=True)

    # ---- Brand (left) ----
    left_col, right_col = st.columns([7,9], vertical_alignment="center")
    with left_col:
        cols = st.columns([1,8], vertical_alignment="center")
        with cols[0]:
            # Prefer URL override; otherwise show local logo via st.image so Streamlit serves it correctly
            try:
                if logo_url_override:
                    st.image(logo_url_override, width=80)
                elif logo_path.exists():
                    st.image(str(logo_path.resolve()), width=80)
                else:
                    st.markdown('<div class="brand-logo">🪐</div>', unsafe_allow_html=True)
            except Exception:
                st.markdown('<div class="brand-logo">🪐</div>', unsafe_allow_html=True)
        with cols[1]:
            st.markdown('<div class="brand"><h1 class="brand-name">Exoura</h1></div>', unsafe_allow_html=True)

    # ---- Nav (right) ----
    with right_col:
        st.markdown('<div class="nav">', unsafe_allow_html=True)
        nav_cols = st.columns(4, vertical_alignment="center")
        for i, name in enumerate(["Home", "Education", "Play", "Results"]):
            if nav_cols[i].button(name, use_container_width=True, key=f"nav_{name}"):
                st.session_state.page = name
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

# ------------------ PAGES ------------------
def page_home():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="kicker">NASA Space Apps 2025</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero">A World Away: Hunting for Exoplanets with AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub">Learn the transit method, see how our AI vets signals, then race it in a fast classification game.</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Quick Links")
    # Use equal-width columns and full-width buttons so modules look balanced
    q1, q2, q3 = st.columns([1, 1, 1], gap="large")
    with q1:
        st.markdown("<div style='padding:10px; border-radius:8px; border:1px solid rgba(0,0,0,0.06);'>", unsafe_allow_html=True)
        if st.button("📘 Education", key="home_education"):
            goto("Education")
        st.markdown("</div>", unsafe_allow_html=True)
    with q2:
        st.markdown("<div style='padding:10px; border-radius:8px; border:1px solid rgba(0,0,0,0.06);'>", unsafe_allow_html=True)
        if st.button("🎮 Play", key="home_play"):
            goto("Play")
        st.markdown("</div>", unsafe_allow_html=True)
    with q3:
        st.markdown("<div style='padding:10px; border-radius:8px; border:1px solid rgba(0,0,0,0.06);'>", unsafe_allow_html=True)
        if st.button("📊 Results", key="home_results"):
            goto("Results")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### What’s inside")
    st.write(
        "- **Education:** Exoplanets & transit photometry, false positives (SS/NT/CO/EC), and how features map physics → AI.\n"
        "- **Play:** Decide **Planet** vs **False Positive**; compare **your reaction time** with **AI inference**.\n"
        "- **Results:** Accuracy, precision/recall/F1, confusion matrix, and timing stats."
    )

def page_education():
    st.markdown("## 📘 Education")
    st.caption("Concepts first—so you can understand the science and then beat the AI.")
    # === Placeholder: swap with your two-tab education content ===
    tab1, tab2 = st.tabs(["Exoplanets 101", "From Data → AI Vetting"])
    with tab1:
        st.write("• What is a transit? • Depth/Period/Duration • False positives (SS/NT/CO/EC) • Phase folding.")
        st.info("Drop your toy light curve + odd/even demo here.")
    with tab2:
        st.write("• Our features (depth, SNR, odd-even, duration, period, impact, Teff, R★)")
        st.info("Add the threshold demo + a short model pipeline explainer here.")

def page_play():
    st.markdown("## 🎮 Play")
    st.caption("Classify signals as Planet or False Positive—your time vs the AI.")
    # === Placeholder: insert your game (signal card + timing) here ===
    st.warning("Game UI placeholder. Hook in your model + round loop.")

def page_results():
    st.markdown("## 📊 Results")
    st.caption("Your accuracy and timing compared to the AI.")
    # === Placeholder: show session metrics & confusion matrix here ===
    st.info("Results page placeholder. Show Accuracy / Precision / Recall / F1, confusion matrix, and avg times.")

# Router
if st.session_state.page == "Home":
    page_home()
elif st.session_state.page == "Education":
    page_education()
elif st.session_state.page == "Play":
    page_play()
elif st.session_state.page == "Results":
    page_results()

st.markdown('</div>', unsafe_allow_html=True)  # end main-wrap
