import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================================================================
# 1. SETUP HALAMAN & KONFIGURASI (UNTUK TIM DATA & AI)
# ==============================================================================
st.set_page_config(
    page_title="MBG-Scan | Professional Nutrition Analytics", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CATATAN UNTUK (AI ENGINEER) ---
if 'data_kamera' not in st.session_state:
    st.session_state['data_kamera'] = {
        'Menu': ['Nasi Putih', 'Ayam Goreng', 'Capcay', 'Susu UHT', 'Pisang'],
        'Kategori': ['Karbohidrat', 'Protein', 'Sayur', 'Minuman', 'Buah'],
        'Kalori': [204, 260, 42, 60, 43],
        'Protein': [4.2, 23.0, 1.5, 2.0, 0.8],
        'Lemak': [0.4, 15.0, 1.8, 1.5, 0.23],
        'Karbohidrat': [44.1, 0.0, 6.2, 5.0, 11.94]
    }

df_ompreng = pd.DataFrame(st.session_state['data_kamera'])

# Target AKG Kemenkes (30% Makan Siang)
target_akg = {
    'TK': {'Kalori': 420, 'Protein': 8.0, 'Lemak': 13.0, 'Karbohidrat': 65.0},
    'SD': {'Kalori': 610, 'Protein': 16.0, 'Lemak': 20.0, 'Karbohidrat': 77.0},
    'SMP': {'Kalori': 700, 'Protein': 21.0, 'Lemak': 23.0, 'Karbohidrat': 90.0},
    'SMA': {'Kalori': 800, 'Protein': 25.0, 'Lemak': 26.0, 'Karbohidrat': 105.0}
}

# ==============================================================================
# 2. SIDEBAR PANEL KONTROL (Corporate Style)
# ==============================================================================
with st.sidebar:
    st.markdown("<h2 style='color: #1A237E; font-size: 20px; font-weight: bold;'>📋 PANEL KONTROL</h2>", unsafe_allow_html=True)
    st.write("Filter target sasaran program Makan Bergizi Gratis.")
    
    pilihan_sekolah = st.selectbox(
        "Tingkat Sekolah Sasaran:",
        options=['TK', 'SD', 'SMP', 'SMA'],
        index=1  # Default SD
    )
    
    # Hitung total aktual gizi
    total_kalori = round(df_ompreng['Kalori'].sum(), 1)
    total_protein = round(df_ompreng['Protein'].sum(), 1)
    total_lemak = round(df_ompreng['Lemak'].sum(), 1)
    total_karbo = round(df_ompreng['Karbohidrat'].sum(), 1)
    total_item = len(df_ompreng)
    target = target_akg[pilihan_sekolah]
    
    st.markdown("---")
    st.markdown("<h2 style='color: #1A237E; font-size: 18px; font-weight: bold;'>🚨 STATUS KELAYAKAN</h2>", unsafe_allow_html=True)
    
    persen_kalori = round((total_kalori / target['Kalori']) * 100, 1)
    persen_protein = round((total_protein / target['Protein']) * 100, 1)

    if persen_kalori >= 95 and persen_protein >= 100:
        st.success(f"**MEMENUHI STANDAR GIZI**\n\nSkor Kecukupan:\nKalori: {persen_kalori}%\nProtein: {persen_protein}%")
    else:
        st.warning(f"**PERLU PENYESUAIAN PORSI**\n\nSkor Kecukupan:\nKalori: {persen_kalori}%\nProtein: {persen_protein}%")

# ==============================================================================
# 3. HEADER UTAMA & BLOK KOTAK 
# ==============================================================================
st.markdown("<h1 style='text-align: left; color: #1A237E; font-size: 32px; font-weight: bold; margin-bottom: 5px;'>DASHBOARD SCAN MENU MBG</h1>", unsafe_allow_html=True)

st.markdown("""
    <style>
    .metric-card-solid {
        padding: 20px; border-radius: 8px; flex: 1;
        box-shadow: 0 4px 6px rgba(0,0,0,0.06); text-align: left;
        color: white; margin-bottom: 15px;
    }
    .metric-head-solid { font-size: 11px; color: rgba(255, 255, 255, 0.85); font-weight: bold; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; }
    .metric-body-solid { display: flex; align-items: baseline; gap: 6px; margin-bottom: 8px; }
    .metric-value-solid { font-size: 26px; font-weight: bold; color: white; }
    .metric-unit-solid { font-size: 13px; color: rgba(255, 255, 255, 0.9); font-weight: 500; }
    .metric-target-solid { font-size: 11px; color: rgba(255, 255, 255, 0.75); border-top: 1px solid rgba(255, 255, 255, 0.2); padding-top: 6px; font-style: italic;}
    </style>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

def render_solid_metric(col, label, value, unit, target_val, bg_color):
    with col:
        st.markdown(f"""
            <div class="metric-card-solid" style="background-color: {bg_color};">
                <div class="metric-head-solid">{label}</div>
                <div class="metric-body-solid">
                    <span class="metric-value-solid">{value}</span>
                    <span class="metric-unit-solid">{unit}</span>
                </div>
                <div class="metric-target-solid">Target {pilihan_sekolah}: {target_val} {unit}</div>
            </div>
        """, unsafe_allow_html=True)

render_solid_metric(col1, "Total Energi", f"{total_kalori}", "kkal", f"{target['Kalori']}", "#1A237E")
render_solid_metric(col2, "Total Protein", f"{total_protein}", "gram", f"{target['Protein']}", "#00796B")
render_solid_metric(col3, "Total Lemak", f"{total_lemak}", "gram", f"{target['Lemak']}", "#005662")
render_solid_metric(col4, "Total Karbohidrat", f"{total_karbo}", "gram", f"{target['Karbohidrat']}", "#283593")
render_solid_metric(col5, "📸 Item Terdeteksi", f"{total_item}", "Menu", "AI Scan", "#2E7D32")

st.markdown("<br>", unsafe_allow_html=True)

# ==============================================================================
# 4. BARIS TENGAH: GRID SEJAJAR DENGAN PEMISAH KOTAK (CARD)
# ==============================================================================
g1, g2, g3 = st.columns([1.1, 0.9, 1])

sns.set_theme(style="white", palette="muted")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 9

with g1:
    # Menggunakan st.container(border=True) untuk membuat pembatas kotak putih luar
    with st.container(border=True):
        st.markdown("<h4 style='color: #424242; font-size: 15px; font-weight: bold; margin-bottom: 10px;'>Pemenuhan Target AKG Kemenkes (%)</h4>", unsafe_allow_html=True)
        
        df_pemenuhan = pd.DataFrame({
            'Zat Gizi': ['Kalori', 'Protein', 'Lemak', 'Karbohidrat'],
            'Persen': [
                (total_kalori / target['Kalori']) * 100,
                (total_protein / target['Protein']) * 100,
                (total_lemak / target['Lemak']) * 100,
                (total_karbo / target['Karbohidrat']) * 100
            ]
        })
        
        fig1, ax1 = plt.subplots(figsize=(4.5, 3.2))
        colors1 = ['#B0BEC5' if x < 100 else '#3F51B5' for x in df_pemenuhan['Persen']]
        sns.barplot(data=df_pemenuhan, x='Zat Gizi', y='Persen', palette=colors1, ax=ax1, width=0.6)
        
        ax1.axhline(100, color='#D32F2F', linestyle='--', linewidth=1, label='Target Minimum')
        
        for p in ax1.patches:
            if p.get_height() > 0:
                ax1.annotate(f"{round(p.get_height(), 1)}%", (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 6), textcoords='offset points', fontsize=8, fontweight='bold', color='#1A237E')
        
        ax1.set_ylabel('Pemenuhan (%)', fontsize=8)
        ax1.set_xlabel('')
        ax1.tick_params(axis='x', labelsize=8)
        ax1.set_ylim(0, 140)
        sns.despine(left=True, bottom=True)
        plt.tight_layout()
        st.pyplot(fig1)

with g2:
    # Pembatas kotak untuk grafik donat kontribusi energi
    with st.container(border=True):
        st.markdown("<h4 style='color: #424242; font-size: 15px; font-weight: bold; margin-bottom: 10px;'>Kontribusi Energi per Menu</h4>", unsafe_allow_html=True)
        fig2, ax2 = plt.subplots(figsize=(3.5, 3.5))
        
        colors_corp = ['#1A237E', '#3949AB', '#5C6BC0', '#9FA8DA', '#C5CAE9']
        wedges, texts, autotexts = ax2.pie(
            df_ompreng['Kalori'], labels=df_ompreng['Menu'], autopct='%1.1f%%', 
            startangle=110, colors=colors_corp, pctdistance=0.78,
            textprops=dict(fontsize=8)
        )
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_weight('bold')
        for text in texts:
            text.set_color('#424242')
            text.set_weight('bold')
            
        centre_circle = plt.Circle((0,0), 0.60, fc='white')
        fig2.gca().add_artist(centre_circle)
        ax2.axis('equal')  
        plt.tight_layout()
        st.pyplot(fig2)

with g3:
    # Pembatas kotak untuk tabel detail komponen data gram
    with st.container(border=True):
        st.markdown("<h4 style='color: #424242; font-size: 15px; font-weight: bold; margin-bottom: 15px;'>Detail Komponen Menu yang Terdeteksi</h4>", unsafe_allow_html=True)
        
        df_tampilan = df_ompreng.copy()
        row_total = pd.DataFrame([{
            'Menu': 'TOTAL', 'Protein': total_protein, 'Lemak': total_lemak, 'Karbohidrat': total_karbo
        }])
        df_tampilan = pd.concat([df_tampilan, row_total], ignore_index=True)
        
        st.dataframe(df_tampilan[['Menu', 'Protein', 'Lemak', 'Karbohidrat']], use_container_width=True, hide_index=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==============================================================================
# 5. BARIS BAWAH: ANALISIS MENDALAM DENGAN PEMISAH KOTAK (CARD)
# ==============================================================================
g4, g5 = st.columns([1.2, 1])

with g4:
    # Pembatas kotak untuk stacked barchart distribusi berat makro
    with st.container(border=True):
        st.markdown("<h4 style='color: #424242; font-size: 15px; font-weight: bold; margin-bottom: 10px;'>Distribusi Berat Nutrisi Makro (Gram) per Menu</h4>", unsafe_allow_html=True)
        
        fig4, ax4 = plt.subplots(figsize=(6, 3))
        df_stacked = df_ompreng.set_index('Menu')[['Protein', 'Lemak', 'Karbohidrat']]
        df_stacked.plot(kind='bar', stacked=True, color=['#3F51B5', '#7986CB', '#C5CAE9'], ax=ax4, width=0.5)
        
        plt.xticks(rotation=0, fontsize=8, fontweight='bold', color='#424242')
        plt.ylabel('Berat (Gram)', fontsize=8)
        plt.xlabel('')
        plt.legend(['Protein', 'Lemak', 'Karbo'], fontsize=8, loc='upper right', frameon=False)
        sns.despine(left=True, bottom=True)
        plt.tight_layout()
        st.pyplot(fig4)

with g5:
    # Pembatas kotak untuk barchart horizontal kategori pangan
    with st.container(border=True):
        st.markdown("<h4 style='color: #424242; font-size: 15px; font-weight: bold; margin-bottom: 10px;'>Ringkasan Energi Berdasarkan Kategori Pangan</h4>", unsafe_allow_html=True)
        
        fig5, ax5 = plt.subplots(figsize=(5, 3))
        df_kategori = df_ompreng.groupby('Kategori')['Kalori'].sum().reset_index().sort_values(by='Kalori', ascending=False)
        
        sns.barplot(data=df_kategori, x='Kalori', y='Kategori', palette='Blues_d', ax=ax5, width=0.6)
        
        for p in ax5.patches:
            if p.get_width() > 0:
                ax5.annotate(f"{int(p.get_width())} kkal", (p.get_width(), p.get_y() + p.get_height() / 2.), ha='left', va='center', xytext=(5, 0), textcoords='offset points', fontsize=8, fontweight='bold', color='#1A237E')
        ax5.set_xlabel('Total Kalori', fontsize=8)
        ax5.set_ylabel('')
        ax5.tick_params(axis='y', labelsize=8)
        sns.despine(left=True, bottom=True)
        plt.tight_layout()
        st.pyplot(fig5)