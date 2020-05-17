import mh_z19

def read_all():
    co2 = tem = hu = -1

    try:
        data = mh_z19.read_all()
        co2 = data["co2"]
        tem = data["temperature"]
        hu = data["TT"]
    except:
        pass

    return co2, tem, hu
