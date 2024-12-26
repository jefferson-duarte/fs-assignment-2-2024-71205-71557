import { createRouter, createWebHistory } from 'vue-router';
import MainPage from '../components/MainPage.vue';
import NutritionistRegister from '@/components/NutritionistRegister.vue';
import UserRegister from '@/components/UserRegister.vue';

const routes = [
  { path: '/', component: MainPage },
  { path: '/register-client', component: UserRegister },
  { path: '/register-nutritionist', component: NutritionistRegister },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
