@echo off
cmd /k "cd /d C:\Users\Wasiq Gilani\Desktop\Newton\env\Scripts & activate & cd /d  C:\Users\Wasiq Gilani\Desktop\Newton & locust -f locustfile.py --host https://dev.newton.co --csv=csv_files/output --headless -u 10 -r 10 --run-time 3s"
exit /B