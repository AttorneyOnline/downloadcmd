from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('downloadcmd.py', base=base)
]

setup(name='downloadcmd',
      version = '0.2',
      description = 'A script to download character files from webAO',
      options = dict(build_exe = buildOptions),
      executables = executables)
