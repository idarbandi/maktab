<!--
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
-->

<template>
  <div class="maktab-analytics-admin">
    <div v-if="isAdmin" class="admin-content">
      <h2>داشبورد آنالیز ادمین</h2>
      <p>نظارت و پیگیری تحلیل‌های مهم در اینجا.</p>
      <button @click="trackMaktabEvent">کلیک کنید!</button>
    </div>
    <div v-else class="access-denied">
      <h2>دسترسی غیرمجاز</h2>
      <p>شما مجوز لازم برای مشاهده این صفحه را ندارید.</p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { useGtag } from 'vue-gtag-next';

export default {
  name: 'MaktabAnalyticsAdmin',
  // کامپوننت داشبورد آنالیز ادمین برای پروژه مکتب
  computed: {
    ...mapGetters(['user']),
    isAdmin() {
      return this.user?.is_superuser || this.user?.is_staff;
    },
  },
  methods: {
    trackMaktabEvent(event) {
      // ردیابی رویداد کلیک با استفاده از Gtag
      const { event: gtagEvent } = useGtag();
      gtagEvent('button_click', {
        event_category: 'interaction',
        event_label: 'click_me_button',
        value: 1,
      });
    },
  },
};
</script>

<style scoped>
.maktab-analytics-admin {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f4f4f4;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  /* استایل‌دهی به بخش اصلی داشبورد آنالیز ادمین */
}

.admin-content {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  /* استایل‌دهی به بخش محتوای ادمین */
}

h2 {
  margin-bottom: 15px;
  color: #004d40;
  /* استایل‌دهی به تیتر ها */
}

p {
  margin-bottom: 20px;
  color: #666;
  /* استایل‌دهی به پاراگراف‌ها */
}

.analytics-button {
  padding: 10px 20px;
  background-color: #004d40;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  /* استایل‌دهی به دکمه آنالیز */
}

.analytics-button:hover {
  background-color: #00796b;
  /* استایل‌دهی دکمه در حالت هاور */
}

.access-denied {
  padding: 20px;
  /* استایل‌دهی به بخش دسترسی غیرمجاز */
}

.access-denied h2 {
  color: #d32f2f;
  /* استایل‌دهی به تیتر در بخش دسترسی غیرمجاز */
}

.access-denied p {
  color: #888;
  /* استایل‌دهی به پاراگراف در بخش دسترسی غیرمجاز */
}
</style>
