# メッセージ ワードクラウド自動生成アプリ

## 概要

このアプリは、CSVファイル（カラム名: `gift_message`）をアップロードするだけで、
メッセージ内容のワードクラウドや頻出単語ランキング、利用シーンの推定を自動で可視化できるStreamlitアプリです。

- 個人名と思われる単語は自動で除外されます。
- ワードクラウド画像はダウンロード可能です。

## 使い方

1. このリポジトリをクローンまたはダウンロード
2. 必要なパッケージをインストール
   ```bash
   pip install -r requirements.txt
   ```
3. アプリを起動
   ```bash
   streamlit run app.py
   ```
4. ブラウザで表示される画面から、`gift_message`カラムを含むCSVファイルをアップロード

## デプロイ方法（Streamlit Community Cloud）

1. GitHubにこのフォルダをアップロード
2. [Streamlit Community Cloud](https://streamlit.io/cloud) にアクセスし、GitHub連携でデプロイ
3. `app.py`を指定して公開

## 注意事項
- CSVのカラム名は必ず `gift_message` としてください。
- 日本語ワードクラウドのため、Macの場合は `ヒラギノ角ゴシック` フォントを利用しています。
- 個人名は自動で除外されますが、完全な匿名化を保証するものではありません。 