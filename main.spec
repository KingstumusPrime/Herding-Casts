# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('images/*','images/Background_1.png'),('images/*','images/Background_2.png'),('images/*','images/background_3.png'),('images/*','images/ben.png'),('images/*','images/bulk.png'),('images/*','images/dario.png'),('images/*','images/goon_1.png'),('images/*','images/goon_2.png'),('images/*','images/goon_3.png'),('images/*','images/intro_1.png'),('images/*','images/intro_2.png'),('images/*','images/intro_3.png'),('images/*','images/intro_4.png'),('images/*','images/menu.png'),('images/*','images/pig_fam_Dad.png'),('images/*','images/pig_fam_pegga.png'),('images/*', 'images/pig_fam_Mom.png'),('images/*', 'images/pig_fam_storge.png'),('images/*','images/play_btn.png'),('images/*','images/player.png'),('images/rysu.png','images/'),('images/squige.png','images/'),('pixeloid-font/*', 'pixeloid-font/PixeloidSansBold-RpeJo.ttf'), ('','soundtrack.wav')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
