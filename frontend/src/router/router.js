// Importing necessary modules and components
import { createRouter, createWebHistory } from 'vue-router'; // Import Vue Router and the history mode for web
import MainPage from '../components/MainPage.vue'; // Main page component
import NutritionistRegister from '@/components/NutritionistRegister.vue'; // Nutritionist registration component
import UserRegister from '@/components/UserRegister.vue'; // Client registration component
import LoginPage from '@/components/LoginPage.vue';
import DashboardPage from '@/components/DashboardPage.vue';
import axiosInstance from '@/axios'; // Import the Axios instance we created

// Defining the application's routes
const routes = [
  { path: '/', component: MainPage }, // Route for the main landing page
  { path: '/register-client', component: UserRegister }, // Route for client registration page
  { path: '/register-nutritionist', component: NutritionistRegister }, // Route for nutritionist registration page
  { path: '/login', component: LoginPage },
  { path: '/dashboard', component: DashboardPage, meta: { requiresAuth: true } } // Add meta field to require authentication
];

// Creating the Vue Router instance
const router = createRouter({
  history: createWebHistory(), // Use HTML5 history mode for cleaner URLs (no # in the URL)
  routes, // Assign the defined routes to the router
});

// Guard de rota para verificar a autenticação
router.beforeEach(async (to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const token = localStorage.getItem('accessToken');
    if (token) {
      try {
        // Verifica se o token ainda é válido
        await axiosInstance.post('/api/token/verify/', { token });
        next();
      } catch (error) {
        // Se o token for inválido ou expirou
        next({ path: '/login' });
      }
    } else {
      // Se não houver token
      next({ path: '/login' });
    }
  } else {
    next();
  }
});

// Exporting the router instance to use it in the main Vue application
export default router;
