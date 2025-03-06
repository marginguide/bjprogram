import datetime, os, sqlite3, random
import win32com.client
import pandas as pd

def create_daily_schedule():

    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')
    task_def = scheduler.NewTask(0)

    # 트리거 종류
    TASK_TRIGGER_DAILY = 2
    trigger = task_def.Triggers.Create(TASK_TRIGGER_DAILY)
    start_time = datetime.datetime.combine(datetime.datetime.now().date(), datetime.time(7, 00))
    trigger.StartBoundary = start_time.isoformat()

 
    # 태스크 생성 생성
    TASK_ACTION_EXEC = 0
    action = task_def.Actions.Create(TASK_ACTION_EXEC)

    action.Path ="C:\\Program Files (x86)\\cafe24_order\\muscle.exe"

    # 파라미터 세팅
    task_def.RegistrationInfo.Description = 'Muscle_ordering'
    task_def.Settings.Enabled = True
    task_def.Settings.StartWhenAvailable = True  # 부팅 후 가능하면 실행
    task_def.Principal.RunLevel = 1 # 최고 레벨로 진행



    # If task already exists, it will be updated
    TASK_CREATE_OR_UPDATE = 6 # 기존 같은 이름의 태스크가 있다면 업데이트
    TASK_LOGON_NONE = 0

    try:
        root_folder.RegisterTaskDefinition(
            'muscleguards_cafe24',  # Task name
            task_def,
            TASK_CREATE_OR_UPDATE,
            '',  # No user
            '',  # No password
            TASK_LOGON_NONE
        )
    except:
        pass
    
