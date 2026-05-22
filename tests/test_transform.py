from transform.transform_data import transform_data

def test_transform():
    try:
        transform_data()
        assert True
    except:
        assert False
