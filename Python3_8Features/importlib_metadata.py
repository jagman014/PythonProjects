from importlib import metadata

print(metadata.version('pip'))

pip_metadata = metadata.metadata('pip')
print(list(pip_metadata))

print(pip_metadata['Home-page'])
print(pip_metadata['Requires-Python'])

print(len(metadata.files('pip')))

py_files = [p for p in metadata.files('realpython-reader') if p.suffix == '.py']
print(py_files)

init_path = py_files[0]
print(init_path.read_text())

print(metadata.requires('realpython-reader'))
