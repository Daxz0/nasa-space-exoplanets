# app.py (or web/home.py)
import streamlit as st
from pathlib import Path

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Exoura",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------ GLOBAL STYLES ------------------
st.markdown("""
<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bitcount+Prop+Double+Ink:wght@100..900&family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&family=Urbanist:ital,wght@0,100..900;1,100..900&family=Azeret+Mono:wght@400..900&display=swap" rel="stylesheet">

<style>
/* Hide Streamlit UI */
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stSidebarNav"],
div[aria-label^="App pages"],
section[aria-label^="Pages"] { display: none !important; }
[data-testid="stSidebar"] { width: 0 !important; min-width: 0 !important; }

.block-container { padding-top: 0rem; padding-bottom: 2rem; }

/* Header */
.site-header{
  position: sticky; top: 0; z-index: 999;
  background: rgba(255,255,255,0.92);
  backdrop-filter: blur(6px);
  border-bottom: 1px solid #eaeaea;
  padding: .6rem 1rem;
}
@media (prefers-color-scheme: dark){
  .site-header{
    background: rgba(13,17,23,0.75);
    border-bottom: 1px solid rgba(255,255,255,0.08);
  }
}

/* Layout */
.topbar{ display:flex; align-items:center; justify-content:space-between; gap:16px; }
.main-wrap{ max-width: 1200px; margin: 0 auto; }

/* Brand */
.brand { display:flex; align-items:center; gap:12px; }
.brand-logo{ height: 64px; transform: translateY(-2px); }
.brand-name{
  font-family: 'Bitcount Prop Double Ink', 'DM Sans', sans-serif;
  font-weight: 800;
  font-size: 2.2rem;
  margin: 0;
}

/* Nav buttons */
.nav{
  display: grid; grid-auto-flow: column; grid-auto-columns: 1fr;
  gap: 12px; min-width: 480px;
}
.nav .stButton>button{
  width: 100%;
  border: 1px solid rgba(127,127,127,.25);
  background: transparent;
  padding: .5rem 1rem;
  border-radius: 10px;
  font-family: 'DM Sans', sans-serif;
  font-weight: 600;
}
.nav .stButton>button:hover{ background: rgba(127,127,127,.12); }

/* HERO */
.hero-wrap{
  min-height: 45vh; /* slimmed down hero section */
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  text-align: center;
  background: linear-gradient(180deg, rgba(255,246,226,0.0) 0%, rgba(255,246,226,0.05) 100%);
}
.hero-title{
  font-family: 'Urbanist', sans-serif !important;
  font-weight: 800;
  letter-spacing: -0.02em;
  margin: 0 auto .9rem auto;
  font-size: clamp(2.4rem, 6vw + .5rem, 5rem);
}
.hero-sub{
  font-family: 'DM Sans', sans-serif !important;
  font-size: 1.1rem;
  line-height: 1.5;
  opacity: .9;
  max-width: 900px;
  margin: 0 auto 1.6rem auto;
}

/* Modal Overlay */
.modal-bg {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.75);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2000;
}
.modal-content {
  background: white;
  border-radius: 12px;
  padding: 0;
  max-width: 800px;
  width: 90%;
  overflow: hidden;
  box-shadow: 0 0 40px rgba(0,0,0,0.3);
}
.modal-video-wrapper{ padding: .5rem; background: #0b0b0b; }
.modal-header {
  background: #fff;
  padding: 1rem;
  font-weight: bold;
  text-align: center;
}
.modal-video {
  width: 100%;
  height: 450px;
  border: none;
}
.modal-close {
  position: absolute;
  top: 20px;
  right: 30px;
  font-size: 2rem;
  color: white;
  cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
logo_path = Path(__file__).parent / "logo.png"
logo_url_override = ""

with st.container():
    st.markdown('<div class="site-header"><div class="topbar">', unsafe_allow_html=True)

    left_col, right_col = st.columns([7,9], vertical_alignment="center")

    # Brand
    with left_col:
        cols = st.columns([1,8], vertical_alignment="center")
        with cols[0]:
            if logo_url_override:
                st.markdown(f'<img class="brand-logo" src="{logo_url_override}">', unsafe_allow_html=True)
            elif logo_path.exists():
                st.image(str(logo_path.resolve()), width=80)
            else:
                st.markdown('<div class="brand-logo">🪐</div>', unsafe_allow_html=True)
        with cols[1]:
            st.markdown('<div class="brand"><h1 class="brand-name">Exoura</h1></div>', unsafe_allow_html=True)

    # Navigation
    with right_col:
        st.markdown('<div class="nav">', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        if c1.button("Home", use_container_width=True): st.switch_page("home.py")
        if c2.button("Education", use_container_width=True): st.switch_page("pages/education.py")
        if c3.button("Demo", use_container_width=True): st.switch_page("pages/demo.py")
        if c4.button("Results", use_container_width=True): st.switch_page("pages/results.py")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

# ------------------ HERO SECTION ------------------
st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
st.markdown('<h1 class="hero-title">Find the worlds between dips</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-sub">Learn about exoplanet detection through transit photometry and go against an AI to try detecting a few yourself!</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ------------------ VIDEO BUTTON ------------------
st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)
if st.button("▶ Watch our 30-second demo"):
    st.session_state["show_modal"] = True
st.markdown('</div>', unsafe_allow_html=True)

# ------------------ MODAL POPUP ------------------
if "show_modal" not in st.session_state:
    st.session_state["show_modal"] = False

if st.session_state["show_modal"]:
    st.markdown("""
    <div class="modal-bg" id="modal">
      <a class="modal-close" href="?close_demo=1" aria-label="Close demo">×</a>
      <div class="modal-content">
        <div class="modal-header">Our 30-Second Demo</div>
        <div class="modal-video-wrapper">
          <iframe class="modal-video" src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&rel=0" allowfullscreen></iframe>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
params = st.experimental_get_query_params()
if 'close_demo' in params:
    # user clicked the close link in the overlay; clear state and remove query params
    st.session_state.show_modal = False
    st.experimental_set_query_params()

if st.session_state.show_modal:
    # Use YouTube embed (autoplay). Replace with local mp4 URL if preferred.
    embed_url = "https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1"
    st.markdown(f"""
    <div class="modal-overlay">
      <div class="modal-content">
        <a class="modal-close" href="?close_demo=1" aria-label="Close demo">✕</a>
        <div class="modal-video-wrapper">
          <iframe src="{embed_url}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        </div>
      </div>
    </div>
    <style>
    .modal-overlay{{position:fixed; inset:0; background:rgba(0,0,0,0.6); z-index:9999; display:flex; align-items:center; justify-content:center;}}
    .modal-content{{width:90%; max-width:980px; aspect-ratio:16/9; position:relative; box-shadow:0 12px 40px rgba(0,0,0,0.45);}}
    .modal-content iframe{{width:100%; height:100%; border-radius:8px;}}
    .modal-close{{position:absolute; top:-18px; right:-18px; background:#ffffff; color:#111; text-decoration:none; width:42px; height:42px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:20px; box-shadow:0 6px 18px rgba(0,0,0,0.2); z-index:10000;}}
    @media (max-width:600px){{ .modal-content{{ width:95%; }} .modal-close{{ top:-10px; right:-10px; }} }}
    </style>
    """, unsafe_allow_html=True)

# ------------------ BELOW HERO ------------------
st.markdown("---")
st.markdown("#### What’s inside")
st.page_link("pages/education.py", label="📘 Education")
st.page_link("pages/demo.py", label="🎮 Demo")
st.page_link("pages/results.py", label="📊 Results")

st.write("""
- **Education:** Exoplanets & transit photometry, false positives (SS/NT/CO/EC), and how features map physics → AI.  
- **Play:** Decide **Planet** vs **False Positive**; compare **your reaction time** with **AI inference**.  
- **Results:** Accuracy, precision/recall/F1, confusion matrix, and timing stats.
""")
