<template>
  <div class="notifications">
    <div v-for="notification in allNotifications" :key="notification.id" class="notification">
      <p>{{ notification.message }}</p>
      <small>{{ notification.created_at }}</small>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'NotificationList',
  computed: {
    ...mapGetters(['allNotifications']),
  },
  methods: {
    ...mapActions(['fetchNotifications']),
  },
  created() {
    this.fetchNotifications();
  },
};
</script>

<style scoped>
.notifications {
  padding: 20px;
}
.notification {
  background: #f9f9f9;
  border: 1px solid #ddd;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
}
</style>
