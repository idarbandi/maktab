// store/notifications.js
import axios from 'axios';

const state = {
  notifications: [],
};

const getters = {
  allNotifications: (state) => state.notifications,
};

const actions = {
  async fetchNotifications({ commit }) {
    const response = await axios.get('http://127.0.0.1:8000/profile/notifications/');
    commit('setNotifications', response.data);
  },
};

const mutations = {
  setNotifications: (state, notifications) => (state.notifications = notifications),
};

export default {
  state,
  getters,
  actions,
  mutations,
};
