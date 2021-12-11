# AutoTempMeasure
ラズパイで温度を測定しよう！

## 環境
Raspberry Pi OS on Raspberry Pi 3B  
Arduino Uno  

## 概要
1分間の平均温度を測定して、Google SpreadSheetに自動で書き込みます。  
ADCが無かったため、Arduinoからシリアル通信で温度データを飛ばしているけども、ADCをつかって直接温度を測定しても◎  

## コードの流れ
1. Arduinoでサーミスタから温度測定  
2. シリアルで転送  
3. Pythonで読み取り、平均値をとってGoogle SpreadSheetに書き込み。

## リンク
[スプレッドシート](https://docs.google.com/spreadsheets/d/1S71xmmjHUmxaegW_N2LZJ0jZKmFUfjjunEJbR1styAo/edit?usp=sharing)

