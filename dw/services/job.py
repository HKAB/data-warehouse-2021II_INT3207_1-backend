from dw.models import Job

def in_range(my_lat, my_long, job_lat, job_long, radius):
    return (job_lat - my_lat) ** 2 + (job_long - my_long) <= radius ** 2

def get_job(*, id: int):
    return Job.objects.filter(id=id).first()

def list_job(*, cat: str):
    return Job.objects.filter(category=cat).all()

def near_job(*, lat, long, radius):
    return [j for j in Job.objects.filter(lat__isnull=False)
            if in_range(lat, long, j.lat, j.long, radius)]