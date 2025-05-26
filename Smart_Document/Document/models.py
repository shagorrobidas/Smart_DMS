from django.db import models


class University(models.Model):
    name = models.CharField(
        max_length=255
    )
    logo = models.ImageField(
        upload_to='university_logos/',
        blank=True,
        null=True
    )
    code = models.CharField(
        max_length=10,
        unique=True)
    location = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Program(models.Model):
    program_name = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )
    program_code = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )
    program_discription = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.program_name


class Department(models.Model):
    name = models.CharField(
        max_length=100,

    )
    code = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )
    short_name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(
        max_length=20,
        unique=True
    )
    intake = models.IntegerField(
        blank=True,
        null=True
    )
    section = models.IntegerField(
        blank=True,
        null=True
    )
    programs = models.ForeignKey(
        Program,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self):
        return self.name


class Position(models.Model):
    title = models.CharField(
        max_length=50
        )
    position_code = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class Instructor(models.Model):
    name = models.CharField(
        max_length=100
        )
    instructor_id = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(
        max_length=100
    )
    code = models.CharField(
        max_length=20,
        unique=True
    )

    def __str__(self):
        return self.title


class Template(models.Model):
    title = models.CharField(
        max_length=100
    )
    code = models.IntegerField()

    def __str__(self):
        return self.title


class Experiment(models.Model):
    exp_name = models.CharField(
        max_length=255
    )
    exp_no = models.IntegerField()

    def __str__(self):
        return self.exp_name


class Submission(models.Model):
    report_number = models.IntegerField()
    submission_date = models.DateField()
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    template = models.ForeignKey(
        Template,
        on_delete=models.CASCADE
    )
    experiment = models.ForeignKey(
        Experiment,
        on_delete=models.CASCADE
    )
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        default=1)

    def __str__(self):
        return f"Submission {
            self.report_number} by {
                self.student.name} in Course {
                    self.course.code} on {
                        self.submission_date}"
