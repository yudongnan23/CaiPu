from datetime import datetime
import time

def timeexchange():
    import time
    time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    _time = datetime.strptime(time,'%Y-%m-%d %H:%M:%S')
    return _time



