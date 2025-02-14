<!--
This file is part of the maktab project.
All rights reserved to idarbandi.
For more details, contact: darbandidr99@gmail.com
GitHub repository: https://github.com/idarbandi/maktab
-->

<template>
  <div class="maktab-filter-sort">
    <div class="filters">
      <select v-model="selectedCategory" @change="applyMaktabFilters">
        <option value="">دسته‌بندی</option>
        <option v-for="category in categories" :key="category.id" :value="category.name">{{ category.name }}</option>
      </select>
      <select v-model="selectedTag" @change="applyMaktabFilters">
        <option value="">برچسب</option>
        <option v-for="tag in tags" :key="tag.id" :value="tag.name">{{ tag.name }}</option>
      </select>
      <select v-model="selectedSortBy" @change="applyMaktabFilters">
        <option value="date">تاریخ</option>
        <option value="popularity">محبوبیت</option>
      </select>
    </div>
    <ul>
      <li v-for="post in filteredMaktabPosts" :key="post.id">
        <h3>{{ post.title }}</h3>
        <p>{{ post.content }}</p>
        <small>{{ post.created_at }} - لایک‌ها: {{ post.like_count }}</small>
      </li>
    </ul>
  </div>
</template>

<script>
import apiService from '@/apiService';

export default {
  name: 'MaktabFilterSort',
  data() {
    return {
      categories: [],
      tags: [],
      selectedCategory: '',
      selectedTag: '',
      selectedSortBy: 'date',
      filteredMaktabPosts: [],
    };
  },
  async created() {
    // دریافت دسته‌بندی‌ها و برچسب‌ها و اعمال فیلترها هنگام ساخت کامپوننت
    await this.fetchMaktabCategoriesAndTags();
    await this.applyMaktabFilters();
  },
  methods: {
    async fetchMaktabCategoriesAndTags() {
      // دریافت دسته‌بندی‌ها و برچسب‌ها از API
      try {
        const categoriesResponse = await apiService.get('/categories/');
        this.categories = categoriesResponse.data;
        const tagsResponse = await apiService.get('/tags/');
        this.tags = tagsResponse.data;
      } catch (error) {
        console.error('Failed to fetch categories and tags:', error);
      }
    },
    async applyMaktabFilters() {
      // اعمال فیلترها و دریافت پست‌های فیلتر شده از API
      try {
        const response = await apiService.get('/posts/filter/', {
          params: {
            category: this.selectedCategory,
            tag: this.selectedTag,
            sort_by: this.selectedSortBy,
          },
        });
        this.filteredMaktabPosts = response.data;
      } catch (error) {
        console.error('Failed to fetch filtered posts:', error);
      }
    },
  },
};
</script>

<style scoped>
.maktab-filter-sort {
  margin-bottom: 20px;
  /* استایل‌دهی به بخش فیلتر و مرتب‌سازی */
}

.filters {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
  /* استایل‌دهی به بخش فیلترها */
}

select {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  /* استایل‌دهی به فیلدهای انتخاب دسته‌بندی و برچسب */
}

ul {
  list-style-type: none;
  padding: 0;
  /* استایل‌دهی به لیست پست‌ها */
}

li {
  background-color: #f9f9f9;
  margin-bottom: 10px;
  padding: 15px;
  border-radius: 5px;
  /* استایل‌دهی به هر پست در لیست */
}

h3 {
  margin: 0;
  /* حذف حاشیه از تگ h3 */
}

small {
  color: #888;
  /* استایل‌دهی به تاریخ ایجاد و تعداد لایک‌ها */
}
</style>
