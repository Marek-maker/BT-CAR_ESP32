# BT-CAR_ESP32
Repo dokumentujúce môj boj so záľudnosťami SW - micropython a HW - BT-CAR od UNIZI.   
Zaoberám sa tu BT_CARom konkrétne jeho myslím 3. verziou. Táto verzia - teraz najnovšia - používa ako svoj "mozog" ESP32 - 32 bitový mikrokontrolér so slušnou pamäťou a výkonom na naše účely.  
Predchádzajúce BT-CARy používali tzv. puky - DPSku okrúhleho tvaru s mikrčipom pripájanú na BT-CAR cez zasúvateľné piny.  
Dnešný BT-CAR od pukov upustil a používa štandardný modul ESP32 obdížnikového tvaru.  

![BT-CAR](https://user-images.githubusercontent.com/59760649/285028540-6ee27923-f3c0-4cd5-87ff-93e0a5f4c457.jpg)

##  Dokumentácia   
Dokumentácia je písaná cez nástroj zvaný [mdBook](https://github.com/rust-lang/mdBook) <br> kompilujúci mark down súbory usporiadané do kapitolovej štruktúry na formáty ako napr. html.    
[MD súbory dokumentácie](./docs/)

## Zdrojový kód
Kód pre BT-CAR v jazyku micropython nájdete [tu](./src/)
