"""
提供排程的方式固定在 9:00 ~ 13:30 分執行 , 每30秒執行一次
第二 單次執行( 13:31 分) 執行一次
套件: schedule
pip install schedule
"""
import schedule
import time

def run_every_5seconds():
    print("每 5秒執行一次")


#只是安排一個任務 
schedule.every(5).seconds.do(run_every_5seconds)

while True:
    #要求 schedule 每n單位 檢查一次是否有任務需要執行
    schedule.run_pending()
    time.sleep(1) 