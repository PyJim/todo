from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task

class TaskViewSetTestCase(APITestCase):

    def setUp(self):
        """Setup the test data"""
        self.task_data = {'title': 'Test Task', 'description': 'A test task description'}
        self.task = Task.objects.create(**self.task_data)
        self.url = reverse('tasks')

    def test_get_all_tasks(self):
        """Test GET /tasks/ to fetch all tasks"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.task.title)

    def test_get_single_task(self):
        """Test GET /tasks/<id>/ to fetch a single task"""
        response = self.client.get(reverse('task', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)

    def test_get_single_task_not_found(self):
        """Test GET /tasks/<id>/ with a non-existing task"""
        response = self.client.get(reverse('task', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'], 'Task not found')

    def test_create_task(self):
        """Test POST /tasks/ to create a new task"""
        new_task_data = {'title': 'New Task', 'description': 'A new task to create'}
        response = self.client.post(self.url, new_task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], new_task_data['title'])
        self.assertEqual(response.data['description'], new_task_data['description'])

    def test_create_task_invalid(self):
        """Test POST /tasks/ with invalid data"""
        invalid_data = {'title': '', 'description': ''}  # Empty title and description
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_task(self):
        """Test PUT /tasks/<id>/ to update an existing task"""
        updated_data = {'title': 'Updated Task', 'description': 'Updated task description'}
        response = self.client.put(reverse('task', kwargs={'pk': self.task.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_data['title'])
        self.assertEqual(response.data['description'], updated_data['description'])

    def test_update_task_not_found(self):
        """Test PUT /tasks/<id>/ with a non-existing task"""
        updated_data = {'title': 'Updated Task', 'description': 'Updated task description'}
        response = self.client.put(reverse('task', kwargs={'pk': 999}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_task(self):
        """Test DELETE /tasks/<id>/ to delete an existing task"""
        response = self.client.delete(reverse('task', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Ensure the task is actually deleted
        response = self.client.get(reverse('task', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_task_not_found(self):
        """Test DELETE /tasks/<id>/ with a non-existing task"""
        response = self.client.delete(reverse('task', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
