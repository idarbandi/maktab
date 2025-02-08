<template>
  <div class="auth-container">
    <div class="auth-card">
      <h2>ثبت نام</h2>
      <form @submit.prevent="submitRegistration">  <!-- Changed method name -->
        <div class="input-group">
          <input type="text" v-model="username" placeholder="نام کاربری" required />
        </div>
        <div class="input-group">
          <input type="email" v-model="email" placeholder="ایمیل" required />
        </div>
        <div class="input-group">
          <input type="password" v-model="password1" placeholder="رمز عبور" required />
        </div>
        <div class="input-group">
          <input type="password" v-model="password2" placeholder="تایید رمز عبور" required />
        </div>
        <button type="submit" class="auth-button">ثبت نام</button>
        <p v-if="error" class="error-message">{{ errorMessage }}</p>
      </form>
    </div>
  </div>
</template>

<!-- Correct RegisterForm.vue methods section -->
<script>
import { mapActions } from 'vuex';

export default {
  name: 'RegisterForm',
  data() {
    return {
      username: '',
      email: '',
      password1: '',
      password2: '',
      error: false,
      errorMessage: ''
    };
  },
  methods: {
    ...mapActions(['register']),
    async submitRegistration() {  // Changed method name
      if (this.password1 !== this.password2) {
        this.error = true;
        this.errorMessage = 'Passwords do not match';
        return;
      }
      try {
        await this.register({
          username: this.username,
          email: this.email,
          password1: this.password1,
          password2: this.password2
        });
        this.$router.push('/');
      } catch (error) {
        this.error = true;
        this.errorMessage = 'Registration failed. Please try again.';
        console.error('Registration error:', error);
      }
    }
  }
};
</script>

<style scoped>
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}

.auth-card {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 300px;
}

.auth-card h2 {
  margin-bottom: 20px;
  color: #004d40;
}

.input-group {
  margin-bottom: 15px;
}

.input-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.auth-button {
  width: 100%;
  padding: 10px;
  background-color: #004d40;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.auth-button:hover {
  background-color: #00796b;
}

.error-message {
  margin-top: 10px;
  color: red;
}
</style>
