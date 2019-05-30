# music-cards(nfcpy)
Write playlist,albums,etc... to NFC tags, Read playlist,albums,etc... from NFC tags. And play it.  

```
NFC tag set.      -> play music.
NFC tag released. -> pause music.
Same NFC tag set. -> play music. From the time of pause.
Another tag set.  -> clear queue. and play music.
```

https://youtu.be/s8S5DVblT0k

need to buy  
- NFC read/write device(Work with nfcpy)  
- NFC tags(read/write)

#NFCタグにプレイリストを書き込んで、それで音楽を再生するやつ  
必要なもの(以下で動作確認済み)  
- SONY 非接触ICカードリーダー/ライター PaSoRi RC-S380 https://amzn.to/2QJIx1r
- サンワサプライ NFCタグ https://amzn.to/2E1tzNn

# How to install
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
If you want use spotify and spotify:playlist,
Execute the command in the next step
```
git clone https://github.com/kingosticks/mopidy-spotify
cd mopidy-spotify
git checkout fix/web-api-playlists-v2
sudo python2 setup.py build install
reboot
```

- music-cards install
```
git clone https://github.com/senyoltw/music-cards
```

# How to USE

```
#ClIでNFCに音楽URLを書き込む. CLI Write [musiclist] to NFC tags.
cd music-cards/
sudo python add_card.py  
#mpc add [musiclist] で再生キューにいれられるものは大丈夫。
#Working with mpc add [musiclist]. ex. spotify:playlist:37i9dQZF1DWUpdd1oGKt2o

#Read NFC tags. and Play. NFCの読み込みと再生確認。
sudo python box.py
```
# Daemonization
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
sudo pip install flask
cd music-cards/
sudo cp musiccardshttp.service /etc/systemd/system/musiccardshttp.service
sudo systemctl daemon-reload
sudo systemctl start musiccardshttp.service
sudo systemctl enable musiccardshttp.service

#and acsess http://[your IP]:5000
```

