from dw.models import Job
import math

def in_range(lat1, lon1, lat2, lon2, radius):
    R = 6378.137 # radius of earth in km
    d_lat = lat1 * math.pi / 180 - lat2 * math.pi / 180
    d_long = lon1 * math.pi / 180 - lon2 * math.pi / 180

    a = math.sin(d_lat / 2) ** 2 + \
        math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180) * \
        math.sin(d_long / 2) ** 2
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c

    return d <= radius

def get_job(*, id: int):
    return Job.objects.filter(id=id).first()

def list_job(*, cat: str):
    return Job.objects.filter(category=cat).all()

def near_job(*, lat, long, radius):
    return [j for j in Job.objects.filter(lat__isnull=False)
            if in_range(lat, long, j.lat, j.long, radius)]