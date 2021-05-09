from dw.models import Job

def get_job(*, id: int):
    return Job.objects.filter(id=id).first()

def list_job(*, cat: str):
    return Job.objects.filter(category=cat).all()