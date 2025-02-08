// src/apiService.js
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000', // Ensure this URL is correct
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = `Token ${token}`;
    }
    console.log('Axios request config:', config); // Add debugging log
    return config;
  },
  (error) => {
    console.error('Axios request error:', error); // Add debugging log
    return Promise.reject(error);
  }
);

const apiService = {
  post(url, data) {
    // Define the post method
    return apiClient.post(url, data);
  },
  getPosts(page = 1) {
    console.log('Fetching posts for page:', page); // Add debugging log
    return apiClient.get(`/api/posts/?page=${page}`);
  },
  // Add any other API methods here
};

export { apiClient };
export default apiService;
