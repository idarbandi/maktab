<!-- FilterSort.vue -->
<template>
    <div class="filter-sort">
      <div class="filters">
        <select v-model="selectedCategory" @change="applyFilters">
          <option value="">دسته‌بندی</option>
          <option v-for="category in categories" :key="category.id" :value="category.name">{{ category.name }}</option>
        </select>
        <select v-model="selectedTag" @change="applyFilters">
          <option value="">برچسب</option>
          <option v-for="tag in tags" :key="tag.id" :value="tag.name">{{ tag.name }}</option>
        </select>
        <select v-model="selectedSortBy" @change="applyFilters">
          <option value="date">تاریخ</option>
          <option value="popularity">محبوبیت</option>
        </select>
      </div>
      <ul>
        <li v-for="post in filteredPosts" :key="post.id">
          <h3>{{ post.title }}</h3>
          <p>{{ post.content }}</p>
          <small>{{ post.created_at }} - Likes: {{ post.like_count }}</small>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import apiService from '@/apiService';
  
  export default {
    name: 'FilterSort',
    data() {
      return {
        categories: [],
        tags: [],
        selectedCategory: '',
        selectedTag: '',
        selectedSortBy: 'date',
        filteredPosts: [],
      };
    },
    async created() {
      await this.fetchCategoriesAndTags();
      await this.applyFilters();
    },
    methods: {
      async fetchCategoriesAndTags() {
        try {
          const categoriesResponse = await apiService.get('/categories/');
          this.categories = categoriesResponse.data;
          const tagsResponse = await apiService.get('/tags/');
          this.tags = tagsResponse.data;
        } catch (error) {
          console.error('Failed to fetch categories and tags:', error);
        }
      },
      async applyFilters() {
        try {
          const response = await apiService.get('/posts/filter/', {
            params: {
              category: this.selectedCategory,
              tag: this.selectedTag,
              sort_by: this.selectedSortBy,
            },
          });
          this.filteredPosts = response.data;
        } catch (error) {
          console.error('Failed to fetch filtered posts:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .filter-sort {
    margin-bottom: 20px;
  }
  
  .filters {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
  }
  
  select {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    background-color: #f9f9f9;
    margin-bottom: 10px;
    padding: 15px;
    border-radius: 5px;
  }
  
  h3 {
    margin: 0;
  }
  
  small {
    color: #888;
  }
  </style>
  