<template>
  <nav class="navbar">
    <div class="navbar-container">
      <div class="navbar-content">
        <div class="navbar-logo">
          <span>Logo</span>
        </div>

        <!-- Desktop Menu -->
        <div class="navbar-menu desktop-menu">
          <router-link to="/" class="navbar-link">Home</router-link>

          <!-- Dropdown for Registration -->
          <div class="dropdown">
            <button class="dropbtn">
              Register
              <svg class="dropdown-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 9l6 6 6-6" />
              </svg>
            </button>
            <div class="dropdown-content">
              <router-link to="/register-client" class="dropdown-item">Register Customer</router-link>
              <router-link to="/register-nutritionist" class="dropdown-item">Register Nutritionist</router-link>
            </div>
          </div>

          <!-- Conditionally Rendered Links -->
          <router-link v-if="!isLoggedIn" to="/login" class="navbar-link">Login</router-link>
          <router-link v-if="isLoggedIn" to="/dashboard" class="navbar-link">Dashboard</router-link>
          <router-link v-if="isLoggedIn" to="/login" class="navbar-link" @click="logout">Logout</router-link>
        </div>

        <!-- Mobile Menu Button -->
        <button class="mobile-menu-button" @click="isOpen = !isOpen" :aria-expanded="isOpen">
          <svg v-if="!isOpen" class="menu-icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
          <svg v-else class="menu-icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
    </div>

    <!-- Mobile Menu -->
    <transition name="fade">
      <div v-show="isOpen" class="mobile-menu" id="mobile-menu">
        <router-link to="/" class="navbar-link mobile-link">Home</router-link>

        <!-- Dropdown for Registration in Mobile Menu -->
        <div class="dropdown">
          <button class="dropbtn">
            Register
            <svg class="dropdown-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 9l6 6 6-6" />
            </svg>
          </button>
          <div class="dropdown-content">
            <router-link to="/register-client" class="dropdown-item">Register Customer</router-link>
            <router-link to="/register-nutritionist" class="dropdown-item">Register Nutritionist</router-link>
          </div>
        </div>

        <!-- Conditionally Rendered Links -->
        <router-link v-if="!isLoggedIn" to="/login" class="navbar-link mobile-link">Login</router-link>
        <router-link v-if="isLoggedIn" to="/dashboard" class="navbar-link mobile-link">Dashboard</router-link>
        <router-link v-if="isLoggedIn" to="/login" class="navbar-link mobile-link" @click="logout">Logout</router-link>
      </div>
    </transition>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      isOpen: false,
      isLoggedIn: false, // Estado para verificar login
    };
  },
  methods: {
    checkAuth() {
      const token = localStorage.getItem("accessToken");
      this.isLoggedIn = !!token; // Define como true se o token existir
    },
    logout() {
      localStorage.removeItem("accessToken");
      localStorage.removeItem("refreshToken");
      this.isLoggedIn = false;
      this.$router.push("/login");
    },
  },
  watch: {
    // Apenas observa mudanças no $route sem usar 'to' e 'from'
    '$route'() {
      this.checkAuth(); // Atualiza o estado sempre que a rota mudar
    }
  },
  created() {
    this.checkAuth(); // Verifica o estado do login ao criar o componente
  },
};
</script>

<style scoped>
/* Navbar Styles */
.navbar {
  background-color: #2c3e50;
  color: white;
}

.navbar-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 4rem;
}

.navbar-content {
  display: flex;
  align-items: center;
  width: 100%;
  justify-content: space-between;
}

.navbar-logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.navbar-link {
  color: #ecf0f1;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  transition: background-color 0.3s;
}

.navbar-link:hover {
  background-color: #34495e;
}

/* Dropdown Styles */
.dropdown {
  position: relative;
  display: inline-block;
}

.dropbtn {
  background-color: #2c3e50;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.25rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: background-color 0.3s;
}

.dropdown:hover .dropbtn {
  background-color: #34495e;
}

.dropdown-icon {
  width: 16px;
  height: 16px;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #34495e;
  min-width: 200px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 1;
  border-radius: 0.25rem;
  overflow: hidden;
}

.dropdown-content .dropdown-item {
  color: white;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  transition: background-color 0.3s;
}

.dropdown-content .dropdown-item:hover {
  background-color: #3d566e;
}

.dropdown:hover .dropdown-content {
  display: block;
}

/* Mobile Menu */
.mobile-menu-button {
  display: none;
  background: none;
  border: none;
  color: white;
  cursor: pointer;
}

.menu-icon {
  width: 24px;
  height: 24px;
}

.mobile-menu {
  display: flex;
  flex-direction: column;
  background-color: #2c3e50;
  padding: 1rem;
}

.mobile-menu.show {
  transform: translateX(0); 
}

.mobile-link {
  color: white;
  padding: 10px 15px;
  display: block;
  text-decoration: none;
}

/* Responsive Design */
@media (max-width: 768px) {
  .desktop-menu {
    display: none;
  }
  .mobile-menu-button {
    display: block;
  }
  .mobile-menu {
    display: flex;
    margin-right: 150px;
  }
}

/* Logout Button */
.btn-logout {
  background-color: #e74c3c;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.25rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-logout:hover {
  background-color: #c0392b;
}

/* Transition */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
