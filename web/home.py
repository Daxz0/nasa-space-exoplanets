# app.py (use as web/home.py if you're running from /web)
import streamlit as st
from pathlib import Path

# ------------------ PAGE / THEME ------------------
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
<link href="https://fonts.googleapis.com/css2?family=Azeret+Mono:wght@400..900&family=Space+Grotesk:wght@400;600;700&family=Fraunces:opsz,wght@9..144,600;9..144,800&display=swap" rel="stylesheet">

<style>
/* Hide Streamlit chrome */
#MainMenu, footer, header {visibility: hidden;}
/* Hide default multipage sidebar/pages list */
[data-testid="stSidebarNav"],
div[aria-label^="App pages"],
section[aria-label^="Pages"] { display: none !important; }
[data-testid="stSidebar"] { width: 0 !important; min-width: 0 !important; }

/* App container spacing */
.block-container { padding-top: 0rem; padding-bottom: 2rem; }

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
.brand { display:flex; align-items:center; gap:12px; }
.brand-logo{
  height: 64px;                 /* logo size */
  transform: translateY(-2px);  /* nudge up to align baseline with text */
}
.brand-name{
  font-family: 'Space Grotesk', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
  font-weight: 800;
  font-size: 1.9rem;            /* bigger brand wordmark */
  letter-spacing: .2px;
  line-height: 1;
  margin: 0;
}

/* Nav: evenly spaced buttons on the right */
.nav{
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 1fr;   /* equal widths */
  gap: 12px;
  min-width: 480px;
}
.nav .stButton>button{
  width: 100%;
  border: 1px solid rgba(127,127,127,.25);
  background: transparent;
  padding: .5rem 1rem;
  border-radius: 10px;
  font-weight: 600;
}
.nav .stButton>button:hover{ background: rgba(127,127,127,.12); }
.nav .stButton>button:focus{ outline: 2px solid rgba(99,102,241,.45); }

/* Shared content width */
.main-wrap{ max-width: 1200px; margin: 0 auto; }

/* Code font (optional) */
[data-testid="stCodeBlock"], pre, code {
  font-family: 'Azeret Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace !important;
  font-weight: 700;
}

/* ===== HERO (big center section) ===== */
.hero-wrap{
  /* fill most of the viewport and center contents */
  min-height: calc(100vh - 120px);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 4rem 0;
  text-align: center;
  background: linear-gradient(180deg, rgba(255,246,226,0.0) 0%, rgba(255,246,226,0.10) 100%);
}
@media (prefers-color-scheme: dark){
  .hero-wrap{ background: linear-gradient(180deg, rgba(245,245,245,0.0) 0%, rgba(245,245,245,0.06) 100%); }
}
.hero-title{
  font-family: 'Fraunces', ui-serif, Georgia, 'Times New Roman', serif !important;
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.03;
  margin: 0 auto .9rem auto;
  max-width: 16ch;
  font-size: clamp(2.4rem, 6vw + .5rem, 6rem);
}
.hero-sub{
  font-family: 'Space Grotesk', system-ui, -apple-system, Segoe UI, Roboto, 'Helvetica Neue', Arial, sans-serif;
  font-size: clamp(1.00rem, 1.2vw + .6rem, 1.3rem);
  line-height: 1.6;
  opacity: .92;
  margin: 0 auto 1.6rem auto;
  max-width: 900px;
}
.hero-ctas{ display: inline-flex; gap: 16px; align-items: center; justify-content: center; }
.btn-ghost{
  border: 1px solid rgba(127,127,127,.28);
  background: rgba(255,255,255,0.0);
  color: inherit;
  padding: .8rem 1.15rem;
  border-radius: 12px;
  font-weight: 700;
}
.btn-ghost:hover{ background: rgba(127,127,127,.12); }
.section-tight { margin-top: .5rem; }
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER (LOGO + NAV) ------------------
logo_path = Path(__file__).parent / "logo.png"  # put your file here
logo_url_override = ""                           # or set to a URL string

with st.container():
    st.markdown('<div class="site-header"><div class="topbar">', unsafe_allow_html=True)

    left_col, right_col = st.columns([7,9], vertical_alignment="center")

    # ---- Brand (left) ----
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

    # ---- Nav (right) ----
    with right_col:
        st.markdown('<div class="nav">', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4, vertical_alignment="center")
        # Use Streamlit's multipage router
        if c1.button("Home", use_container_width=True):
            st.switch_page("home.py")                # this file
        if c2.button("Education", use_container_width=True):
            st.switch_page("pages/education.py")
        if c3.button("Demo", use_container_width=True):
            st.switch_page("pages/demo.py")          # rename to play.py if you prefer
        if c4.button("Results", use_container_width=True):
            st.switch_page("pages/results.py")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

st.markdown('<div class="main-wrap">', unsafe_allow_html=True)

# ------------------ HOME CONTENT ------------------
# Big hero with video CTA
st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
st.markdown('<h1 class="hero-title">Find the worlds between dips</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="hero-sub">Learn about exoplanet detection through transit photometry and go against an AI to try detecting a few yourself!</p>',
    unsafe_allow_html=True
)

center = st.container()
with center:
    colL, colC, colR = st.columns([1,2,1])
    with colC:
        watch = st.button("▶  Watch our 30 second demo", key="watch_demo", help="Opens the demo video below")
st.markdown("</div>", unsafe_allow_html=True)  # end hero

if "show_demo" not in st.session_state:
    st.session_state.show_demo = False
if watch:
    st.session_state.show_demo = True

if st.session_state.show_demo:
    # Replace with your real 30s demo URL or a local mp4
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    # st.video(str(Path(__file__).parent / "assets" / "demo.mp4"))

st.markdown("---")
st.markdown('<div class="section-tight">', unsafe_allow_html=True)
st.markdown("#### What’s inside")
# Handy deep links (work even without the top nav)
st.page_link("pages/education.py", label="📘 Education")
st.page_link("pages/demo.py",      label="🎮 Demo")
st.page_link("pages/results.py",   label="📊 Results")

st.write(
    "- **Education:** Exoplanets & transit photometry, false positives (SS/NT/CO/EC), and how features map physics → AI.\n"
    "- **Play:** Decide **Planet** vs **False Positive**; compare **your reaction time** with **AI inference**.\n"
    "- **Results:** Accuracy, precision/recall/F1, confusion matrix, and timing stats."
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # end main-wrap
