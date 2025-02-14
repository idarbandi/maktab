<!--
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
-->

<template>
  <div class="maktab-notifications">
    <div v-for="notification in allMaktabNotifications" :key="notification.id" class="notification">
      <p>{{ notification.message }}</p>
      <small>{{ notification.created_at }}</small>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'MaktabNotificationList',
  computed: {
    ...mapGetters(['allMaktabNotifications']),
  },
  methods: {
    ...mapActions(['fetchMaktabNotifications']),
  },
  created() {
    // فراخوانی دریافت اطلاعیه‌ها هنگام ساخت کامپوننت
    this.fetchMaktabNotifications();
  },
};
</script>

<style scoped>
.maktab-notifications {
  padding: 20px;
  /* استایل‌دهی به بخش اطلاعیه‌ها */
}
.notification {
  background: #f9f9f9;
  border: 1px solid #ddd;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
  /* استایل‌دهی به هر اطلاعیه */
}
</style>
