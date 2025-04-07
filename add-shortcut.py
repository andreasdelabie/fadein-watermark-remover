import sysconfig, winreg
from elevate import elevate

elevate()

python_scripts = sysconfig.get_path("scripts")
python_sitepackages = sysconfig.get_path("purelib")
location = winreg.HKEY_CLASSES_ROOT
shell = winreg.CreateKey(location, "SystemFileAssociations\\.pdf\\shell")
fadein_watermark_remover = winreg.CreateKey(shell, "fadein-watermark-remover")
command = winreg.CreateKey(fadein_watermark_remover, "command")

winreg.SetValueEx(fadein_watermark_remover, "", 0, winreg.REG_SZ, "Remove Fade In Watermark")
winreg.SetValueEx(fadein_watermark_remover, "Icon", 0, winreg.REG_SZ, f"{python_sitepackages}/fadein_watermark_remover/icon.ico")
winreg.SetValueEx(command, "", 0, winreg.REG_SZ, f'"{python_scripts}/fadein-watermark-remover.exe" "%1"')