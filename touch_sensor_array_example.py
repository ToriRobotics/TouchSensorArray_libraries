import time
from projects.touch_sensor_array import TouchSensorArray #ライブラリの読み込み

touch = TouchSensorArray("E") #SPIKE側のポートを指定

while(1):
    
    #接続を確認する関数
    check = touch.confirm_connection()
    print(check)

    #指定したポートの値を取得する関数
    data_port = touch.get_data_port([4,1,3])
    print(data_port)

    #全てのポートの値を取得する関数
    data = touch.get_data_all()
    print(data)

    time.sleep(0.001)
        