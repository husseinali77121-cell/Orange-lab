import streamlit as st

st.set_page_config(
    page_title="Orange Lab | معمل أورانج لاب للتحاليل الطبية",
    page_icon="🟠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
  html, body, [class*="css"] { font-family: 'Cairo', sans-serif !important; direction: rtl; background: #0a0a0a; color: #fff; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  #MainMenu, footer, header { visibility: hidden; }
  .hero { background: linear-gradient(160deg, #111 0%, #1a1a1a 40%, #FF6B00 100%); padding: 48px 24px 40px; text-align: center; position: relative; overflow: hidden; }
  .hero::before { content: ''; position: absolute; inset: 0; background: radial-gradient(circle at 70% 50%, rgba(255,107,0,0.18) 0%, transparent 70%); }
  .logo-ring { width: 110px; height: 110px; border: 6px solid #FF6B00; border-radius: 50%; margin: 0 auto 16px; display: flex; align-items: center; justify-content: center; background: #111; box-shadow: 0 0 40px rgba(255,107,0,0.4); position: relative; z-index: 1; }
  .logo-inner { font-size: 38px; }
  .hero-title { font-size: 34px; font-weight: 900; color: #FF6B00; margin: 0 0 4px; line-height: 1.1; position: relative; z-index: 1; text-shadow: 0 2px 20px rgba(255,107,0,0.4); }
  .hero-sub { font-size: 17px; color: #fff; font-weight: 700; margin: 0 0 10px; position: relative; z-index: 1; }
  .hero-tagline { font-size: 14px; color: rgba(255,255,255,0.7); margin: 0 0 24px; position: relative; z-index: 1; }
  .cta-group { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; position: relative; z-index: 1; }
  .cta-wa { background: #25D366; color: #fff !important; padding: 14px 28px; border-radius: 50px; font-size: 15px; font-weight: 800; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 6px 24px rgba(37,211,102,0.4); transition: transform 0.2s; }
  .cta-call { background: transparent; color: #FF6B00 !important; padding: 14px 28px; border-radius: 50px; font-size: 15px; font-weight: 800; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; border: 2px solid #FF6B00; transition: transform 0.2s; }
  .badge-strip { background: #FF6B00; padding: 12px 20px; display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; }
  .badge { background: rgba(0,0,0,0.25); color: #fff; border-radius: 20px; padding: 5px 14px; font-size: 12px; font-weight: 700; }
  .section { padding: 32px 20px; max-width: 640px; margin: 0 auto; }
  .section-title { font-size: 20px; font-weight: 800; color: #FF6B00; margin-bottom: 20px; text-align: center; display: flex; align-items: center; justify-content: center; gap: 10px; }
  .why-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
  .why-card { background: #1a1a1a; border-radius: 16px; padding: 18px 14px; text-align: center; border: 1px solid #2a2a2a; transition: border-color 0.2s; }
  .why-card:hover { border-color: #FF6B00; }
  .why-icon { font-size: 28px; margin-bottom: 8px; }
  .why-title { font-size: 13px; font-weight: 700; color: #FF6B00; margin-bottom: 4px; }
  .why-desc { font-size: 11px; color: #888; line-height: 1.5; }
  .services-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
  .service-chip { background: #1a1a1a; border: 1px solid #2a2a2a; border-radius: 12px; padding: 12px 14px; font-size: 13px; font-weight: 600; color: #fff; display: flex; align-items: center; gap: 8px; }
  .service-chip span { font-size: 18px; }
  .disc-list { display: flex; flex-direction: column; gap: 10px; }
  .disc-item { background: linear-gradient(90deg, #1a1a1a, #222); border-radius: 14px; padding: 14px 18px; display: flex; align-items: center; justify-content: space-between; border-right: 4px solid #FF6B00; }
  .disc-name { font-size: 14px; font-weight: 700; color: #fff; }
  .disc-pct { background: #FF6B00; color: #fff; border-radius: 8px; padding: 4px 12px; font-size: 15px; font-weight: 900; }
  .hv-banner { background: linear-gradient(135deg, #FF6B00, #FF9A3C); border-radius: 20px; padding: 28px 22px; text-align: center; margin: 0 20px; }
  .hv-title { font-size: 22px; font-weight: 900; color: #fff; margin-bottom: 8px; }
  .hv-sub { font-size: 14px; color: rgba(255,255,255,0.9); margin-bottom: 20px; }
  .hv-btn { background: #fff; color: #FF6B00 !important; padding: 13px 30px; border-radius: 50px; font-size: 15px; font-weight: 800; text-decoration: none; display: inline-block; box-shadow: 0 6px 20px rgba(0,0,0,0.2); }
  .location-card { background: #1a1a1a; border-radius: 16px; padding: 20px; border: 1px solid #2a2a2a; }
  .location-row { display: flex; gap: 12px; align-items: flex-start; margin-bottom: 14px; }
  .loc-icon { font-size: 22px; margin-top: 2px; flex-shrink: 0; }
  .loc-text { font-size: 13px; color: #ccc; line-height: 1.7; }
  .loc-link { display: block; background: #FF6B00; color: #fff !important; text-decoration: none; text-align: center; padding: 12px; border-radius: 12px; font-weight: 700; font-size: 14px; margin-top: 14px; }
  
  /* تم إضافة هذا السطر لحل مشكلة أرقام الهواتف */
  .phone-link { color: #FF6B00 !important; font-weight: 700; text-decoration: none; margin: 0 5px; }
  
  .footer { background: #111; padding: 28px 20px; text-align: center; border-top: 1px solid #222; margin-top: 32px; }
  .footer-logo { font-size: 20px; font-weight: 900; color: #FF6B00; margin-bottom: 8px; }
  .footer-sub { font-size: 12px; color: #555; }
  .floating-wa { position: fixed; bottom: 24px; left: 20px; background: #25D366; color: #fff !important; width: 58px; height: 58px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 26px; text-decoration: none; box-shadow: 0 6px 24px rgba(37,211,102,0.5); z-index: 999; animation: pulse 2s infinite; }
  @keyframes pulse { 0%,100% { box-shadow: 0 0 0 0 rgba(37,211,102,0.4); } 50% { box-shadow: 0 0 0 12px rgba(37,211,102,0); } }
  div[data-testid="stButton"] { display: none; }
</style>

<div class="hero">
  <div class="logo-ring"><div class="logo-inner">🔬</div></div>
  <div class="hero-title">ORANGE LAB</div>
  <div class="hero-sub">معمل أورانج لاب للتحاليل الطبية</div>
  <div class="hero-tagline">نتائجكم هي رأيكم أهم — نتائج دقيقة بأعلى معايير الجودة</div>
  <div class="cta-group">
    <a href="https://wa.me/201097902820" target="_blank" class="cta-wa">📱 تواصل واتساب</a>
    <a href="tel:01097902820" class="cta-call">📞 اتصل بنا</a>
  </div>
</div>

<div class="badge-strip">
  <div class="badge">🏠 زيارات منزلية</div>
  <div class="badge">⚡ نتائج سريعة</div>
  <div class="badge">✅ معتمد</div>
  <div class="badge">💰 أسعار تنافسية</div>
  <div class="badge">🎁 عروض مستمرة</div>
</div>

<div class="section">
  <div class="section-title">⭐ لماذا تختار أورانج لاب؟</div>
  <div class="why-grid">
    <div class="why-card">
      <div class="why-icon">🎯</div>
      <div class="why-title">الدقة والموثوقية</div>
      <div class="why-desc">نتائج معتمدة من خبراء التحاليل الطبية</div>
    </div>
    <div class="why-card">
      <div class="why-icon">⚙️</div>
      <div class="why-title">أحدث التقنيات</div>
      <div class="why-desc">أجهزة طبية حديثة لضمان دقة وسرعة النتائج</div>
    </div>
    <div class="why-card">
      <div class="why-icon">🏠</div>
      <div class="why-title">خدمة منزلية</div>
      <div class="why-desc">سحب العينات من منزلك براحة تامة</div>
    </div>
    <div class="why-card">
      <div class="why-icon">💰</div>
      <div class="why-title">أسعار تنافسية</div>
      <div class="why-desc">عروض مستمرة مناسبة للجميع</div>
    </div>
  </div>
</div>

<div class="section" style="padding-top:0">
  <div class="section-title">🧪 خدماتنا</div>
  <div class="services-grid">
    <div class="service-chip"><span>🩸</span> تحاليل الدم</div>
    <div class="service-chip"><span>🔬</span> تحاليل الهرمونات</div>
    <div class="service-chip"><span>🫀</span> وظائف الكبد والكلى</div>
    <div class="service-chip"><span>🛡️</span> الأمراض المناعية</div>
    <div class="service-chip"><span>💍</span> تحاليل ما قبل الزواج</div>
    <div class="service-chip"><span>🦠</span> الكشف المبكر عن السرطان</div>
    <div class="service-chip"><span>🧬</span> تحاليل الغدة الدرقية</div>
    <div class="service-chip"><span>💉</span> السكري والكوليسترول</div>
  </div>
</div>

<div class="section" style="padding-top:0">
  <div class="section-title">🎁 خصوماتنا</div>
  <div class="disc-list">
    <div class="disc-item">
      <div class="disc-name">🩺 نقابة أطباء + مهندسين</div>
      <div class="disc-pct">60%</div>
    </div>
    <div class="disc-item">
      <div class="disc-name">💊 فيتامين د</div>
      <div class="disc-pct">60%</div>
    </div>
    <div class="disc-item">
      <div class="disc-name">🏃 الأندية الرياضية</div>
      <div class="disc-pct">50%</div>
    </div>
    <div class="disc-item">
      <div class="disc-name">🏥 شركات التأمين الطبي</div>
      <div class="disc-pct">40%</div>
    </div>
    <div class="disc-item">
      <div class="disc-name">🇸🇾 الجالية السورية</div>
      <div class="disc-pct">30%</div>
    </div>
  </div>
</div>

<div class="hv-banner">
  <div class="hv-title">🏠 خدمة الزيارات المنزلية</div>
  <div class="hv-sub">ماتتعبش — احنا بنيجي لك!<br>سحب العينات من منزلك بكل راحة وأمان</div>
  <a href="https://wa.me/201097902820?text=أريد%20حجز%20زيارة%20منزلية" target="_blank" class="hv-btn">
    📱 احجز زيارة منزلية الآن
  </a>
</div>

<div class="section">
  <div class="section-title">📍 موقعنا</div>
  <div class="location-card">
    <div class="location-row">
      <div class="loc-icon">📍</div>
      <div class="loc-text">
        أمام ديامونـد مـول والعبد — أعلى كوافير عادل المصري وكازابلانكا كافيه<br>
        المحور المركزي — أول أكتوبر — الجيزة
      </div>
    </div>
    <div class="location-row">
      <div class="loc-icon">📞</div>
      <div class="loc-text" style="direction: ltr; text-align: right;">
        <a href="tel:0236969125" class="phone-link">02 3696 9125</a>
        |
        <a href="tel:01097902820" class="phone-link">010 9790 2820</a>
      </div>
    </div>
    <a href="https://maps.app.goo.gl/azH46Kc4YfJhoYVPA" target="_blank" class="loc-link">
      🗺️ افتح على الخريطة
    </a>
  </div>
</div>

<div class="footer">
  <div class="footer-logo">🟠 ORANGE LAB</div>
  <div class="footer-sub">معمل أورانج لاب للتحاليل الطبية<br>© 2026 جميع الحقوق محفوظة</div>
</div>

<a href="https://wa.me/201097902820" target="_blank" class="floating-wa">💬</a>
""", unsafe_allow_html=True)
