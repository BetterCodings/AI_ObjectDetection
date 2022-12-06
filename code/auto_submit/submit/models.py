from django.db import models
from account.models import Account # 몰루?

class Student(models.Model):
    ID= models.CharField(max_length=30,primary_key=True)
    name=models.CharField(max_length=10)
# class Class(models.Model):
#     day = models.IntegerField(default=0)
#     period = models.IntegerField(default=0)
#     ID =models.ForeignKey(Lecture,on_delete=models.CASCADE)
#     classroom=models.CharField(max_length=30)
    # class Meta:
    #     constraints= [models.UniqueConstraint(fields=["day","period","lID"],name="Class-unique")]
    # def get_object(self):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     lookup_url_kwarg = ("day","period",'ID')
    #     values = (self.request.data[kwarg] for kwarg in lookup_url_kwarg)
    #     filter_kwargs = dict(zip(lookup_url_kwarg, values))
    #     obj = get_object_or_404(queryset, **filter_kwargs)
    #     self.check_object_permissions(self.request, obj)
    #     return obj
class Lecture(models.Model):
    ID = models.CharField(max_length=30,primary_key=True)
    subject = models.CharField(max_length=30)
    pID = models.ForeignKey(Account,on_delete=models.CASCADE)
    sum = models.IntegerField(default=0)
    members = models.ManyToManyField(Student)

class Class(models.Model):
    day = models.IntegerField(default=0)
    period = models.IntegerField(default=0)
    lID =models.ForeignKey(Lecture,on_delete=models.CASCADE)
    classroom=models.CharField(max_length=30)


class Attendence(models.Model):
    date=models.DateTimeField('date published')
    lID =models.ForeignKey(Lecture,on_delete=models.CASCADE)
    attend=models.IntegerField(default=0)
    #image = models.ImageField(default='media/default_image.jpg')
    members = models.ManyToManyField(Student,through="Attendence_Student")
    def init_Attendence_Student(self):
        for student in self.lID.members.all():
            self.members.add(student)
        self.attend= len(self.lID.members.all())
        self.save()
    def set_count(self):
        a_s=Attendence_Student.objects.filter(aID=self,submit=True)
        self.attend=len(a_s)
        self.save()
    class Meta:
        constraints= [models.UniqueConstraint(fields=["date","lID"],name="Attendence-unique")]



class Attendence_Student(models.Model):
    aID=models.ForeignKey(Attendence,on_delete=models.CASCADE)
    sID=models.ForeignKey(Student,on_delete=models.CASCADE)
    submit = models.BooleanField(default=True)




