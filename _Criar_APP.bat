@ECHO OFF  
SET /P app=INFORME O NOME DO APP: 
IF "%app%"=="" GOTO Error 
ECHO CRIANDO O MODULO %app% 		
python manage.py startapp %app% 		
move %app% %CD%\bitcoin 
md %CD%\bitcoin\%app%\templates 
if not exist %CD%\bitcoin\core ( 		
python manage.py startapp core 
move core %CD%\bitcoin 
md %CD%\bitcoin\core\static 
md %CD%\bitcoin\core\static\css 
md %CD%\bitcoin\core\static\font-awesome 
md %CD%\bitcoin\core\static\fonts 
md %CD%\bitcoin\core\static\img 
md %CD%\bitcoin\core\static\js 
md %CD%\bitcoin\core\templates 
) 
GOTO End 
:Error 
ECHO ERRO: O NOME DO APP E OBRIGATORIO. 
:End 
pause 
