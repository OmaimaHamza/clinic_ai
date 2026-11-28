"""Tests de base. Adaptez-les aux vraies fonctions de clinic_ai."""
import compileall
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent


def test_requirements_exists():
    assert (ROOT / "requirements.txt").exists()


def test_code_compiles():
    assert compileall.compile_dir(str(ROOT), quiet=1, rx=__import__("re").compile(r"(\.git|venv|\.venv)"))


def test_example():
    # Remplacez par : from votre_module import ma_fonction
    assert 1 + 1 == 2
