import os
import unittest
import json
from flask_migrate import Config
from flask_sqlalchemy import SQLAlchemy
from werkzeug.datastructures import Headers
from models import setup_db,db_refresh_with_mock_data,Movies,Actors
from app import create_app
from auth import AuthConfig

class UdaCastingAgencyTestCase(unittest.TestCase):
    """This class represents the test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        self.new_movie = {
            'title': 'movie test1 ', 
            'release_date': '1991/01/01',
        }
        self.new_actor = {
            'name': 'actor test1 ',
            'age': '44',
            'gender': 'Male',
        }
        self.update_actor = {
            'name': 'actor test1 - updated ',
            'age': '44',
            'gender': 'Male',
        }

        self.casting_agency_assistant_token = AuthConfig.casting_agency_assistant_token
        self.casting_agency_director_token = AuthConfig.casting_agency_director_token
        self.casting_agency_producer_token = AuthConfig.casting_agency_producer_token
 
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            #self.db.create_all() # create all tables
    
    def tearDown(self):
        """Executed after reach test"""
        pass

#   #------------------ GET MOVIES TESTING --------------------------------------
    def test_get_movies(self):
        res=self.client().get('/movies/',headers = self.casting_agency_assistant_token)
        data= json.loads(res.data)
       
        self.assertEqual(res.status_code, 200)
        self.assertGreater(data['count'],0 )
        self.assertTrue(len(data['movies']))

    def test_get_movies_wrong_url_404(self):
        res=self.client().get('/movies1123/')
        self.assertEqual(res.status_code, 404)

    def test_get_movies_no_auth_401(self):
        res=self.client().get('/movies/')
        self.assertEqual(res.status_code, 401)

# #------------------ GET ACTORS TESTING --------------------------------------
    def test_get_actors(self):
        res=self.client().get('/actors/',headers = self.casting_agency_assistant_token)
        data= json.loads(res.data)
        #print(data)
        self.assertEqual(res.status_code, 200)
        self.assertGreater(data['count'],0 )
        self.assertTrue(len(data['actors'])) 

    def test_get_actors_wrong_url(self):
        res=self.client().get('/actors1123/')
        self.assertEqual(res.status_code, 404)

    def test_get_movies_no_auth_401(self):
        res=self.client().get('/movies/')
        self.assertEqual(res.status_code, 401)


#   #------------------ DELETE TESTING --------------------------------------
    def test_delete_actor(self):
        id=1
        res=self.client().delete(f'/actor/{id}/',headers = self.casting_agency_director_token)
        data= json.loads(res.data)
        #print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_actor_id'], id)

    def test_delete_invalid_actor_404(self):
        id=11
        res=self.client().delete(f'/actor/{id}/',headers = self.casting_agency_director_token)
        data= json.loads(res.data)
        #print(data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    
    def test_delete_actor_no_auth_401(self):
        id=1
        res=self.client().delete(f'/actor/{id}/')
        self.assertEqual(res.status_code, 401)
        
    
    def test_delete_movie(self):
        id=1
        res=self.client().delete(f'/movies/{id}/',headers = self.casting_agency_producer_token)
        data= json.loads(res.data)
        #print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_movie_id'], id) 
  
    def test_delete_invalid_movie_404(self):
        id=11
        res=self.client().delete(f'/movies/{id}/',headers = self.casting_agency_producer_token)
        data= json.loads(res.data)
        #print(data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    
    def test_delete_movie_no_auth_401(self): 
        id=1
        res=self.client().delete(f'/movies/{id}/')
        self.assertEqual(res.status_code, 401)

#   #------------------ POST TESTING --------------------------------------
    def test_create_movie(self):
        res = self.client().post('/movies/',json = self.new_movie,headers = self.casting_agency_producer_token)
        data = json.loads(res.data)
        #print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_create_movie_no_json_body(self):
        res = self.client().post('/movies/',json = None,headers = self.casting_agency_producer_token)
        data = json.loads(res.data)
        #print(data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Request body not valid or found.')

    def test_create_movie_no_auth_401(self): 
        res = self.client().post('/movies/',json = self.new_movie)
        self.assertEqual(res.status_code, 401)


    def test_create_actor(self):
        res = self.client().post('/actors/',json = self.new_actor,headers = self.casting_agency_producer_token)
        data = json.loads(res.data)
        #print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_create_actor_no_json_body(self):
        res = self.client().post('/actors/',json = None,headers = self.casting_agency_producer_token)
        data = json.loads(res.data)
        #print(data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Request body not valid or found.')

    def test_create_actor_no_auth_401(self): 
        res = self.client().post('/actors/',json = self.new_actor)
        self.assertEqual(res.status_code, 401)

#------------------ PATCH TESTING --------------------------------------
    def test_update_actor(self):
        id=1
        res = self.client().patch(f'/actors/{id}/',json = self.update_actor,headers = self.casting_agency_producer_token)
        data = json.loads(res.data)
        #print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_update_actor_no_json_body(self):
        id=1
        res = self.client().patch(f'/actors/{id}/',json = None,headers = self.casting_agency_producer_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Request body not valid or found.')

    def test_update_actor_no_auth_401(self): 
        id=1
        res = self.client().patch(f'/actors/{id}/',json = self.update_actor)
        self.assertEqual(res.status_code, 401)

    def test_update_movie(self):
        id=1
        res = self.client().patch(f'/movies/{id}/',json = self.new_movie,headers = self.casting_agency_producer_token)
        data = json.loads(res.data)
        #print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_update_movie_no_json_body(self):
        id=1
        res = self.client().patch(f'/movies/{id}/',json = None,headers = self.casting_agency_producer_token)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Request body not valid or found.')
    
    def test_update_movie_no_auth_401(self): 
        id=1
        res = self.client().patch(f'/movies/{id}/',json = self.new_movie)
        self.assertEqual(res.status_code, 401)

if __name__ == "__main__":
    unittest.main()
 