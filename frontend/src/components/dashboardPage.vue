<template>
  <div class="dashboard-container">
    <h2>داشبورد</h2>
    <div class="user-info">
      <p><strong>نام کاربری:</strong> {{ user.username }}</p>
      <p><strong>ایمیل:</strong> {{ user.email }}</p>
    </div>
    <div class="section">
      <h3>آخرین مطالب</h3>
      <ul>
        <li v-for="post in recentPosts" :key="post.id">
          <h4>{{ post.title }}</h4>
          <p>{{ post.content }}</p>
          <small>{{ post.created_at }}</small>
        </li>
      </ul>
    </div>
    <div class="section">
      <h3>اطلاعیه‌ها</h3>
      <NotificationList />
    </div>
  </div>
</template>

<script>
import apiService from '@/apiService';
import NotificationList from '@/components/NotificationList';

export default {
  name: 'dashboardPage',
  components: {
    NotificationList,
  },
  data() {
    return {
      user: {},
      recentPosts: [],
    };
  },
  async created() {
    try {
      const response = await apiService.get('/profile/dashboard/');
      this.user = response.data.user;
      this.recentPosts = response.data.recent_posts;
    } catch (error) {
      console.error('Failed to fetch dashboard data:', error);
    }
  },
};
</script>

<style scoped>
.dashboard-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: right;
}

.user-info p {
  margin: 10px 0;
}

.section {
  margin-top: 30px;
}

.section h3 {
  margin-bottom: 15px;
}

.section ul {
  list-style-type: none;
  padding: 0;
}

.section ul li {
  background-color: #f9f9f9;
  margin-bottom: 10px;
  padding: 15px;
  border-radius: 5px;
}

.section ul li h4 {
  margin: 0;
}

.section ul li small {
  color: #888;
}
</style>
