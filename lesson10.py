'''
>>> from my_app.models import Student, User, UserProfile, Course, BBoard, Category
>>> user = User.objects.first()
>>> user
<User: admin>
>>> user_profile = UserProfile.objects.create(user=user, birth_date="2024-01-01")
>>> user_profile
<UserProfile: UserProfile object (1)>
>>> user_profile.user
<User: admin>
>>> user_profile.user.username
'admin'
>>> user = User.objects.first()
>>> user.userprofile
<UserProfile: UserProfile object (1)>
>>> user.userprofile.birth_date
datetime.date(2024, 1, 1)
>>> course = Course(title="django")
>>> course.save()
>>> student1 = Student(name="test")
>>> student2 = Student(name="test2")
>>> course.students
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x000001A3AF555C40>
>>> course.students.all()
<QuerySet []>
>>> course.students.add(student1. student2)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'student2'
>>> course.students.add(student1, student2) 
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\SelinN\Documents\lesson\my_venv\Lib\site-packages\django\db\models\fields\related_descriptors.py", line 1253, in add
    self._add_items(
  File "C:\Users\SelinN\Documents\lesson\my_venv\Lib\site-packages\django\db\models\fields\related_descriptors.py", line 1513, in _add_items
    target_ids = self._get_target_ids(target_field_name, objs)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\SelinN\Documents\lesson\my_venv\Lib\site-packages\django\db\models\fields\related_descriptors.py", line 1429, in _get_target_ids
    raise ValueError(
ValueError: Cannot add "<Student: Student object (None)>": instance is on database "default", value is on database "None"
>>> student2.save()
>>> course.students.add(student1, student2)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\SelinN\Documents\lesson\my_venv\Lib\site-packages\django\db\models\fields\related_descriptors.py", line 1253, in add
    self._add_items(
  File "C:\Users\SelinN\Documents\lesson\my_venv\Lib\site-packages\django\db\models\fields\related_descriptors.py", line 1513, in _add_items
    target_ids = self._get_target_ids(target_field_name, objs)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\SelinN\Documents\lesson\my_venv\Lib\site-packages\django\db\models\fields\related_descriptors.py", line 1429, in _get_target_ids
    raise ValueError(
ValueError: Cannot add "<Student: Student object (None)>": instance is on database "default", value is on database "None"
>>> student1.save()
>>> student1       
<Student: Student object (2)>
>>> student2
<Student: Student object (1)>
>>> course.students.add(student1, student2)
>>> course.students.all()
<QuerySet [<Student: Student object (1)>, <Student: Student object (2)>]>
'''

