from kivy.deps import sdl2, glew
# -*- mode: python -*-

block_cipher = None


a = Analysis(['Graphics.py'],
             pathex=['C:\\Users\\Gilad\\Desktop\\New folder (3)\\rpgGame'],
             binaries=[],
             datas=[('grass.png','.'),('dekar_shit.png','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='DekarRPG',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\Gilad\\Downloads\\Fazie69-League-Of-Legends-Riven-Championship.ico')

		  
		  
