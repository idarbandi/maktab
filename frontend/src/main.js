// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import VueGtag from 'vue-gtag-next';

createApp(App)
  .use(store)
  .use(router)
  .use(VueGtag, {
    property: {
      id: process.env.VUE_APP_GOOGLE_ANALYTICS_ID, // Replace with your Google Analytics Measurement ID
    },
  })
  .mount('#app');
