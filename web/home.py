import streamlit as st
from typing import Optional

#python3 -m venv .venv
#source .venv/bin/activate
#python -m pip install --upgrade pip
#pip install streamlit numpy matplotlib

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

/* ===== HERO ===== */
.hero {
  min-height: 80vh; display: flex; align-items: center; justify-content: center;
  text-align: center; padding: 4rem 1rem;
}
.hero-inner { max-width: 900px; }
.hero-title {
  font-family: 'Urbanist', sans-serif;
  font-weight: 900; font-size: clamp(2.5rem, 6vw, 4.5rem);
  background: linear-gradient(90deg, #7aa2ff, #a78bfa);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  margin-bottom: 1rem;
}
.hero-sub {
  font-size: 1.2rem; opacity: .9; line-height: 1.6;
  margin-bottom: 2.5rem;
}

/* ===== CTA ===== */
.cta-btn {
  display: inline-block; padding: .8rem 1.8rem;
  border-radius: 12px; font-weight: 700; font-size: 1.05rem;
  background: linear-gradient(90deg, #3b82f6, #6366f1);
  color: #fff !important; text-decoration: none;
  transition: transform .2s ease, box-shadow .2s ease;
  cursor: pointer;
}
.cta-btn:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(99,102,241,0.3); }

/* ===== MODAL ===== */
#demo-modal { 
  position: fixed; inset: 0; display: none; align-items: center; justify-content: center; z-index: 9999;
}
#demo-modal.show { display: flex; }
#demo-backdrop {
  position: absolute; inset: 0;
  background: rgba(0,0,0,0.6);
  backdrop-filter: blur(3px);
}
.modal-box {
  position: relative; z-index: 10000;
  width: min(1100px, 92%);
  max-height: 75vh;
  border-radius: 16px;
  overflow: hidden;
  padding: 1rem;
  background: linear-gradient(180deg, rgba(6,6,9,0.95), rgba(12,12,16,0.95));
  box-shadow: 0 30px 80px rgba(0,0,0,0.6);
  transform: translateY(40vh);
  opacity: 0;
  transition: transform 450ms cubic-bezier(.22,.9,.35,1), opacity 220ms ease;
  display: flex;
  align-items: center;
  justify-content: center;
}
#demo-modal.show .modal-box { transform: translateY(0); opacity: 1; }

.video-wrap {
  width: 100%; height: 100%; padding: 1rem; box-sizing: border-box;
  background: #000; border-radius: 12px;
  display: flex; align-items: center; justify-content: center;
}
.video-wrap iframe {
  width: 100%; height: min(60vh, 56.25vw); max-height: 60vh; min-height: 260px;
  border: 0; border-radius: 8px;
}
.modal-close {
  position: absolute; top: 12px; right: 12px; z-index: 10010;
  background: rgba(255,255,255,0.95); border: 0; padding: 8px 10px;
  border-radius: 8px; cursor: pointer; font-weight: 700; font-size: 1rem;
  box-shadow: 0 6px 18px rgba(0,0,0,0.4);
}
.modal-close:focus { outline: 2px solid #3b82f6; }
@media (max-width: 640px){
  .hero { padding: 2.5rem 1rem; }
  .modal-box { padding: 0.6rem; border-radius: 12px; }
}
</style>
""", unsafe_allow_html=True)

# Unified blue button theme across the app (overrides theme)
st.markdown(
    """
<style>
/* Unified blue button theme */
.stButton > button {
  background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%) !important;
  color: #fff !important;
  border-radius: 8px !important;
  border: none !important;
  font-weight: 700 !important;
  box-shadow: 0 2px 8px rgba(30,60,114,0.2) !important;
  transition: transform .2s ease, box-shadow .2s ease !important;
  /* Size/spacing to avoid text wrapping */
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

/* Ensure nav buttons match */
.nav .stButton>button {
  background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%) !important;
  color: #fff !important;
  border-radius: 8px !important;
  border: none !important;
  font-weight: 700 !important;
  box-shadow: 0 2px 8px rgba(30,60,114,0.2) !important;
  /* Make nav buttons bigger and non-wrapping */
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
    left, right = st.columns([2,5], vertical_alignment="center")

    with left:
        st.markdown('<h1 class="brand-name">Exoura</h1>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="nav">', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        if c1.button("Education", use_container_width=True):
            st.switch_page("pages/education.py")
        if c2.button("Demo", use_container_width=True):
            st.switch_page("pages/demo.py")
        if c3.button("Methods", use_container_width=True):
            st.switch_page("pages/methods.py")
        if c4.button("Game", use_container_width=True):
            st.switch_page("pages/game.py")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ HERO ------------------
st.markdown("""
<div class="hero">
  <div class="hero-inner">
    <h1 class="hero-title">Finding worlds between dips</h1>
    <p class="hero-sub">
      Learn how scientists detect exoplanets using transit photometry — 
      and put your skills to the test against an AI trained to spot these hidden worlds.
    </p>
</div>
</div>
""", unsafe_allow_html=True)


# ------------------ VIDEO SECTION ------------------
st.markdown("""
<div class="video-section">
  <div class="video-background"></div>
  <div class="video-container">
    <iframe src="https://www.youtube.com/embed/506-EpLlBrI?si=iMMGdZVqytWoMudD" 
            title="Demo Video" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen></iframe>
  </div>
</div>

<style>
.video-section {
  position: relative;
  width: 100%;
  padding: 4rem 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 3rem;
}

.video-background {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(59,130,246,0.2), rgba(99,102,241,0.2));
  filter: blur(25px);
  border-radius: 16px;
  z-index: 0;
}

.video-container {
  position: relative;
  z-index: 1;
  width: 80%;
  max-width: 900px;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0,0,0,0.6);
}

.video-container iframe {
  width: 100%;
  height: 60vh;
  border: 0;
}
@media (max-width: 640px){
  .video-container iframe { height: 40vh; }
}
</style>
""", unsafe_allow_html=True)

# ------------------ ABOUT SECTION ------------------
# Append-only: add this to the end of home.py

import os
from pathlib import Path
import base64

st.markdown("""
<style>
.about-wrap { max-width: 1100px; margin: 0 auto 4rem; padding: 0 1rem; }
.about-card {
  display: grid; grid-template-columns: 1fr 1.8fr; gap: 2rem;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px; padding: 1.6rem;
  align-items: center;
}
@media (max-width: 880px){
  .about-card { grid-template-columns: 1fr; }
}
.about-title {
  font-family: 'Urbanist', sans-serif;
  font-weight: 900; letter-spacing: -0.02em;
  font-size: clamp(1.6rem, 3.8vw, 2.2rem);
  margin: 0 0 .8rem 0;
  background: linear-gradient(90deg, #7aa2ff, #a78bfa);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.about-text { font-size: 1.06rem; line-height: 1.9; opacity: .95; padding: 0.6rem 0; }
.about-text p { margin-bottom: 0.9rem; }
.about-caption { font-size: .9rem; opacity: .75; margin-top: .6rem; }
.team-img { border-radius: 10px; width: 100%; display: block; }
/* Thin gradient frame around team photo */
.team-frame {
  display: block; width: 100%; border-radius: 14px; padding: 4px; box-sizing: border-box;
  background: linear-gradient(90deg, rgba(45,212,191,0.95), rgba(56,189,248,0.9));
}
.team-frame .team-img { border-radius: 10px; display: block; width: 100%; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* Make the description use the full width of the rounded rectangle */
.about-card { grid-template-columns: 1fr !important; }
.about-card .about-text { grid-column: 1 / -1; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='about-wrap'>", unsafe_allow_html=True)
st.markdown("<h2 class='about-title'>About Team Exoura</h2>", unsafe_allow_html=True)

# Try common paths for the image: web/team_photo.png (same folder as home.py)
def _find_team_photo() -> Optional[str]:
    here = Path(__file__).parent  # e.g., web/
    candidates = [
        here / "team_photo.png",
        here / "assets" / "team_photo.png",
        Path.cwd() / "team_photo.png",
    ]
    for p in candidates:
        if p.is_file():
            return str(p)
    return None

with st.container():
  col_img, col_copy = st.columns([5, 7], vertical_alignment="center")
  with col_img:
    photo_path = _find_team_photo()
    if photo_path:
      try:
        with open(photo_path, 'rb') as f:
          data = f.read()
        b64 = base64.b64encode(data).decode('ascii')
        img_html = (
          '<div class="team-frame">'
          f'<img class="team-img" src="data:image/png;base64,{b64}" alt="Team Exoura" />'
          '</div>'
        )
        st.markdown(img_html, unsafe_allow_html=True)
      except Exception:
        st.image(photo_path, use_container_width=True, caption="Team Exoura")
    else:
      st.warning("Place `team_photo.png` in the same folder as `home.py` (web/) or in `web/assets/`.")
  with col_copy:
    st.markdown(
      "<div class='about-card'>"
      "<div style='display:none'></div>"  # grid placeholder for consistent padding on small screens
      "<div class='about-text'>"
      "At <strong>Team Exoura</strong>, we’re a group of high school students focused on STEM, "
      "including Computer Science and Mechanical Engineering. Our skills span graphic design, "
      "astrophysics, and coding (from C++ to Python). With our background in machine learning, "
      "we’re combining astronomy and AI to build a seamless, interactive interface for exploring exoplanets."
      "<p class='about-caption' style='margin-top: 0.8rem;'>"
      "</p>"
      "</div>"
      "</div>",
      unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)  # close .about-wrap

# ------------------ GITHUB LINK SECTION ------------------
st.markdown(
    """
<style>
.github-wrap { max-width: 1100px; margin: -2rem auto 4rem; padding: 0 1rem; }
.github-card {
  display: flex; align-items: center; gap: 1rem;
  text-decoration: none; border-radius: 16px; padding: 1rem 1.25rem;
  background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: 0 12px 40px rgba(0,0,0,0.35);
  transition: transform .18s ease, border-color .18s ease, background .18s ease, box-shadow .18s ease;
}
.github-card:hover {
  transform: translateY(-2px);
  border-color: rgba(99,102,241,0.45);
  background: linear-gradient(180deg, rgba(99,102,241,0.10), rgba(59,130,246,0.08));
  box-shadow: 0 18px 60px rgba(0,0,0,0.45);
}
.github-logo {
  width: 44px; height: 44px; flex: 0 0 44px;
  display: grid; place-items: center;
  border-radius: 12px;
  background: radial-gradient(100% 100% at 50% 0%, rgba(255,255,255,0.18), rgba(255,255,255,0.05));
  border: 1px solid rgba(255,255,255,0.10);
}
.github-logo svg { width: 26px; height: 26px; fill: #ffffff; opacity: 0.95; }
.github-text { display: flex; flex-direction: column; gap: 2px; color: #e5e7eb; margin-top: 50px; }
.github-text .title {
  font-family: 'Urbanist', sans-serif; font-weight: 800; letter-spacing: -0.01em;
  background: linear-gradient(90deg, #7aa2ff, #a78bfa);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.github-text .url { font-family: 'Azeret Mono', monospace; font-size: .95rem; opacity: .85; }
.github-cta {
  margin-left: auto; font-weight: 700; font-size: .95rem; color: #ffffff;
  background: linear-gradient(90deg, #3b82f6, #6366f1);
  padding: .55rem .9rem; border-radius: 10px;
  border: 1px solid rgba(255,255,255,0.14);
}
@media (max-width: 640px){
  .github-cta { display: none; }
}
</style>

<div class="github-wrap">
  <a class="github-card" href="https://github.com/Daxz0/nasa-space-exoplanets" target="_blank" rel="noopener" aria-label="Open the Exoura GitHub repository">
    <div class="github-logo" aria-hidden="true">
      <svg viewBox="0 0 24 24" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.726-4.042-1.61-4.042-1.61-.546-1.387-1.333-1.757-1.333-1.757-1.09-.745.083-.73.083-.73 1.205.085 1.84 1.237 1.84 1.237 1.07 1.834 2.807 1.304 3.492.997.108-.775.42-1.304.763-1.604-2.665-.303-5.466-1.332-5.466-5.93 0-1.31.47-2.38 1.236-3.22-.124-.303-.536-1.523.117-3.176 0 0 1.008-.322 3.3 1.23a11.5 11.5 0 0 1 3.003-.404c1.02.005 2.047.138 3.003.404 2.29-1.552 3.296-1.23 3.296-1.23.655 1.653.243 2.873.12 3.176.77.84 1.235 1.91 1.235 3.22 0 4.61-2.807 5.624-5.48 5.92.43.37.823 1.102.823 2.222 0 1.604-.015 2.896-.015 3.292 0 .322.217.694.825.576C20.565 22.092 24 17.592 24 12.297 24 5.67 18.627.297 12 .297z"/>
      </svg>
    </div>
    <div class="github-text">
      <div class="title">Exoura on GitHub</div>
      <div class="url">github.com/Daxz0/nasa-space-exoplanets</div>
    </div>
    <div class="github-cta">Open →</div>
  </a>
  
</div>
""",
    unsafe_allow_html=True,
)