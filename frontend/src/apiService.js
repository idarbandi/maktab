// src/apiService.js
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api', // Replace with your Django server URL
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

export default {
  getPosts(page = 1) {
    return apiClient.get(`/posts?page=${page}`);
  },
};
