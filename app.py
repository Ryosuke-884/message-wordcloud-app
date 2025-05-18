import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from janome.tokenizer import Tokenizer
from io import BytesIO
from collections import Counter

st.title("メッセージ ワードクラウド自動生成アプリ")

st.markdown(
    """
    ### CSVファイルをアップロードしてください  
    <span style="color:red;">（カラム名は <b>gift_message</b> としてください）</span>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "CSVファイルを選択",
    type="csv"
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if 'gift_message' not in df.columns:
        st.error("gift_message というカラムがありません。")
    else:
        text = ' '.join(df['gift_message'].dropna().astype(str))
        tokenizer = Tokenizer()
        words = []
        for token in tokenizer.tokenize(text):
            part = token.part_of_speech.split(',')
            if part[0] == '名詞':
                if not (part[1] == '固有名詞' and part[2] == '人名'):
                    if len(token.base_form) > 1:
                        words.append(token.base_form)
        wc_text = ' '.join(words)

        wordcloud = WordCloud(
            font_path="fonts/NotoSansJP-Bold.otf",
            width=1600,
            height=800,
            background_color='white',
            colormap='tab20',
            font_step=1,
            prefer_horizontal=1.0,
            max_font_size=400
        ).generate(wc_text)

        st.subheader("ワードクラウド")
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

        img_buffer = BytesIO()
        wordcloud.to_image().save(img_buffer, format='PNG')
        img_buffer.seek(0)

        st.download_button(
            label="ワードクラウド画像をダウンロード",
            data=img_buffer,
            file_name="wordcloud.png",
            mime="image/png"
        )

        counter = Counter(words)
        st.subheader("頻出単語ランキング（上位30）")
        freq_df = pd.DataFrame(counter.most_common(30), columns=['単語', '出現回数'])
        st.dataframe(freq_df) 