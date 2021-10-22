from services.service import Service


def test_validation(serv):
    try:
        serv.add(1, "Alex", -1)
        raise ValueError("Negative group error")
    except:
        return


def test_add(serv):
    serv.add(1, "Mihai", 1)
    serv.add(2, "Andrei", 1)
    serv.add(3, "Alina", 2)
    try:
        serv.add(1, "Alex", 2)
        raise ValueError("Duplicate id error")
    except:
        return


def test_filter(serv):
    serv.filter(1)

    assert len(serv) == 1


def test_all():
    serv = Service()
    serv._students = []

    test_validation(serv)
    test_add(serv)
    test_filter(serv)
