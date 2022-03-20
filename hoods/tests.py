from django.test import TestCase
from .models import UserProfile,Post,NeighbourHood,Business
from django.contrib.auth.models import User
# Create your tests here.

class NeighbourhoodTest(TestCase):
  def setUp(self):
    self.new_admin=User.objects.create_superuser('francis','francis@gmail.com','123')
    self.new_neighbourhood=NeighbourHood(name='Kahawa',location='Nairobi',admin=self.new_admin)
    

  def test_instance(self):
    self.assertTrue(isinstance(self.new_admin,User))
 
  def test_create_neighbourhood(self):
    self.new_admin.save()
    self.new_neighbourhood.create_neighbourhood()
    self.assertTrue(len(NeighbourHood.objects.all())>0)

  def test_delete_neighbourhood(self):
    self.new_admin.save()
    self.new_neighbourhood.create_neighbourhood()
    self.assertTrue(len(NeighbourHood.objects.all())==0)

  def test_find_neighbourhood(self):
    self.new_admin.save()
    self.new_neighbourhood.create_neighbourhood()
    self.neighbourhood_result=NeighbourHood.find_neighbourhood(1)
    self.assertEqual(self.new_neighbourhood,self.neighbourhood_result)

  def test_update_neigbourhood(self):
    self.new_admin.save()
    self.new_neighbourhood.create_neighbourhood()
    self.neighbourhood_result=NeighbourHood.find_neighbourhood(1)
    self.neighbourhood_result.update_neighbourhood(name='Kahawa Wendani')
    self.updated_neighbourhood_result=NeighbourHood.find_neighbourhood(1)
    self.assertEqual(self.updated_neighbourhood_result.name,'Kahawa Wendani')

  def test_update_occupants(self):
    self.new_admin.save()
    self.new_neighbourhood.create_neighbourhood()
    self.neighbourhood_result=NeighbourHood.find_neighbourhood(1)

    self.neighbourhood_result.update_occupants()
    self.neighbourhood_result=NeighbourHood.find_neighbourhood(1)
    
    self.assertEqual(self.neighbourhood_result.occupants_count,0)

class BusinessTest(TestCase):
  '''
  Business test class to test the the methods for business model
  '''
  def setUp(self):
    self.new_admin=User.objects.create_superuser('francis','francis@gmail.com','123')
    self.new_neighbourhood=NeighbourHood(name='Kahawa',location='Nairobi',admin=self.new_admin)
    self.new_user=User(first_name='francis',last_name='g',username='francisg',email="francis@gmail.com",password='go4it')
    self.new_profile=UserProfile(name='francis githae',national_id='0000000',user=self.new_user,neighbourhood=self.new_neighbourhood,email='francisg@gmail.com')
    self.new_business=Business(name='Chicken platta',profile=self.new_profile,neighbourhood=self.new_neighbourhood,email='chickenplatta@gmail.com')
  
  def test_create_business(self):
    self.new_admin.save()
    self.new_user.save()
    self.new_profile.save()
    self.new_business.create_business()
    self.assertTrue(len(Business.objects.all())>0)

  def test_find_business(self):
    self.new_admin.save()
    self.new_user.save()
    self.new_profile.save()
    self.new_business.create_business()
    self.business_result=Business.find_business(1)
    self.assertTrue(isinstance(self.business_result,Business))

  def test_update_business(self):
    self.new_admin.save()
    self.new_user.save()
    self.new_profile.save()
    self.new_business.create_business()
    self.business_result=Business.find_business(1)
    self.business_updated=self.business_result.update_business(name='Chicken place')
    self.assertEqual(self.business_updated.name,'Chicken place')

  def delete_business(self):
    self.new_admin.save()
    self.new_user.save()
    self.new_profile.save()
    self.new_business.create_business()
    self.business_result=Business.find_business(1)
    self.business_result.delete_business()
    self.assertTrue(len(Business.objects.all())==0)
