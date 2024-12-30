// Importing necessary modules and components
import { createRouter, createWebHistory } from 'vue-router'; // Import Vue Router and history mode for clean URLs
import MainPage from '../views/MainPage.vue'; // Main landing page component
import NutritionistRegister from '@/views/NutritionistRegister.vue'; // Nutritionist registration component
import UserRegister from '@/views/UserRegister.vue'; // Client registration component
import LoginPage from '@/views/LoginPage.vue'; // Login page component
import DashboardPage from '@/views/DashboardPage.vue'; // Dashboard component
import axiosInstance from '@/axios'; // Axios instance with interceptors
import AvailableNutritionists from '@/views/AvailableNutritionists.vue'; // Available nutritionists component
import ClientsNutritionist from '@/views/ClientsNutritionist.vue';

// Defining the application's routes
const routes = [
  { path: '/', component: MainPage }, // Route for the main landing page
  { path: '/register-client', component: UserRegister }, // Route for client registration page
  { path: '/register-nutritionist', component: NutritionistRegister }, // Route for nutritionist registration page
  { path: '/login', component: LoginPage }, // Route for login page
  { path: '/dashboard', component: DashboardPage, meta: { requiresAuth: true } }, // Route for dashboard with authentication requirement
  { path: '/available-nutritionists', component: AvailableNutritionists, meta: { requiresAuth: true, requiresClient: true } }, // Route for available nutritionists with authentication and client requirement
  { path: '/clients-nutritionist', component: ClientsNutritionist, meta: { requiresAuth: true, requiresClient: false } }, // Route for clients of a nutritionist with authentication and nutritionist requirement
];

// Creating the Vue Router instance
const router = createRouter({
  history: createWebHistory(), // Use HTML5 history mode for cleaner URLs (no # in the URL)
  routes, // Assign the defined routes to the router
});

// Route guard to check authentication and user type
router.beforeEach(async (to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth); // Check if route requires authentication
  const requiresClient = to.matched.some(record => record.meta.requiresClient); // Check if route requires client access

  if (requiresAuth) {
    const token = localStorage.getItem('accessToken');
    if (token) {
      try {
        // Verify if the token is still valid
        await axiosInstance.post('/api/token/verify/', { token });

        if (requiresClient) {
          // Check if the user is a client
          const response = await axiosInstance.get('/api/user-profile/');
          const userProfile = response.data;

          // If the user is a client, allow access; otherwise, redirect to dashboard
          if (userProfile.registration_number) {
            next({ path: '/clients-nutritionist' }); // Redirect nutritionists to dashboard
          } else {
            next(); // Allow clients to proceed
          }
        } else {
          next(); // Allow access if route does not require client access
        }
      } catch (error) {
        // If the token is invalid or expired
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
        next({ path: '/login' }); // Redirect to login page
      }
    } else {
      // If there is no token
      next({ path: '/login' }); // Redirect to login page
    }
  } else {
    next(); // Allow access to routes that do not require authentication
  }
});

// Exporting the router instance to use it in the main Vue application
export default router;
