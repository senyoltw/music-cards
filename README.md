# music-cards(nfc)
Write playlist,albums,etc... to NFC tags, Read playlist,albums,etc... from NFC tags. And play it.  

need to buy  
- NFC read/write device(Work with nfcpy)  
- NFC tags(read/write)

#NFCタグにプレイリストを書き込んで、それで音楽を再生するやつ  
必要なもの(以下で動作確認済み)  
- SONY 非接触ICカードリーダー/ライター PaSoRi RC-S380 https://amzn.to/2QJIx1r
- サンワサプライ NFCタグ https://amzn.to/2E1tzNn

# How to install インストール方法
- install nfcpy  
```
sudo pip install nfcpy
```

- install python-mpd2  
```
sudo pip install python-mpd2
```

- install music server(Can be controlled with mpd)    
ex. https://github.com/mopidy/mopidy  

- music-cards install
```
git clone https://github.com/senyoltw/music-cards
```

# How to USE 使い方

```
#ClIでNFCに音楽URLを書き込む. CLI Write [musiclist] to NFC tags.
cd music-cards/
sudo python add_card.py  
#mpc add [musiclist] で再生キューにいれられるものは大丈夫。
#mpc add [musiclist]. ex. spotify:playlist:37i9dQZF1DWUpdd1oGKt2o

#Read NFC tags. and Play. NFCの読み込みと再生確認。
sudo python box.py
```
# Daemonization サービス化
```
cd music-cards/
sudo cp musiccards.service /etc/systemd/system/musiccards.service
sudo systemctl daemon-reload
sudo systemctl start musiccards.service
sudo systemctl enable musiccards.service
```

NFCの書き込みもWEBで実行したい場合  
When you want to execute NFC writing on WEB
```
sudo sudo pip install flask
cd music-cards/
sudo cp musiccardshttp.service /etc/systemd/system/musiccardshttp.service
sudo systemctl daemon-reload
sudo systemctl start musiccardshttp.service
sudo systemctl enable musiccardshttp.service
```
and acsess http://[your pi IP]:5000

