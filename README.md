#SONYのICカードリーダーで音楽を再生したりするやつ
買うもの(これで動作確認)
SONY 非接触ICカードリーダー/ライター PaSoRi RC-S380 https://amzn.to/2QJIx1r
サンワサプライ NFCタグ https://amzn.to/2E1tzNn 

# インストール方法
- nfcpyのインストール
```
sudo pip install nfcpy
```

- python mpd-2. To install
Mopidyなどのmpdクライアント対応音楽サーバを導入しましょう。
```
pip install python-mpd2
```

- music-cardsインストール
```
git clone https://github.com/senyoltw/music-cards
cd music-cards/
```
はじめに実行 'python add_card.py' NFCに音楽URLを書き込む.
書き込み終えたら 'python box.py' でサービス動作

# サービス化
```
cd music-cards/
sudo cp musiccards.service /etc/systemd/system/musiccards.service
sudo systemctl daemon-reload
sudo systemctl start musiccards.service
sudo systemctl enable musiccards.service
```