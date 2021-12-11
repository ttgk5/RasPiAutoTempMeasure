import serial
import time
import datetime
import gsp as gs
 
COM="COM3"
bitRate=9600
temp_data_buff = []


dt_now = datetime.datetime.now()
 
ser = serial.Serial(COM, bitRate, timeout=0.1)


def main():

    global temp_data_buff

    #スプレッドシートのインデックスカウンタ 書き込みを始めたいロー番号を指定
    cell_cnt = 1

    try:
        while True:
        
            time.sleep(0.1)
            
            result = ser.read_all()

            if result.decode("utf-8") != "":
                temp_data_buff.append(result.decode("utf-8"))
                #print(result.decode("utf-8"), end="")
            
            if len(temp_data_buff) == 60:
                cell_cnt += 1

                for i in range(len(temp_data_buff)):
                    temp_data_buff[i] = (float(temp_data_buff[i].strip("\r\n")))
                

                print(temp_data_buff, sum(temp_data_buff), len(temp_data_buff))

                one_min_temp = sum(temp_data_buff)/len(temp_data_buff)

                
                #スプレッドシート書き込み
                now = str(dt_now.hour) + ":" + str(dt_now.minute) + ":" + str(dt_now.second)
                gs.worksheet.update_cell(cell_cnt, 1, now)
                time.sleep(0.1)
                gs.worksheet.update_cell(cell_cnt, 2, round(one_min_temp, 2))

                temp_data_buff = []
                
    

    except KeyboardInterrupt:
        print("ctrl+c")
        ser.close()

    except Exception as e:
        print(e)
        ser.close()


if __name__ == "__main__":
    main()