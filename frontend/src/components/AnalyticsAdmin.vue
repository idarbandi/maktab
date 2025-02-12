<template>
    <div class="analytics-admin">
      <div v-if="isAdmin" class="admin-content">
        <h2>Admin Analytics Dashboard</h2>
        <p>Monitor and track important analytics here.</p>
        <button @click="trackEvent" class="analytics-button">Track Event</button>
      </div>
      <div v-else class="access-denied">
        <h2>Access Denied</h2>
        <p>You do not have the necessary permissions to view this page.</p>
      </div>
    </div>
  </template>
  
  <script>
  import { mapGetters } from 'vuex';
  import { useGtag } from 'vue-gtag-next';
  
  export default {
    name: 'AnalyticsAdmin',
    computed: {
      ...mapGetters(['user']),
      isAdmin() {
        return this.user?.is_superuser || this.user?.is_staff;
      },
    },
    methods: {
      trackEvent() {
        const { event } = useGtag();
        event('button_click', {
          event_category: 'interaction',
          event_label: 'admin_analytics_button',
          value: 1,
        });
      },
    },
  };
  </script>
  
  <style scoped>
  .analytics-admin {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f4f4f4;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  
  .admin-content {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  h2 {
    margin-bottom: 15px;
    color: #004d40;
  }
  
  p {
    margin-bottom: 20px;
    color: #666;
  }
  
  .analytics-button {
    padding: 10px 20px;
    background-color: #004d40;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .analytics-button:hover {
    background-color: #00796b;
  }
  
  .access-denied {
    padding: 20px;
  }
  
  .access-denied h2 {
    color: #d32f2f;
  }
  
  .access-denied p {
    color: #888;
  }
  </style>
  