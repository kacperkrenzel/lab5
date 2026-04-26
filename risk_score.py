import pytest

def calculate_risk_score(age: int, cholesterol: int, max_heart_rate: int) -> float:
    if age < 0 or cholesterol < 0 or max_heart_rate <= 0:
        raise ValueError('All parameters must be positive.')

    score = age * 0.2 + cholesterol * 0.05 - max_heart_rate * 0.03
    return round(score, 2)

#Testy AI
def test_normal_values():
    assert calculate_risk_score(50, 200, 150) == round(50*0.2 + 200*0.05 - 150*0.03, 2)

def test_zero_values():
    assert calculate_risk_score(0, 0, 1) == round(0 + 0 - 1*0.03, 2)

def test_high_values():
    assert calculate_risk_score(100, 300, 200) == round(100*0.2 + 300*0.05 - 200*0.03, 2)

def test_negative_age():
    with pytest.raises(ValueError):
        calculate_risk_score(-1, 200, 150)

def test_negative_cholesterol():
    with pytest.raises(ValueError):
        calculate_risk_score(50, -10, 150)

def test_zero_heart_rate():
    with pytest.raises(ValueError):
        calculate_risk_score(50, 200, 0)


#Dodatkowy edge test 
def test_min_positive_heart_rate():
    result = calculate_risk_score(30, 180, 1)
    expected = round(30*0.2 + 180*0.05 - 1*0.03, 2)
    assert result == expected


"""
Walidacja danych wejściowych
Sprawdza, czy:
age (wiek) ≥ 0
cholesterol ≥ 0
max_heart_rate > 0
Jeśli którykolwiek warunek nie jest spełniony rzuca wyjątek ValueError.

Obliczenie wyniku (risk score)
Wzór:
score = age * 0.2 + cholesterol * 0.05 - max_heart_rate * 0.03
Wiek i cholesterol zwiększają ryzyko
Maksymalne tętno zmniejsza ryzyko

Zaokrąglenie wyniku
Wynik jest zaokrąglany do 2 miejsc po przecinku (round(score, 2))
"""
