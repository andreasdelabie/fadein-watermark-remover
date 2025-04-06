import sysconfig, winreg
from elevate import elevate

elevate()

python_scripts = sysconfig.get_path("scripts")
location = winreg.HKEY_CLASSES_ROOT
shell = winreg.CreateKey(location, "SystemFileAssociations\\.pdf\\shell")
fadein_watermark_remover = winreg.CreateKey(shell, "fadein-watermark-remover")
command = winreg.CreateKey(fadein_watermark_remover, "command")

winreg.DeleteValue(command, "")
winreg.DeleteValue(fadein_watermark_remover, "")

winreg.DeleteKey(command, "")
winreg.CloseKey(command)
winreg.DeleteKey(fadein_watermark_remover, "")
winreg.CloseKey(fadein_watermark_remover)