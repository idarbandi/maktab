<!--
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
-->

<template>
  <button @click="performMaktabLogout" class="maktab-logout-button">خروج</button>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'MaktabLogoutButton',
  methods: {
    ...mapActions(['logout']),
    async performMaktabLogout() {
      // اجرا کردن عمل لاگ‌اوت و هدایت به صفحه ورود
      await this.logout();
      this.$router.push('/login');
    },
  },
};
</script>

<style scoped>
.maktab-logout-button {
  background-color: #d32f2f;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  /* استایل‌دهی به دکمه خروج */
}

.maktab-logout-button:hover {
  background-color: #b71c1c;
  /* استایل‌دهی دکمه در حالت هاور */
}
</style>
