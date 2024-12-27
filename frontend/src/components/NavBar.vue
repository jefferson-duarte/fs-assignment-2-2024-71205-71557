<template>
  <nav class="navbar">
    <div class="navbar-container">
      <div class="navbar-content">
        <div class="navbar-logo">
          <span>Logo</span>
        </div>
        <div class="navbar-menu desktop-menu">
          <router-link v-for="item in menuItems" :key="item.path" :to="item.path" class="navbar-link">
            {{ item.name }}
          </router-link>
        </div>
      </div>
      <div class="mobile-menu-button">
        <button @click="isOpen = !isOpen" type="button" aria-controls="mobile-menu" :aria-expanded="isOpen">
          <svg v-if="!isOpen" class="menu-icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
          <svg v-else class="menu-icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
    </div>

    <transition name="fade">
      <div v-show="isOpen" class="mobile-menu" id="mobile-menu">
        <router-link v-for="item in menuItems" :key="item.path" :to="item.path" class="navbar-link mobile-link">
          {{ item.name }}
        </router-link>
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
      menuItems: [
        { name: 'Home', path: '/' },
        { name: 'Register Customer', path: '/register-client' },
        { name: 'Register Nutritionist', path: '/register-nutritionist' },
        { name: 'Login', path: '/login' },
        { name: 'Dashboard', path: '/dashboard' }
      ]
    }
  }
}
</script>

<style scoped>
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
  justify-content: space-around;
}

.navbar-logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.navbar-menu {
  display: none;
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

.mobile-menu-button {
  display: block;
}

.menu-icon {
  width: 1.5rem;
  height: 1.5rem;
  color: white;
}

.mobile-menu {
  padding: 1rem;
  background-color: #2c3e50;
}

.mobile-link {
  display: block;
  padding: 0.5rem 0;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

@media (min-width: 768px) {
  .navbar-menu {
    display: flex;
    gap: 1rem;
  }

  .mobile-menu-button {
    display: none;
  }

  .mobile-menu {
    display: none;
  }
}
</style>
