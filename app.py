import streamlit as st
import sqlite3

# Veritabanına bağlan
conn = sqlite3.connect('kullanicilar.db')
cursor = conn.cursor()

# Tabloyu oluştur (eğer yoksa)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT,
    email TEXT
)
''')

st.title("👤 Kullanıcı Kayıt Formu")

# Kullanıcıdan bilgi al
ad = st.text_input("Adınız")
email = st.text_input("Email adresiniz")

# Kayıt butonu
if st.button("Kaydet"):
    if ad and email:
        cursor.execute("INSERT INTO users (ad, email) VALUES (?, ?)", (ad, email))
        conn.commit()
        st.success("✅ Kayıt başarıyla eklendi!")
    else:
        st.warning("⚠️ Lütfen tüm alanları doldurun.")

# Yönetici paneli (sadece sen görebil)
st.markdown("---")
st.subheader("🔐 Yönetici Girişi")

sifre = st.text_input("Şifre giriniz:", type="password")

if sifre == "benimsifrem123":  # Buraya kendi şifreni koy
    st.success("✅ Giriş başarılı. Kayıtlı kullanıcılar aşağıda:")
    cursor.execute("SELECT * FROM users")
    kullanicilar = cursor.fetchall()

    for k in kullanicilar:
        st.write(f"{k[0]}. {k[1]} - {k[2]}")
else:
    st.info("📌 Bu kısım sadece yönetici için görünür.")

# Bağlantıyı kapat
conn.close()
