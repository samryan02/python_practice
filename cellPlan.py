data1 = float(input("please input prcie per GB: "))
talk1 = float(input("please Input price per Minute of call: "))
text1 = float(input("please input price per text: "))

data2 = float(input("please input prcie per GB of plan 2: "))
talk2 = float(input("please Input price per Minute of call of plan 2: "))
text2 = float(input("please input price per text of plan 2: "))

data_use = int(input("please input how much GB ypu plan to use : "))
talk_use = int(input("please Input how many minutes you plan to use: "))
text_use = int(input("please input how many texts you plan to use: "))




data1_price = data1*data_use
talk1_price = talk1*talk_use
text1_price = text1*text_use

data2_price = data2*data_use
talk2_price = talk2*talk_use
text2_price = text2*text_use



total_price1 = data1_price+talk1_price+text1_price
total_price2 = data2_price+talk2_price+text2_price

print(total_price1)
print(total_price2)

if(total_price1<total_price2):
    print("plan 1 will be cheaper")
else:
    print("plan 2 will ne cheaper")

