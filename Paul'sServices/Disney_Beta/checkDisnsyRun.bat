@echo off
set _task=python.exe
set _svr=C:\Python27\python.exe    C:\Python27\Disney_Beta\DisneyGrabTickets.py
set _des=start.bat
:checkstart
for /f "tokens=5" %%n in ('qprocess.exe ^| find "%_task%" ') do (
 if %%n==%_task% (goto checkag) else goto startsvr
)

:startsvr
echo %time% 
echo ********����ʼ����********
echo �������������� %time% ,����ϵͳ��־ >> restart_service.txt
echo start %_svr% > %_des%
echo exit >> %_des%
start %_des%
set/p=.for /L %%i in (1 1 10) do set /p a=.nul
echo .
echo Wscript.Sleep WScript.Arguments(0) >%tmp%\delay.vbs 
cscript //b //nologo %tmp%\delay.vbs 10000 
del %_des% /Q
echo ********�����������********
goto checkstart

:checkag
echo %time% ������������,10���������.. 
echo Wscript.Sleep WScript.Arguments(0) >%tmp%\delay.vbs 
cscript //b //nologo %tmp%\delay.vbs 10000 
goto checkstart