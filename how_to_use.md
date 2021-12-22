## 仕様
- 対応アプリ : LEGO® Education SPIKE™ v.1.3.5 (以下SPIKEアプリと呼ぶ)
- 対応ハブOS : 3.0.22
- 対応言語 : Python
- 穴間距離 : 4×4(stud)
- 大きさ(基板サイズ) : 42×42×9(mm)
- 大きさ(ソケット含む) : 42×42×17(mm)

## ライブラリのインストール方法
1. SPIKEアプリで新しいプロジェクトを作成
2. ```touchsensorarray_send.py```に書かれているプログラムをコピー
3. 1.で作成したプロジェクトにペースト
4. プログラムの実行
5. SPIKEが自動的に再起動

## ライブラリの使い方
- ライブラリのサンプルプログラムは```touch_sensor_array_example.py```に記載している

### ライブラリの読み込み
- ```from projects.touch_sensor_array import TouchSensorArray```によってインストールしたライブラリを読み出すことができる

### SIPKEプライムとタッチセンサの接続
図のように接続を行う
図の番号がタッチセンサのポート番号となる
<div align="center">
<img src="https://user-images.githubusercontent.com/42668499/147165235-5bf6cc65-e6c9-4947-8e54-9cf64f8cb1c5.png" width="650">
</div>

### ポートの指定
- ```touch = TouchSensorArray("E")```によってポート(A~F)を指定し、オブジェクトを定義する
- 上記の```touch```にあたるオブジェクト名は任意

### 関数の仕様
- 全ての関数は```ポートの指定```で定義したオブジェクトのメソッドとして読み込む

1. confirm_connection()
    - データを取得できているか確認するための関数
    - 引数
        - try_num : int データ取得のトライ回数
            - default : 10
        - delay_time : float データ再取得の間隔 [s]
            - default : 0.02
    - 返り値 
        - bool データ取得の可否

2. get_data_all()
    - 全てのセンサー値データを取得するための関数
    - 引数
        - data_set_num : int 1組とみなすデータの個数
            - default : 4
        - try_num : int データ取得のトライ回数
            - default : 10
        - delay_time : float データ再取得の間隔 [s]
            - default : 0.02
    - 返り値
        - list 1組の最新データセット

3. get_data_port()
    - 指定したポートのセンサー値データを取得する 
    - 引数
        - port num : list 取得するセンサーのポート番号
            - default : [1,2,3,4]
        - data set num : int 1組とみなすデータの個数
            - default : 4
        - try num : int データ取得のトライ回数
            - default : 10
        - delay time : float データ再取得の間隔 [s]
            - default : 0.02
    - 返り値
        - list 1組の最新データセット
