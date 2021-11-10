from operator import le
import unittest
from SPM7.app import lesson
from app import Administrator, Employee, Learner, Trainer, Course, Classes, Lesson, Quiz, Quizscore, QuestionTrueFalse
 
#Daniel
class TestEmployee(unittest.TestCase):
    def testemployee(self):
        employee = Employee(StaffID = 1, Name = 'Henry loh', Username = 'hen', Email = 'henlow@gmail.com', 
        CurrentDesignation = 'Hr', Department ='hr', ContactNo = '90227823', Role = 'Administrator')
        self.assertEqual(employee.to_dict(), {
            'StaffID' : 1,
            'Name' : 'Henry loh',
            'Username' : 'hen',
            'Email' : 'henlow@gmail.com',
            'CurrentDesignation' : 'Hr',
            'Department' : 'hr',
            'ContactNo' : '90227823',
            'Role' : 'Administrator'
        })
         
        
#Bernice
class TestLearner(unittest.TestCase):
    def testlearner(self):
        learner = Learner(StaffID = 3, Name = 'Constance Tan', Username = 'cons', Email = 'constan@gmail.com',
        CurrentDesignation = 'Engineer', Department = 'Learning', ContactNo = '92130843',CompletedCourses = 'IS214')
        self.assertEqual(learner.to_dict(), {
            'StaffID' : 3,
            'id' : None,
            'Name' : 'Constance Tan',
            'Username' : 'cons',
            'Email' : 'constan@gmail.com',
            'CurrentDesignation' : 'Engineer',
            'Department': 'Learning',
            'ContactNo' : '92130843',
            'CompletedCourses' : 'IS214',
            'CoursesAssigned': None,
            'CoursesEnrolled': None,
            'Role': None
                       
        })

#Terence
class TestTrainer(unittest.TestCase):
    def testtrainer(self):
        trainer = Trainer(StaffID = 2, Name = 'Roger Ng', Username = 'Rog', Email = 'Rogng@gmail.com',
        CurrentDesignation = 'Senior Engineer', Department = 'Training', ContactNo = '82329832', coursesTeaching = 'IS212 Software Project Management G2')
        self.assertEqual(trainer.to_dict(), {
            'StaffID' : 2,
            'id' : None,
            'Name' : 'Roger Ng',
            'Username' : 'Rog',
            'Email' : 'Rogng@gmail.com',
            'CurrentDesignation' : 'Senior Engineer',
            'Department': 'Training',
            'ContactNo' : '82329832',
            'coursesTeaching' : 'IS212 Software Project Management G2',
            'Role': None
        })

#Terence
class TestCourse(unittest.TestCase):
    def testcourse(self):
        course = Course(courseID = 1, courseName = 'Software Project Management', courseDesc = 'agile methods',
        preRequisites = 'NULL' ,classesID = 1)
        self.assertEqual(course.json(), {
            'courseID' : 1,
            'courseName' : 'Software Project Management',
            'courseDesc' : 'agile methods',
            'preRequisites' : 'NULL',
            'classesID' : 1
        })


#Qi Sheng
class Testclasses(unittest.TestCase):
    def testclasses(self):
        classes= Classes(classesID= 1, startDate="August 18 2021", startTime="8am", 
        endDate="November 5 2021", endTime="12pm", classesSize= 40, trainerAssigned="Roger Ng", currentEnrolled=0)
        self.assertEqual(classes.json(), {
            'classesID' : 1,
            'startDate' : 'August 18 2021',
            'startTime' : '8am',
            'endDate' : 'November 5 2021',
            "endTime" : '12pm',
            "classesSize" : 40,
            "trainerAssigned" : 'Roger Ng',
            "currentEnrolled" : 0
        })


    def test_IncreaseCurrentEnrolled(self):
        classes= Classes(classesID= 1, startDate="August 18 2021", startTime="8am", 
        endDate="November 5 2021", endTime="12pm", classesSize= 40, trainerAssigned="Roger Ng", currentEnrolled=0)
    
        self.assertEqual(classes.json(), {
            'classesID' : 1,
            'startDate' : 'August 18 2021',
            'startTime' : '8am',
            'endDate' : 'November 5 2021',
            "endTime" : '12pm',
            "classesSize" : 40,
            "trainerAssigned" : 'Roger Ng',
            "currentEnrolled" : 0
        })

        size = classes.IncreaseCurrentEnrolled(2)
        self.assertEqual(classes.currentEnrolled, 2)
        #self.assertEqual(size, 4)
        
#Daniel      
class TestLesson(unittest.TestCase):

  def testclasses(self):
      lesson = Lesson(lessonID=1, courseMaterial="Week1a-Introduction",classesID=1)

      self.assertEqual(lesson.json(), {
        'lessonID': 1,
        'courseMaterial': 'Week1a-Introduction',
        'classesID': 1
     
    })
      
#Qi Sheng  
class TestQuiz(unittest.TestCase):

  def testquiz(self):
      
      quiz = Quiz(quizID=1, quizDuration="15 mins",attemptNo="Unlimited",quizTitle="Week1 Quiz", quizDesc="No calculator", lessonID=1)

      self.assertEqual(quiz.json(), {
        'quizID': 1,
        'quizDuration': '15 mins',
        'attemptNo': 'Unlimited',
        'quizTitle':"Week1 Quiz",
        "quizDesc" : "No calculator",
        "lessonID":1
     
    })
      
#Bernice     
class TestQuestionTrueFalse(unittest.TestCase):

  def testQuestionTrueFalse(self):

      question = QuestionTrueFalse(
          qnID=1, qn="Software Project Management module is about coding" , ans="False",quizID=1)

      self.assertEqual(question.json(), {
          'qnID': 1,
          'qn': "Software Project Management module is about coding",
          'ans': "False",
          'quizID': 1,


      })
      
#Terence
class TestQuizscore(unittest.TestCase):
    
  def testQuizscore(self):
      
      quizscore = Quizscore(qsID=1, quizscore=0 ,quizID=1,learnerID=3)

      self.assertEqual(quizscore.json(), {
          'qsID': 1,
          'quizscore': 0,
          'quizID': 1,
        'learnerID':3,
      
     
    })
          

