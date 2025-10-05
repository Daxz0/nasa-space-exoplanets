# app.py  (put in your web/ or project root)
import streamlit as st
from pathlib import Path

# ------------------ PAGE / THEME ------------------
st.set_page_config(
    page_title="Exoura",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------ GLOBAL STYLES (FONTS + CSS) ------------------
st.markdown("""
<!-- Google Fonts: Bitcount (brand), DM Sans (UI), Urbanist (hero), Azeret Mono (code) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bitcount+Prop+Double+Ink:wght@100..900&family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&family=Urbanist:ital,wght@0,100..900;1,100..900&family=Azeret+Mono:wght@400..900&display=swap" rel="stylesheet">

<style>
:root{
  --header-h: 88px;
}

/* Hide Streamlit chrome & default pages sidebar */
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stSidebarNav"],
div[aria-label^="App pages"],
section[aria-label^="Pages"] { display: none !important; }
[data-testid="stSidebar"] { width: 0 !important; min-width: 0 !important; }

/* Layout container */
.block-container { padding-top: 0 !important; padding-bottom: 2rem; }

/* ===== Sticky Header ===== */
.site-header{
  position: sticky; top: 0; z-index: 999;
  background: rgba(255,255,255,0.92);
  backdrop-filter: blur(6px);
  border-bottom: 1px solid #eaeaea;
  padding: .6rem 0 .6rem 0;
}
@media (prefers-color-scheme: dark){
  .site-header{
    background: rgba(13,17,23,0.75);
    border-bottom: 1px solid rgba(255,255,255,0.08);
  }
}

/* Header row */
.topbar{ display:flex; align-items:center; justify-content:space-between; gap:16px; padding: 0 16px; }

/* Brand (logo + wordmark) */
.brand { display:flex; align-items:center; gap:12px; }
.brand-logo{ height: 64px; transform: translateY(-2px); }
.brand-name{
  font-family: 'Bitcount Prop Double Ink', 'DM Sans', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial !important;
  font-weight: 800; font-size: 2.2rem; letter-spacing: .02em; line-height: 1; margin: 0;
}

/* Top navigation buttons */
.nav{
  display: grid; grid-auto-flow: column; grid-auto-columns: 1fr;
  gap: 12px; min-width: 480px;
}
.nav .stButton>button{
  width: 100%; border: 1px solid rgba(127,127,127,.25); background: transparent;
  padding: .5rem 1rem; border-radius: 10px;
  font-family: 'DM Sans', system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif;
  font-weight: 600;
}
.nav .stButton>button:hover{ background: rgba(127,127,127,.12); }
.nav .stButton>button:focus{ outline: 2px solid rgba(99,102,241,.45); }

/* Code font */
[data-testid="stCodeBlock"], pre, code {
  font-family: 'Azeret Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace !important;
  font-weight: 700;
}

/* Main width wrapper */
.main-wrap{ max-width: 1200px; margin: 0 auto; }

/* ===== HERO (slim, centered) ===== */
.hero-wrap{
  min-height: clamp(300px, 42vh, 560px);            /* slimmer hero */
  display: flex; align-items: center;               /* vertical center */
  justify-content: flex-start;                      /* align to left a bit */
  text-align: left;
  padding: 3rem 1rem 2rem;                          /* reduce vertical padding */
  background: linear-gradient(180deg, rgba(255,246,226,0.00) 0%, rgba(255,246,226,0.06) 100%);
}
@media (prefers-color-scheme: dark){
  .hero-wrap{ background: linear-gradient(180deg, rgba(245,245,245,0.00) 0%, rgba(245,245,245,0.04) 100%); }
}

.hero-inner{ max-width: 760px; }

/* Urbanist for the big headline */
.hero-title{
  font-family: 'Urbanist', system-ui, -apple-system, Segoe UI, Roboto, 'Helvetica Neue', Arial, sans-serif !important;
  font-weight: 800;
  letter-spacing: -0.01em;
  line-height: 1.05;
  margin: 0 0 .6rem 0;
  font-size: clamp(2.1rem, 4.2vw + .4rem, 4.2rem);  /* a bit smaller in slim mode */
}

/* Subhead in DM Sans */
.hero-sub{
  font-family: 'DM Sans', system-ui, -apple-system, Segoe UI, Roboto, 'Helvetica Neue', Arial, sans-serif !important;
  font-size: clamp(.98rem, 1.05vw + .45rem, 1.15rem);
  line-height: 1.6;
  opacity: .92;
  margin: 0;
}

/* CTA container spacing below hero */
.section-tight { margin-top: .75rem; }
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER (LOGO + NAV) ------------------
logo_path = Path(__file__).parent / "logo.png"
logo_url_override = ""  # set to an https URL if you prefer

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

    # Nav
    with right_col:
        st.markdown('<div class="nav">', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4, vertical_alignment="center")
        if c1.button("Home", use_container_width=True):
            st.switch_page("home.py")
        if c2.button("Education", use_container_width=True):
            st.switch_page("pages/education.py")
        if c3.button("Demo", use_container_width=True):
            st.switch_page("pages/demo.py")
        if c4.button("Results", use_container_width=True):
            st.switch_page("pages/results.py")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

# ------------------ MAIN ------------------
st.markdown('<div class="main-wrap">', unsafe_allow_html=True)

# HERO (text only)
st.markdown("""
<div class="hero-wrap">
  <div class="hero-inner">
    <h1 class="hero-title">Find the worlds between dips</h1>
    <p class="hero-sub">
      Learn about exoplanet detection through transit photometry and go against an AI
      to try detecting a few yourself!
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

# CTA: show video on click (YouTube)
if "show_demo" not in st.session_state:
    st.session_state.show_demo = False

# If query param demo_closed is present, clear the demo flag so modal won't reappear
qp = st.experimental_get_query_params()
if 'demo_closed' in qp:
  st.session_state.show_demo = False
  # clear query params to keep URL clean
  try:
    st.experimental_set_query_params()
  except Exception:
    pass

st.markdown('<div class="section-tight">', unsafe_allow_html=True)
colL, colC, colR = st.columns([1,2,1])
with colC:
    if st.button("▶  Watch our 30 second demo", key="watch_demo"):
        st.session_state.show_demo = True
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.show_demo:
    # Show demo in a modal overlay (iframe) that darkens the page behind it.
    demo_embed = "https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&rel=0"
    modal = """
<div id="demo-modal" style="position:fixed;inset:0;display:flex;align-items:center;justify-content:center;z-index:9999;">
  <div id="demo-backdrop" style="position:fixed;inset:0;background:rgba(0,0,0,0.7);backdrop-filter: blur(2px);"></div>
  <div style="position:relative;z-index:10000;max-width:1100px;width:92%;height:66vh;border-radius:12px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,0.6);background:#000;">
    <button id="demo-close" aria-label="Close demo" style="position:absolute;top:10px;right:10px;z-index:10010;background:rgba(255,255,255,0.95);border:0;padding:8px 10px;border-radius:8px;cursor:pointer;font-weight:700;">✕</button>
    <iframe src="{demo_embed}" width="100%" height="100%" frameborder="0" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen style="display:block;"></iframe>
  </div>
</div>
<script>
(function(){
  // prevent body scroll while modal visible
  const prevOverflow = document.body.style.overflow;
  document.body.style.overflow = 'hidden';
  const closeModal = ()=>{
    // navigate to same page with query param so Streamlit can clear session state
    const href = window.location.pathname + '?demo_closed=1';
    window.location.href = href;
  }
  // wire up close handlers
  const btn = document.getElementById('demo-close');
  if(btn) btn.addEventListener('click', closeModal);
  const backdrop = document.getElementById('demo-backdrop');
  if(backdrop) backdrop.addEventListener('click', closeModal);
  // also close on Escape
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') closeModal(); });
})();
</script>
""".replace("{demo_embed}", demo_embed)

    st.markdown(modal, unsafe_allow_html=True)

    # Streamlit-level close (ensures modal won't reappear on rerun)
    if st.button("Close demo"):
        st.session_state.show_demo = False

st.markdown("---")

# Quick links section
st.markdown("#### What’s inside")
st.page_link("pages/education.py", label="📘 Education")
st.page_link("pages/demo.py",      label="🎮 Demo")
st.page_link("pages/results.py",   label="📊 Results")
st.write(
    "- **Education:** Exoplanets & transit photometry, false positives (SS/NT/CO/EC), and how features map physics → AI.\n"
    "- **Play:** Decide **Planet** vs **False Positive**; compare **your reaction time** with **AI inference**.\n"
    "- **Results:** Accuracy, precision/recall/F1, confusion matrix, and timing stats."
)

st.markdown('</div>', unsafe_allow_html=True)  # end .main-wrap