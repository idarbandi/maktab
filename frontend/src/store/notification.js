/*
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
*/

import axios from 'axios';

const state = {
  maktabNotifications: [], // تغییر نام به شکل اختصاصی
};

const getters = {
  allMaktabNotifications: (state) => state.maktabNotifications, // تغییر نام به شکل اختصاصی
};

const actions = {
  async fetchMaktabNotifications({ commit }) {
    // دریافت اطلاعیه‌ها از API
    const response = await axios.get('http://127.0.0.1:8000/profile/notifications/');
    commit('setMaktabNotifications', response.data);
  },
};

const mutations = {
  setMaktabNotifications: (state, notifications) => (state.maktabNotifications = notifications), // تغییر نام به شکل اختصاصی
};

export default {
  state,
  getters,
  actions,
  mutations,
};
