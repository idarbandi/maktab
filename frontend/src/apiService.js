// src/apiService.js
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000/api', // Updated to use 127.0.0.1 instead of localhost
  withCredentials: false,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }
});

apiClient.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers['Authorization'] = `Token ${token}`;
  }
  console.log('Axios request config:', config); // Debugging log
  return config;
}, error => {
  console.error('Axios request error:', error); // Debugging log
  return Promise.reject(error);
});

export default {
  getPosts(page = 1) {
    console.log('Fetching posts for page:', page); // Debugging log
    return apiClient.get(`/posts/?page=${page}`);
  }
};
