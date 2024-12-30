<template>
  <div class="login-container">
    <h1 class="login-title">Login</h1>

    <!-- Login form -->
    <form @submit.prevent="login" class="login-form">
      <!-- Username input field -->
      <input v-model="username" type="text" class="login-input" placeholder="Username" required />

      <!-- Password input field -->
      <input v-model="password" type="password" class="login-input" placeholder="Password" required />

      <!-- Submit button -->
      <button type="submit" class="login-button">Login</button>
			<p v-if="message" class="error">{{ message }}</p>
    </form>
  </div>
</template>

<script>
import axiosInstance from '../axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      message: ''
    };
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

        const userProfileResponse = await axiosInstance.get('/api/user-profile/');
        const userProfile = userProfileResponse.data;

        // Redirect based on user type
        if (userProfile.nutritionist) {
          this.$router.push('/clients-nutritionist');
        } else {
          this.$router.push('/available-nutritionists');
        }
      } catch (error) {
				this.message = 'Invalid credentials. Please try again.';
        // Handle login error, display error messages, etc.
      }
    }
  }
};
</script>

<style scoped>
/* Container styling */
.login-container {
  max-width: 400px;
  margin: 100px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
}

/* Title styling */
.login-title {
  margin-bottom: 20px;
  font-size: 24px;
  color: #333;
}

/* Form styling */
.login-form {
  display: flex;
  flex-direction: column;
}

/* Input fields styling */
.login-input {
  margin-bottom: 15px;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  outline: none;
  box-sizing: border-box;
  width: 100%;
}

.login-input:focus {
  border-color: #007bff;
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}

/* Button styling */
.login-button {
  padding: 10px;
  font-size: 16px;
  font-weight: bold;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  width: 100%;
}

.login-button:hover {
  background-color: #0056b3;
}

.error {
  color: red;
  margin-top: 10px;
  font-size: 14px;
  text-align: center;
}
</style>
