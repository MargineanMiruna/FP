from logic.solution import ersatz


def test_ersatz():
    assert ersatz('Fisch', 'Hund', debug=True) == 'Ersetzt Fisch durch Hund an 1 Stellen.'
    assert ersatz('Mensch', 'Hund', debug=True) == 'Das Wort kommt in dem Text nicht vor und konnte nicht ersetzt werden.'
