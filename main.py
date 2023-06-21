import psutil
import time


def get_time_app(name_app):
    time_start = None
    time_execute = 0

    for process in psutil.process_iter(['name', 'create_time']):
        if process.info['name'] == name_app:
            prid = process.pid
            time_start = psutil.Process(prid).create_time()
            break

    if time_start is not None:
        time_execute = time.time() - time_start

    return time_execute


def count_time():
    app_name = "obs64.exe"
    time_execute = get_time_app(app_name)
    time_execute = (time_execute / 60)
    print(f"Tiempo de ejecucion de la app: {time_execute}")
    return time_execute



