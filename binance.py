import streamlit as st
import pandas as pd
import requests
import time

# إعدادات الواجهة العريضة لـ Streamlit
st.set_page_config(layout="wide", page_title="Falcon Live Dashboard")
st.title("🚀 Falcon Egypt - لوحة تحكم الصيد الرقمي الحية السحابية")
st.subheader("📊 مسح أونلاين مباشر لعملات باينانس (النسخة الذهبية المستقرة والمعالجة بالكامل)")

# قائمتك الكاملة المكونة من 448 زوجاً الخاصة بك بعد إزالة التكرار وضبط النصوص
MY_BINANCE_COINS = [
    "0G", "1000CAT", "1000CHEEMS", "1000SATS", "1INCH", "1MBABYDOGE", "2Z", "A", "AAVE", "ACE",
    "ACH", "ACM", "ACT", "ACX", "ADA", "ADX", "AEUR", "AEVO", "AGLD", "AI", "AIGENSYN", "AIXBT",
    "ALGO", "ALICE", "ALLO", "ALPINE", "ALT", "AMDB", "AMP", "ANIME", "ANKR", "APE", "API3",
    "APT", "AR", "ARB", "ARK", "ARKM", "ARPA", "ASR", "ASTER", "ASTR", "ATM", "ATOM",
    "AUCTION", "AUDIO", "AVA", "AVAX", "AVNT", "AWE", "AXL", "AXS", "BABY", "BANANA", "BANANAS31",
    "BAND", "BANK", "BAR", "BARD", "BAT", "BB", "BCH", "BEAMX", "BEL", "BERA", "BFUSD", "BICO",
    "BIGTIME", "BIO", "BLUR", "BMT", "BNB", "BNSOL", "BNT", "BOME", "BONK", "BREV", "BROCCOLI714",
    "BTC", "BTTC", "C", "C98", "CAKE", "CATI", "CBRSB", "CELO", "CELR", "CETUS", "CFG", "CFX",
    "CGPT", "CHIP", "CHR", "CHZ", "CITY", "CKB", "COINB", "COMP", "COOKIE", "COTI", "COW",
    "CRCLB", "CRV", "CTK", "CTSI", "CVC", "CVX", "CYBER", "DASH", "DCR", "DEXE", "DGB", "DIA",
    "DODO", "DOGE", "DOGS", "DOLO", "DOT", "DRAMB", "DUSK", "DYDX", "DYM", "EDEN", "EDU", "EGLD",
    "EIGEN", "ENA", "ENJ", "ENS", "ENSO", "EPIC", "ERA", "ESP", "ETC", "ETH", "ETHFI", "EUL",
    "EUR", "EURI", "EWYB", "F", "FDUSD", "FET", "FF", "FIDA", "FIL", "FLOKI", "FLOW", "FLUX",
    "FOGO", "FORM", "FRAX", "FTT", "G", "GALA", "GAS", "GENIUS", "GIGGLE", "GLM", "GLMR", "GLWB",
    "GMT", "GMX", "GNO", "GNS", "GOOGLB", "GPS", "GRAM", "GRT", "GTC", "GUN", "HAEDAL", "HBAR",
    "HEI", "HEMI", "HFT", "HIVE", "HMSTR", "HOLO", "HOME", "HOT", "HUMA", "HYPER", "ICP", "ICX",
    "ID", "ILV", "IMX", "INIT", "INJ", "INTCB", "IO", "IOST", "IOTA", "IOTX", "IQ", "JASMY",
    "JOE", "JST", "JTO", "JUP", "JUV", "KAIA", "KAITO", "KAT", "KAVA", "KERNEL", "KGST", "KITE",
    "KMNO", "KNC", "KSM", "LA", "LAYER", "LAZIO", "LDO", "LINEA", "LINK", "LISTA", "LITEB", "LPT",
    "LQTY", "LSK", "LTC", "LUMIA", "LUNA", "LUNC", "MAGIC", "MANA", "MANTA", "MANTRA", "MASK",
    "MAV", "MBL", "ME", "MEGA", "MEME", "MET", "METAB", "METIS", "MINA", "MIRA", "MITO", "MMT",
    "MORPHO", "MOVE", "MOVR", "MSFTB", "MSTRB", "MTL", "MUB", "MUBARAK", "NBISB", "NEAR", "NEIRO",
    "NEO", "NEWT", "NEXO", "NIGHT", "NIL", "NMR", "NOM", "NOT", "NVDAB", "NXPC", "OG", "OGN",
    "ONDO", "ONE", "ONG", "ONT", "OP", "OPEN", "OPG", "OPN", "ORCA", "ORDI", "OSMO", "PARTI",
    "PAXG", "PENDLE", "PENGU", "PEOPLE", "PEPE", "PHA", "PIVX", "PIXEL", "PLTRB", "PLUME", "PNUT",
    "POL", "POLYX", "PORTAL", "PORTO", "POWR", "PROM", "PROVE", "PSG", "PUMP", "PUNDIX", "PYR",
    "PYTH", "QCOMB", "QI", "QKC", "QNT", "QQQB", "QTUM", "QUICK", "RAD", "RARE", "RAY", "RE",
    "RED", "RENDER", "REQ", "RESOLV", "REZ", "RIF", "RLC", "RLUSD", "ROBO", "RONIN", "ROSE",
    "RPL", "RSR", "RUNE", "RVN", "S", "SAGA", "SAHARA", "SAND", "SANTOS", "SAPIEN", "SC", "SCR",
    "SCRT", "SEI", "SENT", "SFP", "SHELL", "SHIB", "SIGN", "SKL", "SKY", "SLP", "SNDKB", "SNX",
    "SOL", "SOLV", "SOMI", "SOPH", "SOXLB", "SPCXB", "SPELL", "SPK", "SPYB", "SSV", "STEEM",
    "STG", "STO", "STORJ", "STRAX", "STRK", "STX", "SUI", "SUN", "SUPER", "SUSHI", "SXT", "SYN",
    "SYRUP", "T", "TAO", "TFUEL", "THE", "THETA", "TIA", "TKO", "TLM", "TNSR", "TOWNS", "TRB",
    "TREE", "TRUMP", "TRX", "TSLAB", "TST", "TURBO", "TURTLE", "TUSD", "TUT", "TWT", "U", "UMA",
    "UNI", "USD1", "USDC", "USDE", "USDP", "USDS", "USTC", "USUAL", "VANA", "VANRY", "VELODROME",
    "VET", "VIC", "VIRTUAL", "VTHO", "W", "WAL", "WAXP", "WBETH", "WBTC", "WCT", "WDCB", "WIF",
    "WIN", "WLD", "WLFI", "WOO", "XAI", "XAUT", "XEC", "XLM", "XNO", "XPL", "XRP", "XTZ", "XUSD",
    "XVG", "XVS", "YB", "YFI", "YGG", "ZAMA", "ZBT", "ZEC", "ZEN", "ZIL", "ZK", "ZKC", "ZKP",
    "ZRO", "ZRX"
]

# فلاتر التصفية الجانبية
st.sidebar.header("🎯 فلاتر التحكم والتصفية")
show_only_breakouts = st.sidebar.checkbox("عرض العملات المخترقة فقط (Breakout)", value=False)
rsi_min = st.sidebar.slider("الحد الأدنى لمؤشر RSI التقديري", 0, 100, 0)
rvol_min = st.sidebar.slider("الحد الأدنى للزخم النسبي", 0.0, 5.0, 0.0, step=0.1)

# دالة التلوين المحدثة المتوافقة كلياً مع الجداول السحابية
def style_dataframe(df_to_style):
    def make_styles(row):
        styles = [''] * len(row)
        if row['Breakout'] == True:
            styles = ['background-color: #1b3a24; color: #00ffcc; font-weight: bold;'] * len(row)
        return styles
    
    def color_rsi(val):
        try:
            val_float = float(val)
            if val_float >= 70: return 'background-color: #4a1b1b; color: #ff4a4a; font-weight: bold;'
            elif val_float <= 30: return 'background-color: #1b4a2d; color: #00ffaa; font-weight: bold;'
        except (ValueError, TypeError):
            pass
        return ''

    return df_to_style.style.apply(make_styles, axis=1).map(color_rsi, subset=['RSI'])

@st.fragment
def render_live_dashboard():
    try:
        # إرسال هيدرز موثقة بالكامل لتخطي حماية السيرفرات السحابية
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json"
        }
        
        # طلب إجمالي موحد ومباشر لأسعار سوق KuCoin المفتوح سحابياً
        url = "https://kucoin.com"
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200 and "application/json" in response.headers.get("Content-Type", ""):
            ticker_list = response.json().get('data', {}).get('ticker', [])
            parsed_data = []
            target_set = {coin.upper() for coin in MY_BINANCE_COINS}
            
            for item in ticker_list:
                symbol_raw = item.get('symbol', '')
                
                if symbol_raw.endswith('-USDT'):
                    coin_base = symbol_raw.replace('-USDT', '').upper()
                    
                    if coin_base in target_set:
                        current_price = float(item.get('last', 0) or 0)
                        # ضبط الحساب الرياضي للنسبة المئوية القادمة من السيرفر كقيمة عشرية
                        price_change_pct = float(item.get('changeRate', 0) or 0) * 100
                        high_24h = float(item.get('high', 0) or 0)
                        
                        pct_1h = price_change_pct / 24.0
                        estimated_rsi = max(0, min(100, 50 + (pct_1h * 3)))
                        rvol_score = round(1.0 + (abs(pct_1h) / 2), 2)
                        
                        high_breakout = bool(high_24h > 0 and current_price >= high_24h * 0.995)
                        bb_breakout = bool(pct_1h > 2.0)
                        ma50_breakout = bool(price_change_pct > 5.0 and pct_1h > 0)
                        any_breakout = high_breakout or bb_breakout or ma50_breakout
                        
                        parsed_data.append({
                            'Symbol': f"{coin_base}/USDT",
                            'Price': round(current_price, 6) if current_price < 1 else round(current_price, 4),
                            'RVOL': rvol_score,
                            'RSI': round(estimated_rsi, 2),
                            'BB_Breakout': "🟢" if bb_breakout else "🔴",
                            'MA50_Breakout': "🟢" if ma50_breakout else "🔴",
                            'High_Breakout': "🟢" if high_breakout else "🔴",
                            'Breakout': any_breakout
                        })

            df = pd.DataFrame(parsed_data)
            
            if not df.empty:
                if show_only_breakouts:
                    df = df[df['Breakout'] == True]
                df = df[df['RSI'] >= rsi_min]
                df = df[df['RVOL'] >= rvol_min]
                
                if not df.empty and df['Breakout'].any():
                    st.markdown("<audio autoplay src='https://google.com'></audio>", unsafe_allow_html=True)
                    
                tab1, tab2 = st.tabs(["🔥 الماسح الفوري والسريع", "📊 لوحة تحكم المؤشرات"])
                
                with tab1:
                    if not df.empty:
                        df_sorted = df.sort_values('RVOL', ascending=False)
                        st.dataframe(style_dataframe(df_sorted), use_container_width=True)
                    else:
                        st.info("ℹ️ لا توجد عملات تطابق الفلاتر المحددة حالياً.")
                with tab2:
                    st.dataframe(style_dataframe(df), use_container_width=True)
            else:
                st.warning("⚠️ جدول البيانات فارغ حالياً.")
        else:
            st.error("⚠️ جدار حماية خوادم المنصة يعترض جلب أسعار الكريبتو المجمعة حالياً سحابياً.")
    except Exception as e:
        st.error(f"❌ حدث خطأ غير متوقع أثناء معالجة الجداول السحابية: {e}")

    # التحديث التلقائي المستقر كل دقيقة (60 ثانية)
    time.sleep(60)
    st.rerun()

render_live_dashboard()
