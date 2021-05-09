from django.db import models


class Job(models.Model):
    id = models.IntegerField(primary_key=True, db_column='rowid', )
    title = models.TextField(db_column='jobTitle')
    company_name = models.TextField(db_column='companyName')
    category = models.TextField(db_column='category')
    office_location = models.TextField(db_column='officeLocation')
    deadline = models.TextField(db_column='deadline')
    description = models.TextField(db_column='jobDescription')
    requirement = models.TextField(db_column='requirement')
    welfare = models.TextField(db_column='welfare')
    company_logo = models.TextField(db_column='companyLogo')

    class Meta:
        db_table = "JOB"
