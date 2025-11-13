from django.db import models

# NOTA: Usamos 'managed = False' en todas las clases porque la BD ya existe.

class Classroom(models.Model):
    # PK Compuesta (building, room_number)
    building = models.CharField(primary_key=True, max_length=15)
    room_number = models.CharField(max_length=7)
    capacity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'classroom'
        unique_together = (('building', 'room_number'),)


class Department(models.Model):
    # PK Simple
    dept_name = models.CharField(primary_key=True, max_length=20)
    building = models.CharField(max_length=15)
    budget = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'department'


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=8)
    title = models.CharField(max_length=50)
    # FK a Department (on delete set null -> models.SET_NULL)
    dept_name = models.ForeignKey(Department, models.SET_NULL, db_column='dept_name', blank=True, null=True)
    credits = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course'


class Instructor(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=5) 
    name = models.CharField(max_length=20) 
    dept_name = models.ForeignKey(Department, models.SET_NULL, db_column='dept_name', blank=True, null=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'instructor'


class Section(models.Model):
    # PK Compuesta
    course = models.ForeignKey(Course, models.CASCADE, db_column='course_id', primary_key=True)
    sec_id = models.CharField(max_length=8)
    semester = models.CharField(max_length=6)
    year = models.IntegerField()
    
    # FK Compuesta a Classroom (El ORM usa la PK de Classroom, 'building')
    building = models.ForeignKey(Classroom, models.SET_NULL, db_column='building', blank=True, null=True)
    room_number = models.CharField(max_length=7, blank=True, null=True)
    time_slot_id = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'section'
        unique_together = (('course', 'sec_id', 'semester', 'year'),)


class Teaches(models.Model):
    # Tabla M2M (Instructor <-> Section) con PK Compuesta
    id = models.ForeignKey(Instructor, models.CASCADE, db_column='ID', primary_key=True)
    course = models.ForeignKey(Section, models.CASCADE, db_column='course_id')
    sec_id = models.CharField(max_length=8)
    semester = models.CharField(max_length=6)
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'teaches'
        unique_together = (('id', 'course', 'sec_id', 'semester', 'year'),)


class Student(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=5)
    name = models.CharField(max_length=20)
    dept_name = models.ForeignKey(Department, models.SET_NULL, db_column='dept_name', blank=True, null=True)
    tot_cred = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'student'


class Takes(models.Model):
    # Tabla M2M (Student <-> Section) con datos extra ('grade') y PK Compuesta
    id = models.ForeignKey(Student, models.CASCADE, db_column='ID', primary_key=True)
    course = models.ForeignKey(Section, models.CASCADE, db_column='course_id')
    sec_id = models.CharField(max_length=8)
    semester = models.CharField(max_length=6)
    year = models.IntegerField()
    grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'takes'
        unique_together = (('id', 'course', 'sec_id', 'semester', 'year'),)


class Advisor(models.Model):
    # Relación 1-a-1: s_ID es PK y FK a Student
    s = models.OneToOneField(Student, models.CASCADE, db_column='s_ID', primary_key=True)
    i = models.ForeignKey(Instructor, models.SET_NULL, db_column='i_ID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advisor'


class TimeSlot(models.Model):
    # PK Compuesta
    time_slot_id = models.CharField(primary_key=True, max_length=4)
    day = models.CharField(max_length=1)
    start_hr = models.IntegerField()
    start_min = models.IntegerField()
    end_hr = models.IntegerField()
    end_min = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'time_slot'
        unique_together = (('time_slot_id', 'day', 'start_hr', 'start_min'),)


class Prereq(models.Model):
    # Tabla M2M (Course <-> Course) con PK Compuesta (self-referencing)
    course = models.ForeignKey(Course, models.CASCADE, db_column='course_id', primary_key=True, related_name='main_course_set')
    prereq = models.ForeignKey(Course, models.CASCADE, db_column='prereq_id', related_name='prereq_set')

    class Meta:
        managed = False
        db_table = 'prereq'
        unique_together = (('course', 'prereq'),)
