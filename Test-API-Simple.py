import pytest

def test_falla_1(driver):
    """Test que falla siempre"""
    assert False, "Test 1 falló"

def test_falla_2(driver):
    """Otro test que falla"""
    titulo = driver.title
    assert "FACEBOOK" in titulo, f"Título es: {titulo}"

def test_falla_3(driver):
    """Tercer test que falla"""
    assert 10 == 20, "10 no es igual a 20"