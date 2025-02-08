// store/index.js
import { createStore } from 'vuex';
import apiService, { apiClient } from '@/apiService'; // Import apiService and apiClient

const store = createStore({
  state: {
    token: localStorage.getItem('token') || '',
    user: {},
    status: '',
  },
  mutations: {
    auth_request(state) {
      state.status = 'loading';
    },
    auth_success(state, payload) {
      state.status = 'success';
      state.token = payload.token;
      state.user = payload.user || {}; // Default to an empty object if user is undefined
    },
    auth_error(state) {
      state.status = 'error';
    },
    logout(state) {
      state.status = '';
      state.token = '';
      state.user = {};
    },
  },
  actions: {
    async login({ commit }, user) {
      commit('auth_request');
      console.log('Login action called with user:', user); // Debugging log
      try {
        const response = await apiService.post('/dj-rest-auth/login/', user);
        console.log('Login response:', response); // Debugging log

        // Ensure response.data contains the expected properties
        const token = response.data.key; // Check if `response.data.key` exists
        if (!token) {
          throw new Error('Invalid response format'); // Throw error if properties are missing
        }

        localStorage.setItem('token', token);
        apiClient.defaults.headers.common['Authorization'] = `Token ${token}`; // Set token on apiClient
        commit('auth_success', { token, user: {} }); // Pass an empty object for user
      } catch (error) {
        commit('auth_error');
        localStorage.removeItem('token');
        console.error('Login error:', error); // Debugging log
        throw error;
      }
    },
    async register({ commit }, user) {
      commit('auth_request');
      console.log('Register action called with user:', user); // Debugging log
      try {
        const response = await apiService.post('/dj-rest-auth/registration/', user);
        console.log('Registration response:', response); // Debugging log

        // Ensure response.data contains the expected properties
        const token = response.data.key; // Check if `response.data.key` exists
        if (!token) {
          throw new Error('Invalid response format'); // Throw error if properties are missing
        }

        localStorage.setItem('token', token);
        apiClient.defaults.headers.common['Authorization'] = `Token ${token}`; // Set token on apiClient
        commit('auth_success', { token, user: {} }); // Pass an empty object for user
      } catch (error) {
        commit('auth_error');
        localStorage.removeItem('token');
        console.error('Registration error:', error); // Debugging log
        throw error;
      }
    },
    logout({ commit }) {
      commit('logout');
      localStorage.removeItem('token');
      delete apiClient.defaults.headers.common['Authorization']; // Delete token from apiClient
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.token,
    authStatus: (state) => state.status,
    user: (state) => state.user,
  },
});

export default store;
