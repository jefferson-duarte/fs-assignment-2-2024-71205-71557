<template>
  <div class="register-form">
    <h2>User Registration</h2>
    <form @submit.prevent="registerUser">
      <!-- First name field -->
      <div>
        <label for="first_name">First Name</label>
        <input type="text" v-model="user.first_name" id="first_name" required />
      </div>

      <!-- Last name field -->
      <div>
        <label for="last_name">Last Name</label>
        <input type="text" v-model="user.last_name" id="last_name" required />
      </div>

      <!-- Email field -->
      <div>
        <label for="email">Email</label>
        <input type="email" v-model="user.email" id="email" required />
      </div>

      <!-- Phone field -->
      <div>
        <label for="phone">Phone</label>
        <input type="text" v-model="user.phone" id="phone" required />
      </div>

      <!-- Password field -->
      <div>
        <label for="password">Password</label>
        <input type="password" v-model="user.password" id="password" required />
      </div>

      <!-- Confirm Password field -->
      <div>
        <label for="confirm_password">Confirm Password</label>
        <input type="password" v-model="user.confirm_password" id="confirm_password" required />
      </div>

      <button type="submit">Register</button>
    </form>

    <!-- Message display -->
    <p v-if="message" class="error">{{ message }}</p>
  </div>
</template>

<script scoped>
import axios from 'axios';

export default {
  data() {
    return {
      user: {
        first_name: '',
        last_name: '',
        email: '',
        phone: '',
        password: '',
        confirm_password: ''
      },
      message: ''  // Store error messages
    };
  },
  methods: {
    // Function to handle user registration
    async registerUser() {
      // Prepare the data to be sent to the backend
      const userData = {
        first_name: this.user.first_name,
        last_name: this.user.last_name,  
        email: this.user.email,
        phone: this.user.phone,
        password: this.user.password,
        confirm_password: this.user.confirm_password,
      };

      try {
        // Send registration data to the Django backend
        await axios.post('http://127.0.0.1:8000/auth/api/register/user/', userData); // Use user registration endpoint
        // Handle success, redirect or show success message
        this.message = 'User registered:';
      } catch (error) {
        // Handle errors if any
        if (error.response) {
          // If error.response exists, show the error message from backend
          const errors = error.response.data;
          if (errors.email) {
            this.message = errors.email[0];
          } else if (errors.non_field_errors) {
            this.message = errors.non_field_errors[0];
          } else if (errors.password){
            this.message = errors.password[0];
          } else {
            this.message = 'Error registering user: ' + JSON.stringify(errors);
          }
        } else {
          // If there's no response, handle the general error
          this.message = 'An unexpected error occurred.';
        }
      }
    }
  }
};
</script>
