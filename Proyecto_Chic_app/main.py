"""
+CHIC — Boutique de Lujo | main.py
Arquitectura: Proyecto_Chic_app/
  ├── main.py
  ├── assets/    (multimedia)
  └── css/      (luxury_style.css)
"""

import streamlit as st
import base64
from pathlib import Path

# ── Configuración de página ───────────────────────────────────────────────────
st.set_page_config(
    page_title="+CHIC | Luxury Gifts · Sarasota, FL",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Rutas relativas ───────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
ASSETS   = BASE_DIR / "assets"
CSS_FILE = BASE_DIR / "css" / "luxury_style.css"

WHATSAPP_NUMBER = "19412989750"
WHATSAPP_BASE   = f"https://wa.me/{WHATSAPP_NUMBER}"

# ── Helper: imagen → base64 (evita el widget st.image y sus márgenes) ─────────
def img_b64(filename: str) -> str:
    """Devuelve un data-URI base64 listo para usar in <img src=...>. """
    p = ASSETS / filename
    if not p.exists():
        return ""
    mime = "image/jpeg" if str(p).lower().endswith(".jpg") else "image/png"
    return f"data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"

# ── Inyección de CSS externo + overrides Streamlit ───────────────────────────
def inject_css():
    st.markdown('<meta name="google" content="notranslate">', unsafe_allow_html=True)
    try:
        css_text = CSS_FILE.read_text(encoding="utf-8")
        st.markdown(f"<style>{css_text}</style>", unsafe_allow_html=True)
    except:
        pass

    st.markdown("""
    <style>
    /* ── Paleta y Comportamiento Global ── */
    :root { 
        --chic-white: #FFFFFF; 
        --chic-gold: #D4AF37; 
        --chic-gold-light: #FFE57F;
        --chic-gold-dark: #AA820A;
        --chic-red: #8B0000; 
    }

    /* Activar el desplazamiento suave global */
    html, body, .stApp {
        scroll-behavior: smooth !important;
    }

    /* ── Fondo global con más aire inferior para permitir el movimiento ── */
    .stApp {
        background-color: #FAFAF8 !important;
        background-image:
            radial-gradient(at 0% 0%,    rgba(212,175,55,0.08) 0, transparent 55%),
            radial-gradient(at 100% 100%,rgba(139,0,0,0.05)   0, transparent 55%);
        background-attachment: fixed;
        padding-bottom: 60px !important;
    }

    /* ── Ocultar chrome de Streamlit ── */
    #MainMenu, header, footer { visibility: hidden !important; }
    [data-testid="stDecoration"]  { display: none !important; }
    [data-testid="stStatusWidget"]{ display: none !important; }

    /* ── MOBILE-FIRST: contenedor principal ── */
    .block-container {
        padding-top:    0    !important;
        padding-bottom: 40px !important;
        padding-left:   12px !important;
        padding-right:  12px !important;
        max-width:      100% !important;
    }
    @media (min-width: 768px) {
        .block-container {
            padding-left:   32px   !important;
            padding-right:  32px   !important;
            max-width:      1200px !important;
            margin: 0 auto         !important;
        }
    }

    /* ── MARGENES Y GAP BLINDADOS PARA COLUMNAS NATIVAS ── */
    [data-testid="stVerticalBlock"]   { gap: 0 !important; padding: 0 !important; }
    [data-testid="column"]            { padding: 10px !important; background-color: transparent !important; }
    [data-testid="stHorizontalBlock"] { gap: 16px !important; background-color: transparent !important; }
    div[data-styled-column="true"]    { background-color: transparent !important; }

    /* Eliminar márgenes del wrapper de imagen nativo */
    [data-testid="stImage"],
    [data-testid="stImage"] > *,
    .stImage, .stImage > * {
        margin:  0 !important;
        padding: 0 !important;
        line-height: 0 !important;
        font-size:   0 !important;
    }

    /* Imágenes HTML puras */
    .product-img-wrap img, .contact-img img {
        display: block !important;
        margin:  0 !important;
        padding: 0 !important;
        line-height: 0 !important;
        vertical-align: bottom !important;
    }

    /* ── CUADRO DE DISEÑO ── */
    .product-card, .glass-card, .contact-img {
        background: #FFFFFF !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 16px !important;
        overflow: hidden !important;
        box-shadow: inset 0 0 15px rgba(212, 175, 55, 0.18), 0 8px 24px rgba(170, 130, 10, 0.18) !important;
        transition: all 0.35s ease-in-out !important;
        box-sizing: border-box !important;
        display: flex !important;
        flex-direction: column !important;
        height: 100% !important; 
        margin-bottom: 24px !important;
    }
    
    .product-card:hover, .glass-card:hover, .contact-img:hover {
        box-shadow: inset 0 0 22px rgba(212, 175, 55, 0.3), 0 14px 28px rgba(170, 130, 10, 0.25) !important;
        border-color: #F3E5AB !important;
        transform: translateY(-4px);
    }

    /* ── Estilos de botones premium de oro líquido ── */
    .btn-gold {
        background: linear-gradient(135deg, #FFE57F 0%, #D4AF37 50%, #AA820A 100%) !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
        color: #FFFFFF !important;
        border: 1px solid #AA820A !important;
        padding: 12px 20px !important;
        font-family: 'Montserrat', sans-serif !important;
        font-size: 0.76rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
        border-radius: 30px !important;
        cursor: pointer !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 8px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 10px rgba(170, 130, 10, 0.15) !important;
        margin-top: auto !important; 
        margin-bottom: 6px;
    }
    .btn-gold:hover {
        box-shadow: 0 6px 16px rgba(212, 175, 55, 0.4) !important;
    }

    /* ── PRECIOS ── */
    .product-price-bottom {
        font-family: 'Montserrat', sans-serif !important;
        font-size: 0.85rem !important;
        font-weight: 700 !important;
        color: #000000 !important;
        margin-top: auto !important; 
        margin-bottom: 10px !important;
        text-align: center !important;
        letter-spacing: 0.05em !important;
    }

    /* ── SECCIÓN CENTRALIZADA ── */
    .product-info { 
        padding: 12px 14px 14px 14px !important;
        text-align: center !important; 
        background: #FFFFFF !important; 
        display: flex !important;
        flex-direction: column !important;
        flex-grow: 1 !important; 
    }
    .product-name { 
        font-family: 'Playfair Display', serif !important; 
        font-size: 1.05rem !important; 
        font-weight: 600 !important; 
        color: #1A1A1A !important; 
        margin-top: 0px !important;
        margin-bottom: 4px !important;
    }
    .product-caption { 
        font-family: 'Montserrat', sans-serif !important; 
        font-size: 0.74rem !important; 
        color: #6B6B6B !important; 
        line-height: 1.3 !important; 
        margin-bottom: 12px !important;
    }
    .ornament { font-family: 'Montserrat', sans-serif; font-size: 0.68rem; letter-spacing: 0.25em; color: #D4AF37; text-transform: uppercase; }

    /* Divisores Dorados Finos */
    .divider-gold {
        height: 4px;
        background: #D4AF37;
        max-width: 150px;
        margin: 40px auto;
        box-shadow: 0 1px 4px rgba(170, 130, 10, 0.25);
    }

    /* ── TABS NAVEGACIÓN REUBICADAS Y DORADAS METALIZADAS ── */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(255,255,255,0.96);
        backdrop-filter: blur(14px);
        border-bottom: 2px solid #D4AF37;
        padding: 0 12px;
        margin-top: 24px !important;
        position: sticky; top: 0; z-index: 999;
        overflow-x: auto;
        gap: 0;
        box-shadow: 0 4px 12px rgba(170, 130, 10, 0.05);
    }
    
    /* Estado Normal: Letras doradas elegantes */
    .stTabs [data-baseweb="tab"] {
        font-family: 'Montserrat', sans-serif !important;
        font-size:   0.74rem  !important;
        font-weight: 600      !important;
        letter-spacing: 0.14em !important;
        text-transform: uppercase !important;
        color: #C5A028 !important; /* Dorado base sofisticado */
        padding: 18px 20px !important;
        border:  none !important;
        background: transparent !important;
        white-space: nowrap !important;
        transition: all 0.3s ease-in-out !important;
        opacity: 0.85;
    }
    
    /* Estado Activo (Seleccionado): Oro Líquido Brillante Metalizado */
    .stTabs [aria-selected="true"] {
        color: #AA820A !important;
        background: linear-gradient(135deg, #AA820A 0%, #D4AF37 50%, #AA820A 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        text-shadow: 0px 1px 1px rgba(212, 175, 55, 0.2) !important;
        border-bottom: 3px solid #D4AF37 !important;
        opacity: 1 !important;
        transform: scale(1.02);
    }
    
    /* Al pasar el mouse por encima */
    .stTabs [data-baseweb="tab"]:hover {
        color: #D4AF37 !important;
        opacity: 1;
    }
    
    .stTabs [data-baseweb="tab-highlight"],
    .stTabs [data-baseweb="tab-border"] { display: none !important; }

    .essence-grid {
        display: grid !important;
        grid-template-columns: 1fr !important;
        gap: 24px !important;
        padding: 10px 4px !important;
    }
    @media (min-width: 640px)  { .essence-grid { grid-template-columns: repeat(3, 1fr) !important; } }
    
    .contact-img-wrap {
        margin-bottom: 20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

inject_css()

# ── Catálogo: diccionarios con metadatos completos ────────────────────────────
CATALOG = [
    {
        "file":    "regalo1.jpg",
        "name":    "Gift Set Elite",
        "caption": "Premium hand-curated gift box. Perfect for celebrating unique moments.",
        "price":    "", 
        "msg":     "Hi! I'm interested in the Gift Set Elite. Is it available?",
    },                                                                               
    {
        "file":    "regalo2_nuevo.jpg",
        "name":    "Golden Arrangement",
        "caption": "Floral arrangement with gold metallic finishes. Elegance for any occasion.",
        "price":   "38.00 USD",
        "msg":     "Hi! I'm interested in the Golden Arrangement ($38). Can we coordinate delivery?",
    },
    {
        "file":    "regalo3_nuevo.jpg",
        "name":    "Crimson Basket",
        "caption": "Exclusive selection in deep red tones. The gift that never goes unnoticed.",
        "price":   "27.00 USD",
        "msg":     "Hi! I'd like the Crimson Basket ($27). Is it available?",
    },
    {
        "file":    "regalo4_nuevo.jpg",
        "name":    "Box Serenity",
        "caption": "Wellness gift box with luxury body and mind products.",
        "price":   "30.00 USD",
        "msg":     "Hi! I'm interested in the Box Serenity ($30). How can I order it?",
    },
    {
        "file":    "regalo5_nuevo.jpg",
        "name":    "Luxury Bloom",
        "caption": "Artistic bouquet with premium decorative elements. A one-of-a-kind design.",
        "price":   "45.00 USD",
        "msg":     "Hi! I'd love the Luxury Bloom ($45). Can you give me more details?",
    },
    {
        "file":    "regalo6_nuevo.jpg",
        "name":    "Signature Set",
        "caption": "Our flagship box with the +CHIC seal. For those who demand the very best.",
        "price":   "15.00 USD",
        "msg":     "Hi! I want the Signature Set ($15). That's exactly what I'm looking for!",
    },
    {
        "file":    "regalo7_nuevo.jpg",
        "name":    "Romantic Edition",
        "caption": "Special couples set with curated details and impeccable presentation.",
        "price":   "30.00 USD",
        "msg":     "Hi! I love the Romantic Edition ($30). Is it available?",
    },
    {
        "file":    "regalo8_nuevo.jpg",
        "name":    "Mini Luxe Pack",
        "caption": "Compact version of our star set. Big visual impact in a refined small presentation.",
        "price":   "15.00 USD",
        "msg":     "Hi! I'd like the Mini Luxe Pack ($15). Can you help me place the order?",
    },
    {
        "file":    "regalo9_nuevo.jpg",
        "name":    "Grand Prestige",
        "caption": "Our most exclusive piece. Limited-edition handcrafted packaging, truly one of a kind.",
        "price":   "27.00 USD",
        "msg":     "Hi! I'm interested in the Grand Prestige ($27). Is it available?",
    },
]

# ── Helper: ibujado local ──────────────────────────────────────────────────────
def asset_path(filename: str) -> Path:
    return ASSETS / filename

# ── Helper: botón WhatsApp HTML ───────────────────────────────────────────────
def wa_button(msg: str, label: str = "✦ Order via WhatsApp") -> str:
    import urllib.parse
    url = f"{WHATSAPP_BASE}?text={urllib.parse.quote(msg)}"
    return f"""
    <a href="{url}" target="_blank" style="text-decoration:none; display:block; width:100%;">
      <button class="btn-gold">
        <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24" style="vertical-align:middle;">
          <path d="M12.031 21c-1.603 0-3.14-.407-4.498-1.182l-.322-.184-3.344.877.893-3.26-.202-.32A8.932 8.932 0 013.06 12.03C3.06 7.086 7.085 3.06 12.031 3.06c4.945 0 8.97 4.025 8.97 8.97 0 4.945-4.025 8.97-8.97 8.97zm4.83-6.338c-.264-.132-1.563-.771-1.805-.859-.242-.088-.418-.132-.594.132s-.682.859-.836 1.035c-.154.176-.308.198-.572.066-.264-.132-1.114-.41-2.122-1.308-.784-.699-1.313-1.562-1.467-1.826-.154-.264-.016-.407.116-.539.119-.118.264-.308.396-.462.132-.154.176-.264.264-.44.088-.176.044-.33-.022-.462-.066-.132-.594-1.43-.814-1.958-.214-.514-.432-.443-.594-.451l-.506-.009a.97.97 0 00-.704.33c-.242.264-.924.903-.924 2.201s.946 2.553 1.078 2.729c.132.176 1.861 2.84 4.509 3.982.63.272 1.122.434 1.506.556.633.201 1.209.173 1.664.105.507-.075 1.563-.639 1.783-1.257.22-.617.22-1.146.154-1.257-.066-.11-.242-.176-.506-.308z"/>
        </svg>
        <span style="vertical-align:middle; margin-left:4px;">{label}</span>
      </button>
    </a>"""

# ── Render Tarjeta de Producto (100% HTML) ──────────────────────────
def render_product_card(product: dict) -> str:
    src      = img_b64(product["file"])
    wa_html   = wa_button(product["msg"])
    
    price_val = product.get('price', '').strip()
    price_html = f'<div class="product-price-bottom">{price_val}</div>' if price_val else ''

    img_html = (
        f'<img src="{src}" alt="{product["name"]}"'
        f' style="width:100%;height:100%;object-fit:cover;display:block;margin:0;padding:0;">'
        if src else
        f'<div style="display:flex;align-items:center;justify-content:center;'
        f'height:240px;background:#F5F0E8;color:#D4AF37;font-size:0.8rem;">'
        f'📷 {product["file"]}</div>'
    )
    return f"""
    <div class="product-card">
      <div class="product-img-wrap" style="position:relative;overflow:hidden;aspect-ratio:4/3;">
        {img_html}
      </div>
      <div class="product-info">
        <p class="product-name">{product['name']}</p>
        <p class="product-caption">{product['caption']}</p>
        {price_html}
        {wa_html}
      </div>
    </div>"""

# ── Render Catálogo ───────────────────────────────────────────────────────────
def render_catalog():
    st.markdown("""
    <div style="text-align:center;padding:40px 0 24px;">
      <p class="ornament">✦ EXCLUSIVE COLLECTION ✦</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:clamp(1.6rem,5vw,2.4rem);
                 color:#1A1A1A;margin:12px 0 8px;">Our Catalog</h2>
      <p style="font-family:Montserrat,sans-serif;font-size:0.85rem;
                color:#6B6B6B;letter-spacing:0.06em;">
        Every piece, a story. Every gift, a +CHIC experience.
      </p>
    </div>
    <div class="divider-gold"></div>
    """, unsafe_allow_html=True)

    cols = st.columns(3)
    for i, p in enumerate(CATALOG):
        with cols[i % 3]:
            st.markdown(render_product_card(p), unsafe_allow_html=True)

# ── Tab: INICIO ───────────────────────────────────────────────────────────────
def render_inicio():
    st.markdown("""
    <section style="text-align:center;padding:48px 16px 20px;">
      <p class="ornament">✦ LUXURY BOUTIQUE ✦</p>
      <h1 class="hero-title animate__animated animate__fadeInDown" style="margin:16px 0 20px;">+CHIC</h1>
      <p class="hero-subtitle animate__animated animate__fadeInUp animate__delay-1s" style="margin:0 auto 24px;">
        Luxury gifts for unforgettable moments.
      </p>
    </section>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1.2, 1.6, 1.2])
    with c2:
        st.markdown(wa_button(
            "Hi! I'd love to learn more about +CHIC gifts.",
            "✦ Contact Us"
        ), unsafe_allow_html=True)

    st.markdown('<div class="divider-gold"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;padding:40px 0 24px;">
      <p class="ornament">✦ OUR ESSENCE ✦</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:clamp(1.6rem,5vw,2.4rem);
                 color:#1A1A1A;margin:12px 0 8px;">The +CHIC Experience</h2>
      <p style="font-family:Montserrat,sans-serif;font-size:0.85rem;
                color:#6B6B6B;max-width:600px;margin:0 auto;line-height:1.6;">
        We believe gifting is an art. Every detail is carefully designed to convey elegance, exclusivity, and love.
      </p>
    </div>
    """, unsafe_allow_html=True)

    essence = [
        ("inicio1.jpg", "", ""), 
        ("inicio2.jpg", "Impeccable Presentation", "Luxury boxes, silk ribbons, and a flawless finish."),
        ("inicio3.jpg", "Unique Moments", "We don't just deliver gifts, we deliver emotions.")
    ]

    cards = ""
    for img, title, desc in essence:
        src = img_b64(img)
        img_tag = (
            f'<div class="product-img-wrap" style="position:relative;overflow:hidden;aspect-ratio:4/3;">'
            f'<img src="{src}" alt="{title}" style="width:100%;height:100%;display:block;margin:0;object-fit:cover;">'
            f'</div>'
            if src else ""
        )
        
        if title:
            cards += f"""
            <div class="glass-card">
              {img_tag}
              <div class="product-info">
                <p class="product-name">{title}</p>
                <p class="product-caption">{desc}</p>
              </div>
            </div>"""
        else:
            cards += f"""
            <div class="glass-card" style="background:transparent !important; display:block !important; height:auto !important;">
              {img_tag}
            </div>"""
            
    st.markdown(f'<div class="essence-grid">{cards}</div>', unsafe_allow_html=True)

    st.markdown('<div class="divider-gold"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="glass-card" style="text-align:center;padding:48px 32px;max-width:640px;margin:0 auto 60px;">
      <p class="ornament">✦ READY TO IMPRESS? ✦</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:2rem;color:#1A1A1A;margin:16px 0 12px;">
        Create a moment<br>no one will forget
      </h2>
      <p style="font-family:Montserrat,sans-serif;font-size:0.85rem;color:#6B6B6B;margin-bottom:0;">
        Explore our exclusive catalog or contact us for a personalized service.
      </p>
    </div>
    """, unsafe_allow_html=True)

# ── Tab: CONTACTO ─────────────────────────────────────────────────────────────
def render_contacto():
    st.markdown("""
    <div style="text-align:center;padding:48px 24px 36px;">
      <p class="ornament">✦ WE'RE HERE FOR YOU ✦</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:2.4rem;color:#1A1A1A;margin:14px 0 10px;">
        Contact &amp; Orders
      </h2>
      <p style="font-family:Montserrat,sans-serif;font-size:0.88rem;color:#6B6B6B;max-width:500px;margin:0 auto;">
        Our concierge team is ready to guide you through every detail of your perfect gift.
      </p>
    </div>
    <div class="divider-gold"></div>
    """, unsafe_allow_html=True)

    col_imgs, col_info = st.columns([1, 1], gap="large")

    with col_imgs:
        for img in ["contacto1.jpg", "contacto2.jpg", "contacto3.jpg"]:
            src = img_b64(img)
            if src:
                img_html = (
                    f'<div class="contact-img contact-img-wrap" style="aspect-ratio:4/3;">'
                    f'<img src="{src}" alt="+CHIC" style="width:100%;height:100%;display:block;margin:0;object-fit:cover;">'
                    f'</div>'
                )
                st.markdown(img_html, unsafe_allow_html=True)

    with col_info:
        st.markdown("""
        <div style="padding:12px 0;">
          <p class="ornament" style="margin-bottom:16px;">✦ +CHIC L.L.C.</p>
          <h3 style="font-family:'Playfair Display',serif;font-size:1.6rem;
                     color:#8B0000;margin-bottom:20px;">Luxury Boutique</h3>
          <p style="font-family:Montserrat,sans-serif;font-size:0.85rem;color:#6B6B6B;
                    line-height:1.75;margin-bottom:28px;">
            Specialists in personalized luxury gifts. Every box is a work of art
            curated with meticulous attention to detail, guaranteeing an unmatched
            experience for both the giver and the recipient.
          </p>

          <div style="margin-bottom:20px;">
            <p style="font-family:Montserrat,sans-serif;font-size:0.72rem;
                       letter-spacing:0.18em;color:#D4AF37;text-transform:uppercase;
                       margin-bottom:6px;">Direct WhatsApp</p>
            <p style="font-family:Montserrat,sans-serif;font-size:0.9rem;color:#1A1A1A;">
              +1 (941) 298-9750
            </p>
          </div>

          <div style="margin-bottom:20px;">
            <p style="font-family:Montserrat,sans-serif;font-size:0.72rem;
                       letter-spacing:0.18em;color:#D4AF37;text-transform:uppercase;
                       margin-bottom:6px;">Instagram</p>
            <p style="font-family:Montserrat,sans-serif;font-size:0.9rem;color:#1A1A1A;">
              @chic.fl
            </p>
          </div>

          <div style="display:flex;flex-direction:column;gap:14px;margin-top:32px;margin-bottom:20px;">
        """, unsafe_allow_html=True)

        st.markdown(wa_button(
            "Hi! I'd like to place a custom order with +CHIC. Can you assist me?",
            "✦ Place Order via WhatsApp"
        ), unsafe_allow_html=True)

        st.markdown(wa_button(
            "Hi! I have a question about +CHIC gifts in Sarasota.",
            "💬 General Inquiry"
        ), unsafe_allow_html=True)

        st.markdown("""
          </div>

          <div style="margin-top:36px;padding:20px;background:rgba(212,175,55,0.07);
                      border-left:3px solid #D4AF37;border-radius:8px;">
            <p style="font-family:Montserrat,sans-serif;font-size:0.78rem;
                       color:#6B6B6B;line-height:1.7;font-style:italic;">
              "We don't send packages — we deliver stories with the +Chic seal."
            </p>
          </div>
        </div>
        """, unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
def render_footer():
    st.markdown("""
    <div class="divider-gold" style="max-width:100%; margin:40px 0 0 0;"></div>
    <footer style="text-align:center;padding:32px 24px 48px;">
      <p style="font-family:'Playfair Display',serif;font-size:1.8rem;
                font-weight:700;letter-spacing:0.22em;color:#8B0000;margin-bottom:10px;">
        +CHIC
      </p>
      <p class="ornament" style="margin-bottom:16px;">© 2026 +CHIC L.L.C. · Luxury Gifts · Sarasota, FL</p>
      <div style="display:flex;gap:20px;justify-content:center;">
        <a href="https://instagram.com/chic.fl" target="_blank"
           style="font-family:Montserrat,sans-serif;font-size:0.75rem;
                  letter-spacing:0.12em;color:#6B6B6B;text-decoration:none;
                  transition:color 0.3s;"
           onmouseover="this.style.color='#8B0000'"
           onmouseout="this.style.color='#6B6B6B'">
          Instagram
        </a>
        <span style="color:#D4AF37;">·</span>
        <a href="https://wa.me/19412989750" target="_blank"
           style="font-family:Montserrat,sans-serif;font-size:0.75rem;
                  letter-spacing:0.12em;color:#6B6B6B;text-decoration:none;"
           onmouseover="this.style.color='#D4AF37'"
           onmouseout="this.style.color='#6B6B6B'">
          WhatsApp
        </a>
      </div>
    </footer>
    """, unsafe_allow_html=True)

# ── NAVEGACIÓN PRINCIPAL (st.tabs) ────────────────────────────────────────────
tab_inicio, tab_catalogo, tab_contacto = st.tabs(["✦ INICIO", "✦ CATALOG", "✦ CONTACT"])

with tab_inicio:
    render_inicio()

with tab_catalogo:
    render_catalog()

with tab_contacto:
    render_contacto()

render_footer()