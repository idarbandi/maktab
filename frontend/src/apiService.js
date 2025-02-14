/*
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
*/

import axios from 'axios';

const maktabApiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000', // Ensure this URL is correct
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

maktabApiClient.interceptors.request.use(
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

const maktabApiService = {
  post(url, data) {
    return maktabApiClient.post(url, data);
  },
  get(url) {
    return maktabApiClient.get(url);
  },
  getMaktabPosts(page = 1) {
    console.log('Fetching maktab posts for page:', page); // Add debugging log
    return maktabApiClient.get(`/api/posts/?page=${page}`);
  },
  getMaktabMainPagePosts(page = 1) {
    console.log('Fetching maktab main page posts for page:', page); // Add debugging log
    return maktabApiClient.get(`/api/posts/?page=${page}`); // Ensure this matches your API endpoint
  },
  getMaktabUserPosts(userId, page = 1) {
    console.log(`Fetching maktab posts for user ${userId} on page ${page}`); // Add debugging log
    return maktabApiClient.get(`/api/posts/?user=${userId}&page=${page}`);
  },
  getMaktabCategoriesAndTags() {
    return maktabApiClient.get('/api/categories/'); // Ensure this matches your API endpoint
  },
  getMaktabFilteredPosts(params) {
    console.log('Fetching filtered maktab posts', params); // Add debugging log
    return maktabApiClient.get('/api/posts/filter/', { params });
  },
  getMaktabUser() {
    return maktabApiClient.get('/dj-rest-auth/user/'); // Endpoint to fetch user information
  },
};

export { maktabApiClient };
export default maktabApiService;
