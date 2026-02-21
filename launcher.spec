# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Bandcamp Player Launcher.
Builds the exe + _internal (Python and third-party deps only).
App files (bandcamp_pl_gui.py, modules/, Logo/, Color Scheme/, icon.ico, etc.) are NOT
bundled here; copy them into the dist root with copy_app_to_dist.py after building.
"""

block_cipher = None

from PyInstaller.utils.hooks import collect_dynamic_libs

# Ensure PyAudioWPatch's PortAudio/WASAPI binaries are bundled for audio-reactive visualizations
pyaudiowpatch_binaries = []
try:
    pyaudiowpatch_binaries = collect_dynamic_libs('pyaudiowpatch')
except Exception:
    pyaudiowpatch_binaries = []

a = Analysis(
    ['launcher.py'],
    pathex=[],
    binaries=pyaudiowpatch_binaries,
    # No app datas: app files live in exe root (copied by copy_app_to_dist.py after build).
    # _internal will contain only Python runtime and third-party dependencies.
    datas=[],
    hiddenimports=[
        'requests',  # Required for GitHub API calls
        'json',
        'pathlib',
        'subprocess',
        'threading',
        # Audio-reactive visualizations (WASAPI loopback)
        'numpy',
        'pyaudiowpatch',
        '_portaudiowpatch',
        # Standard library modules used by bandcamp_pl_gui.py
        'webbrowser',
        'tempfile',
        'hashlib',
        'html',
        're',
        'ctypes',
        'ctypes.wintypes',
        'urllib.request',
        'urllib.parse',
        'urllib.error',
        'tkinter',
        'tkinter.messagebox',
        # PyQt6 modules required by bandcamp_pl_gui.py
        # Even though launcher.py doesn't import them, the script does
        # PyInstaller needs these to bundle PyQt6 with the launcher
        'PyQt6',
        'PyQt6.QtWidgets',
        'PyQt6.QtCore',
        'PyQt6.QtGui',
        'PyQt6.QtWebEngineWidgets',
        'PyQt6.QtWebEngineCore',
        'PyQt6.QtNetwork',
        'qtawesome',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Exclude unnecessary modules to reduce size and scan time
        'matplotlib',
        'scipy',
        'pandas',
        'PIL._tkinter_finder',  # Not needed for launcher
        'test',
        'unittest',
        'pydoc',
        'doctest',
        'pydoc_data',
        'lib2to3',
        'distutils',
        # PyQt6 modules not used by this app (conservative list)
        # Note: QtWebEngine is still bundled (size is dominated by Chromium).
        'PyQt6.QtMultimedia',
        'PyQt6.QtMultimediaWidgets',
        'PyQt6.QtSql',
        'PyQt6.QtTest',
        'PyQt6.QtDesigner',
        # PyQt6 modules not used (no Bluetooth, positioning, sensors, serial, NFC, Quick/3D, charts)
        'PyQt6.QtBluetooth',
        'PyQt6.QtPositioning',
        'PyQt6.QtSensors',
        'PyQt6.QtSerialPort',
        'PyQt6.QtNfc',
        'PyQt6.QtQuick',
        'PyQt6.QtQuickWidgets',
        'PyQt6.Qt3DCore',
        'PyQt6.Qt3DRender',
        'PyQt6.Qt3DInput',
        'PyQt6.Qt3DLogic',
        'PyQt6.Qt3DExtras',
        'PyQt6.QtCharts',
        'PyQt6.QtDataVisualization',
        'PyQt6.QtScxml',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    [],
    name='BandcampPlayer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,  # Faster startup (avoid UPX decompression / AV overhead)
    runtime_tmpdir=None,  # Use default temp dir (faster than custom location for antivirus)
    console=False,  # Hide console window - launch silently
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',  # Use the same icon as the main app
    exclude_binaries=True,  # onedir: collect binaries separately (no onefile extraction)
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    name='BandcampPlayer'
)

