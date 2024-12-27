import axios from 'axios';

// Create an Axios instance with a base URL and default headers
const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/auth',
  headers: {
    'Content-Type': 'application/json'
  }
});

// Add a request interceptor to include the access token in the headers if it exists
axiosInstance.interceptors.request.use(
  config => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      config.headers['Authorization'] = 'Bearer ' + token;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

// Add a response interceptor to handle token refresh logic
axiosInstance.interceptors.response.use(
  response => {
    return response;
  },
  async error => {
    const originalRequest = error.config;
    // Check if the response status is 401 (Unauthorized) and the request is not retried yet
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      const refreshToken = localStorage.getItem('refreshToken');
      // Request a new access token using the refresh token
      const response = await axiosInstance.post('/token/refresh/', { refresh: refreshToken });
      if (response.status === 200) {
        // Store the new access token and update the default Authorization header
        localStorage.setItem('accessToken', response.data.access);
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access;
        // Retry the original request with the new access token
        return axiosInstance(originalRequest);
      }
    }
    return Promise.reject(error);
  }
);

export default axiosInstance;
