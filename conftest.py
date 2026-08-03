"""Makes the repository root importable so tests can `import algorithms`.

pytest prepends the directory containing the root conftest.py to sys.path, so
this file existing is enough - it needs no contents beyond this note.
"""
