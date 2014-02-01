from mean_sightings import get_sightings

filename = 'sightings_tab_sm.csv'

def test_owl_is_correct():
    owlrec, owlmean = get_sightings(filename, 'Owl')
    assert owlrec == 2, 'Number of records for owl is wrong'
    assert owlmean == 17, 'Mean sightings for owl is wrong'

def test_Muskox_is_correct():
    muskrec, muskmean = get_sightings(filename, 'Muskox')
    assert muskrec == 2, 'Number of records for Muskox is wrong'
    assert muskmean == 25.5, 'Mean sightings for Muskox is wrong'

def test_animal_not_present():
    animrec, animmean = get_sightings(filename, 'NotPresent')
    print animrec, animmean
    assert animrec == 0, 'Animal missing should return zero records'
    assert animmean == 0, 'Animal missing should return zero mean'