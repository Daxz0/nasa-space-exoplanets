import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Methods - Exoura",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------ GLOBAL STYLES ------------------
st.markdown("""
<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Urbanist:wght@500;700;900&family=Azeret+Mono:wght@500;700&display=swap" rel="stylesheet">

<style>
/* Hide Streamlit chrome */
#MainMenu, header, footer {visibility: hidden;}
[data-testid="stSidebar"], section[data-testid="stSidebarNav"], div[aria-label^="App pages"] { display: none !important; }

/* Core layout */
.block-container { padding-top: 0 !important; }
.stApp { background: #050510 !important; color: #e5e7eb; font-family: 'DM Sans', sans-serif; }

/* ===== HEADER ===== */
.site-header {
  position: sticky; top: 0; z-index: 999;
  background: rgba(5,5,16,0.92);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid rgba(255,255,255,0.08);
  padding: .75rem 2rem;
  display: flex; justify-content: space-between; align-items: center;
}
.brand-name {
  font-family: 'Urbanist', sans-serif;
  font-weight: 900; font-size: 1.8rem; color: #fff;
  letter-spacing: -0.02em;
}

.nav { display: flex; gap: 1rem; }
.nav .stButton>button {
  background: transparent; border: 1px solid rgba(255,255,255,.15);
  padding: .5rem 1rem; border-radius: 10px;
  color: #fff; font-weight: 600; transition: all .2s ease;
}
.nav .stButton>button:hover { background: rgba(255,255,255,.12); }
.nav .stButton>button:focus { outline: 2px solid #3b82f6; }

/* Content wrap for sections */
.main-wrap { max-width: 1200px; margin: 1.2rem auto 2rem auto; padding: 0 1rem; }
.lead { font-size: 1.05rem; opacity: .92; }
.callout { padding: .75rem 1rem; border: 1px solid rgba(255,255,255,0.12); border-radius: 12px; background: rgba(255,255,255,0.04); }
</style>
""", unsafe_allow_html=True)

# Unified blue button theme across the app (overrides theme)
st.markdown(
        """
<style>
.stButton > button {
    background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%) !important;
    color: #fff !important;
    border-radius: 8px !important;
    border: none !important;
    font-weight: 700 !important;
    box-shadow: 0 2px 8px rgba(30,60,114,0.2) !important;
    padding: 0.6rem 1.1rem !important;
    min-height: 44px !important;
    line-height: 1.2 !important;
    font-size: 0.95rem !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    white-space: nowrap !important;
}
.stButton > button:hover { transform: translateY(-1px) !important; box-shadow: 0 4px 12px rgba(30,60,114,0.3) !important; }
.nav .stButton>button {
    background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%) !important;
    color: #fff !important;
    border-radius: 8px !important;
    border: none !important;
    font-weight: 700 !important;
    box-shadow: 0 2px 8px rgba(30,60,114,0.2) !important;
    padding: 0.6rem 1.1rem !important;
    min-height: 44px !important;
    min-width: 120px !important;
    line-height: 1.2 !important;
    font-size: 0.95rem !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    white-space: nowrap !important;
}
.nav .stButton>button:hover { transform: translateY(-1px) !important; box-shadow: 0 4px 12px rgba(30,60,114,0.3) !important; }
</style>
""",
        unsafe_allow_html=True,
)

# ------------------ HEADER ------------------
with st.container():
    st.markdown('<div class="site-header">', unsafe_allow_html=True)
    left, right = st.columns([2,4], vertical_alignment="center")

    with left:
        st.markdown('<h1 class="brand-name">Exoura</h1>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="nav">', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        if c1.button("Home", use_container_width=True):
            st.switch_page("home.py")
        if c2.button("Education", use_container_width=True):
            st.switch_page("pages/education.py")
        if c3.button("Demo", use_container_width=True):
            st.switch_page("pages/demo.py")
        if c4.button("Game", use_container_width=True):
            st.switch_page("pages/game.py")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ MAIN CONTENT ------------------
st.markdown('<div class="main-wrap">', unsafe_allow_html=True)

st.markdown("# Methods")
st.markdown(
    "<p class='lead'>Learn about the machine learning methods and algorithms used in Exoura to detect exoplanets from light curve data.</p>",
    unsafe_allow_html=True
)

st.markdown("## Random Forest Model")
st.markdown(
    "Our primary classification model uses a Random Forest algorithm trained on NASA's Kepler and TESS exoplanet datasets. "
    "The model analyzes key features from transit light curves to distinguish between genuine planetary signals and false positives."
)

st.markdown("### Key Features Used:")
st.markdown("""
- **Orbital Period**: Time taken for one complete orbit around the star
- **Transit Duration**: Duration of the transit event in hours  
- **Transit Depth**: Depth of the transit in parts per million (ppm)
- **Planet Radius**: Radius of the planet in Earth radii
""")

st.markdown("### Model Performance")
st.markdown(
    "The Random Forest model achieves high accuracy in distinguishing between confirmed exoplanets and false positive detections, "
    "helping astronomers prioritize which candidates deserve further investigation."
)

st.markdown(
    "<div class='callout'>Try out the model yourself on the <strong>Demo</strong> page by inputting different parameter values!</div>",
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
