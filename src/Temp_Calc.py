from math import log

def TempCalc(AdcInput):     #ADCからの生データ
    B = 3380        #[K]
    T0 = 25 + 273   #[K]
    R0 = 10000      #25℃ 時のサーミスタ抵抗
    R1 = 10000      #分圧抵抗値
    Vref = 3.301    #ラズパイの3.3V出力値
    
    #サーミスタの抵抗値
    th_reg = ((Vref/(AdcInput*Vref)) -1) * R1
    
    #温度計算
    temp_deno = (log(th_reg/R0)/B) + (1/T0)
    temp = (1/temp_deno) - 273
    
    return temp


    