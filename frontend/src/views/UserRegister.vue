<template>
  <div class="register-form container mt-5">
    <h2 class="text-center mb-4">User Registration</h2>
    <form @submit.prevent="registerUser" class="card p-4 shadow">
      <!-- First name field -->
      <div class="form-group mb-3">
        <label for="first_name">First Name</label>
        <input
          type="text"
          v-model="user.first_name"
          id="first_name"
          class="form-control"
          :class="{ 'is-invalid': errors.first_name }"
          placeholder="Enter your first name"
          required
        />
        <div v-if="errors.first_name" class="invalid-feedback">
          {{ errors.first_name }}
        </div>
      </div>

      <!-- Last name field -->
      <div class="form-group mb-3">
        <label for="last_name">Last Name</label>
        <input
          type="text"
          v-model="user.last_name"
          id="last_name"
          class="form-control"
          :class="{ 'is-invalid': errors.last_name }"
          placeholder="Enter your last name"
          required
        />
        <div v-if="errors.last_name" class="invalid-feedback">
          {{ errors.last_name }}
        </div>
      </div>

      <!-- Email field -->
      <div class="form-group mb-3">
        <label for="email">Email</label>
        <input
          type="email"
          v-model="user.email"
          id="email"
          class="form-control"
          :class="{ 'is-invalid': errors.email }"
          placeholder="Enter your email"
          required
        />
        <div v-if="errors.email" class="invalid-feedback">
          {{ errors.email }}
        </div>
      </div>

      <!-- Phone field -->
      <div class="form-group mb-3">
        <label for="phone">Phone</label>
        <input
          type="text"
          v-model="user.phone"
          id="phone"
          class="form-control"
          placeholder="Enter your phone number"
          required
        />
      </div>

      <!-- Password field -->
      <div class="form-group mb-3">
        <label for="password">Password</label>
        <input
          type="password"
          v-model="user.password"
          id="password"
          class="form-control"
          :class="{ 'is-invalid': errors.password }"
          placeholder="Enter your password"
          required
        />
        <div v-if="errors.password" class="invalid-feedback">
          {{ errors.password }}
        </div>
      </div>

      <!-- Confirm Password field -->
      <div class="form-group mb-3">
        <label for="confirm_password">Confirm Password</label>
        <input
          type="password"
          v-model="user.confirm_password"
          id="confirm_password"
          class="form-control"
          :class="{ 'is-invalid': errors.password }"
          placeholder="Re-enter your password"
          required
        />
        <div v-if="errors.password" class="invalid-feedback">
          {{ errors.password }}
        </div>
      </div>

      <!-- Submit button -->
      <button type="submit" class="btn btn-primary w-100">Register</button>
    </form>

    <!-- Success Message -->
    <p v-if="successMessage" class="alert alert-success mt-4">{{ successMessage }}</p>

    <!-- Error Message -->
    <p v-if="message && !successMessage" class="alert alert-danger mt-4">{{ message }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      user: {
        first_name: "",
        last_name: "",
        email: "",
        phone: "",
        password: "",
        confirm_password: "",
      },
      message: "", // General error messages
      successMessage: "", // Success message
      errors: {}, // Field-specific validation errors
    };
  },
  methods: {
    async registerUser() {
      // Clear previous errors and messages
      this.errors = {};
      this.message = "";
      this.successMessage = "";

      // Simple validation for first and last name
      if (!this.user.first_name.trim()) {
        this.errors.first_name = "First name cannot be blank.";
      }
      if (!this.user.last_name.trim()) {
        this.errors.last_name = "Last name cannot be blank.";
      }

      // Prevent submission if there are validation errors
      if (Object.keys(this.errors).length > 0) {
        return;
      }

      try {
        // Send data to the backend
        const userData = { ...this.user };
        await axios.post("http://127.0.0.1:8000/auth/api/register/user/", userData);

        // Display success message
        this.successMessage = "User registered successfully!";
        
        // Reset the form fields
        this.user = {
          first_name: "",
          last_name: "",
          email: "",
          phone: "",
          password: "",
          confirm_password: "",
        };
      } catch (error) {
        // Handle errors from the backend
        if (error.response) {
          const errors = error.response.data;
          if (errors.first_name) {
            this.errors.first_name = errors.first_name[0];
          }
          if (errors.last_name) {
            this.errors.last_name = errors.last_name[0];
          }
          if (errors.email) {
            this.errors.email = errors.email[0];
          }
          if (errors.password) {
            this.errors.password = errors.password[0];
          }
          if (errors.non_field_errors) {
            this.message = errors.non_field_errors[0];
          }
        } else {
          this.message = "An unexpected error occurred.";
        }
      }
    },
  },
};
</script>

<style scoped>
.register-form {
  max-width: 600px;
  margin: 0 auto;
}
.card {
  border-radius: 10px;
  border: none;
  background-color: #f9f9f9;
}
.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
  font-weight: bold;
}
.btn-primary:hover {
  background-color: #0056b3;
  border-color: #004085;
}
.invalid-feedback {
  font-size: 0.875rem;
}
.alert-success {
  color: #155724;
  background-color: #d4edda;
  border-color: #c3e6cb;
}
.alert-danger {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
}
</style>
