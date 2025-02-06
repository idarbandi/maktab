<template>
  <div id="home-page">
    <header>
      <div class="logo">
        <img src="logo.png" alt="پروژه مکتب" />
      </div>
      <nav>
        <ul>
          <li><router-link to="/">خانه</router-link></li>
          <li><router-link to="/about">درباره ما</router-link></li>
          <li><router-link to="/resources">منابع آموزشی</router-link></li>
          <li><router-link to="/contact">تماس با ما</router-link></li>
        </ul>
      </nav>
    </header>
    <main>
      <section class="hero">
        <h1>به مکتب خوش آمدید</h1>
        <p>جامع‌ترین منابع آموزشی برای همه</p>
        <button class="cta-button">شروع کنید</button>
      </section>
      <section class="posts">
        <h2>آخرین مطالب</h2>
        <div class="post-grid">
          <div v-for="post in posts" :key="post.id" class="post-card">
            <h3>{{ post.title }}</h3>
            <p>{{ post.content }}</p>
          </div>
        </div>
      </section>
    </main>
    <footer>
      <p>حق نشر © 2025. تمامی حقوق محفوظ است.</p>
    </footer>
  </div>
</template>

<script>
import apiService from '@/apiService';

export default {
  name: 'HomePage',
  data() {
    return {
      posts: []
    };
  },
  created() {
    this.fetchPosts();
  },
  methods: {
    async fetchPosts() {
      try {
        const response = await apiService.getPosts();
        this.posts = response.data.results;
      } catch (error) {
        console.error('Failed to fetch posts:', error);
      }
    }
  }
};
</script>

<style scoped>
#home-page {
  font-family: 'Iran Sans', Tahoma, sans-serif;
  direction: rtl;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #004d40;
  padding: 10px 20px;
  color: white;
}

header .logo img {
  height: 50px;
}

nav ul {
  list-style-type: none;
  display: flex;
  gap: 20px;
}

nav ul li a {
  color: white;
  text-decoration: none;
  font-size: 16px;
}

main {
  padding: 20px;
}

.hero {
  text-align: center;
  background-color: #e0f7fa;
  padding: 40px 20px;
  margin-bottom: 20px;
}

.hero h1 {
  font-size: 36px;
  margin-bottom: 10px;
}

.hero p {
  font-size: 20px;
  margin-bottom: 20px;
}

.hero .cta-button {
  background-color: #004d40;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.hero .cta-button:hover {
  background-color: #00796b;
}

.posts {
  text-align: center;
}

.posts h2 {
  font-size: 24px;
  margin-bottom: 20px;
}

.post-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
}

.post-card {
  background-color: #f1f1f1;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

footer {
  background-color: #004d40;
  color: white;
  text-align: center;
  padding: 10px 0;
  margin-top: 40px;
}
</style>
