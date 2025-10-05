import streamlit as st

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

# ------------------ HEADER ------------------
with st.container():
    st.markdown('<div class="site-header">', unsafe_allow_html=True)
    left, right = st.columns([2,4], vertical_alignment="center")

    with left:
        st.markdown('<h1 class="brand-name">Exoura</h1>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="nav">', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        if c1.button("Education", use_container_width=True):
            st.switch_page("pages/education.py")
        if c2.button("Demo", use_container_width=True):
            st.switch_page("pages/demo.py")
        if c3.button("Methods", use_container_width=True):
            st.switch_page("pages/methods.py")
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
    <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" 
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


