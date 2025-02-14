<!--
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
-->

<template>
  <div class="maktab-dashboard-container">
    <h2>داشبورد</h2>
    <div class="user-info">
      <p><strong>نام کاربری:</strong> {{ user.username }}</p>
      <p><strong>ایمیل:</strong> {{ user.email }}</p>
    </div>
    <div class="section">
      <h3>آخرین مطالب</h3>
      <ul>
        <li v-for="post in recentMaktabPosts" :key="post.id">
          <h4>{{ post.title }}</h4>
          <p>{{ post.content }}</p>
          <small>{{ post.created_at }}</small>
        </li>
      </ul>
    </div>
    <div class="section">
      <h3>اطلاعیه‌ها</h3>
      <MaktabNotificationList />
    </div>
  </div>
</template>

<script>
import apiService from '@/apiService';
import MaktabNotificationList from '@/components/NotificationList';

export default {
  name: 'MaktabDashboardPage',
  components: {
    MaktabNotificationList,
  },
  data() {
    return {
      user: {},
      recentMaktabPosts: [],
    };
  },
  async created() {
    // دریافت اطلاعات داشبورد هنگام ساخت کامپوننت
    try {
      const response = await apiService.get('/profile/dashboard/');
      this.user = response.data.user;
      this.recentMaktabPosts = response.data.recent_posts;
    } catch (error) {
      console.error('Failed to fetch dashboard data:', error);
    }
  },
};
</script>

<style scoped>
.maktab-dashboard-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: right;
  /* استایل‌دهی به بخش اصلی داشبورد */
}

.user-info p {
  margin: 10px 0;
  /* استایل‌دهی به اطلاعات کاربر */
}

.section {
  margin-top: 30px;
  /* استایل‌دهی به بخش‌های مختلف داشبورد */
}

.section h3 {
  margin-bottom: 15px;
  /* استایل‌دهی به تیتر های بخش‌ها */
}

.section ul {
  list-style-type: none;
  padding: 0;
  /* استایل‌دهی به لیست مطالب */
}

.section ul li {
  background-color: #f9f9f9;
  margin-bottom: 10px;
  padding: 15px;
  border-radius: 5px;
  /* استایل‌دهی به هر مطلب */
}

.section ul li h4 {
  margin: 0;
  /* حذف حاشیه از تگ h4 */
}

.section ul li small {
  color: #888;
  /* استایل‌دهی به تاریخ ایجاد مطلب */
}
</style>
