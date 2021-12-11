import os
import serial
import time
import datetime
import gsp as gs
 

bitRate=9600
temp_data_buff = []

dt_now = datetime.datetime.now()

if os.name == "nt":
    COM="COM3"
    ser = serial.Serial(COM, bitRate, timeout=0.1)

elif os.name == "posix":
    COM="/dev/ttyACM0"
    ser = serial.Serial(COM, bitRate, timeout=0.1)

def main():

    global temp_data_buff

    #スプレッドシートのインデックスカウンタ 書き込みを始めたいロー番号を指定
    row_cnt = 1
    col_cnt = 1

    try:
        while True:
        
            time.sleep(0.1)
            

            result = ser.read_all()
            
            #debug
            """
            print(result, result.decode("utf-8"), type(result.decode("utf-8")), result.decode("utf-8").rstrip().isdigit() )
            if result == b'':
                print("void")
            else:
                print(float(result.decode("utf-8")))
            """

            if result != b'' and result.decode("utf-8").rstrip().isdigit() and result != "\n" and result != "\r":
                #print("appended")
                temp_data_buff.append(result.decode("utf-8"))
                #print(result.decode("utf-8"), end="")
            
            if len(temp_data_buff) == 720:
                row_cnt += 1
                if row_cnt == 31:
                    col_cnt = col_cnt + 2
                    row_cnt = 2

                for i in range(len(temp_data_buff)):
                    if temp_data_buff[i] != "\r\n" :
                        try:
                            temp_data_buff[i] = (float(temp_data_buff[i].strip("\r\n")))
                        except ValueError:
                            print("err")

                print(temp_data_buff, sum(temp_data_buff), len(temp_data_buff))
                
                dt_now = datetime.datetime.now()
                one_min_temp = sum(temp_data_buff)/len(temp_data_buff)

                
                #スプレッドシート書き込み
                now = str(dt_now.hour) + ":" + str(dt_now.minute) + ":" + str(dt_now.second)

                gs.worksheet.update_cell(row_cnt, col_cnt, now)
                time.sleep(0.1)
                gs.worksheet.update_cell(row_cnt, col_cnt+1, round(one_min_temp, 2))

                temp_data_buff = []
                
    

    except KeyboardInterrupt:
        print("ctrl+c")
        ser.close()

    except Exception as e:
        print(e)
        ser.close()


if __name__ == "__main__":
    main()
