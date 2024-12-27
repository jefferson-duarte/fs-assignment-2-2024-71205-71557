<template>
  <div>
      <h1>Login</h1>
      <!-- Login form -->
      <form @submit.prevent="login">
          <!-- Username input field -->
          <input v-model="username" type="text" placeholder="Username" required />
          <!-- Password input field -->
          <input v-model="password" type="password" placeholder="Password" required />
          <!-- Submit button -->
          <button type="submit">Login</button>
      </form>
  </div>
</template>

<script>
import axiosInstance from '../axios';

export default {
  data() {
      return {
          username: '',  // Username field bound to input
          password: ''   // Password field bound to input
      }
  },
  methods: {
      async login() {
          try {
              // Send login request to the backend
              const response = await axiosInstance.post('api/token/', {
                username: this.username,
                  password: this.password
              });

              // Store the access and refresh tokens in localStorage
              localStorage.setItem('accessToken', response.data.access);
              localStorage.setItem('refreshToken', response.data.refresh);

              // Redirect to the dashboard after successful login
              this.$router.push('/dashboard');
          } catch (error) {
              console.error("Login failed", error);
              // Handle login error, display error messages, etc.
          }
      }
  }
}
</script>
