# いっぺん来ぃまいうどん県
TwoGate Dev Camp 2023 Summer Team H

## How to use
LINE公式アカウントの実行方法です。

### 1. Download This Repository
Ngrokを使用してするため、ローカルにダウンロードします。

### 2. Run Ngrok
Ngrokを使用して、Djangoデフォルトの8000ポートを開放します。

Ngrok.exeを起動して、以下のコードを実行します。

※予め認証が必要です
```powershell
ngrok http 8000
```

### 3. Run Local Server
manage.pyがあるディレクトリでターミナルを開き、以下のコードを実行します。

※Pythonがインストールされている必要があります。
```powershell
python manage.py runserver
```

### 4. Edit LINE Official Account
LINE Developer Consoleよりアカウントへアクセスします。

Messaging APIのWebhook URLを{Ngrokで発行されたURL} + /line_bot/に設定します。

例）https://837f-126-161-1-107.ngrok-free.app/line_bot/

検証を押してもエラーが返されますが、動作します。

### 5. Edit Python URL File
/utils/templates/ngrok_url.pyの中にある変数「ngrok_url」の値をngrokで発行されたURLに変更します。
```python
def url():
    ngrok_url = "{ここの値を変更}"
    return ngrok_url
```

以上の手順でLINE公式アカウントを動作させられます。

## Features
 - うどん店舗検索
   - 県内のうどん店舗をエリアごとに検索
   - 検索結果を口コミ順に上位10店舗をカルーセルで表示
   - 店舗リストからワンタップでGoogle Mapへアクセス
 - うどんスタンプラリー
   - 位置情報送信で店舗ごとにスタンプを獲得可能
   - 獲得スタンプをWebサイトで一覧表示
 - 観光地検索
   - 気象庁APIを利用し、天気ごとに出力地を変更
   - 天気予報関係なく出力も可能
 - お土産検索
   - カテゴリーごとにお土産を検索
   - お土産販売元のECサイトから簡単に購入可能

## Caution
 - 有償メッセージは使用していないため、全機能無料メッセージの範囲内で利用可能です。
 - データは自動更新でないため、情報が古い場合があります。

ホームディレクトリ内に発表で使用したプレゼンファイルを設置しています。
[PowerPointファイル](https://github.com/TG-DevCamp-2023Summer-TeamH/Ippen-Kiimai-UDON-Ken/blob/main/TG-DevCamp.pptx)
