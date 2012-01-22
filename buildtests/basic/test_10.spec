# -*- mode: python -*-

__testname__ = 'test_10'

a = Analysis([os.path.join(HOMEPATH,'support', '_mountzlib.py'),
              __testname__ + '.py'],
             pathex=['.'])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build', 'pyi.'+sys.platform, __testname__ + '.exe'),
          debug=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT( exe,
               a.binaries,
               strip=False,
               upx=False,
               name=os.path.join('dist', __testname__),)