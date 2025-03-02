<!-- src/views/Login.vue -->
<template>
  <div
    class="flex justify-center items-center h-screen bg-gradient-to-r from-blue-50 to-blue-100"
  >
    <div class="bg-white p-10 rounded-lg shadow-lg w-full max-w-sm">
      <h2 class="text-3xl font-bold mb-6 text-center text-blue-600">
        Employee Login
      </h2>
      <form @submit.prevent="login">
        <div class="mb-4">
          <label for="username" class="block text-gray-700 mb-2"
            >Username</label
          >
          <input
            type="text"
            id="username"
            v-model="username"
            required
            class="w-full p-2 border rounded focus:outline-none focus:ring focus:border-blue-300"
          />
        </div>
        <div class="mb-6">
          <label for="password" class="block text-gray-700 mb-2"
            >Password</label
          >
          <input
            type="password"
            id="password"
            v-model="password"
            required
            class="w-full p-2 border rounded focus:outline-none focus:ring focus:border-blue-300"
          />
        </div>
        <!-- <p v-if="errorMessage" class="text-red-500 text-sm mb-4">{{ errorMessage }}</p> -->

        <button
          type="submit"
          class="w-full bg-blue-500 hover:bg-blue-600 text-white py-2 rounded transition-colors duration-200"
        >
          Login
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { useAuthStore } from "../store/auth";

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      errorMessage: "",

    };
  },
  setup() {
    const authStore = useAuthStore();
    return { authStore };
  },
  methods: {

    // API call to login
    // async login() {
    //   if (!this.username || !this.password) {
    //     this.errorMessage = "Please enter your credentials.";
    //     return;
    //   }

    //   try {
    //     const response = await axios.post("http://127.0.0.1:8000/login/", {
    //       username: this.username,
    //       password: this.password,
    //     });

    //     if (response.data === "Authentication succeed.") {
    //       this.authStore.login(); // Save authentication state
    //       this.$router.push("/dashboard"); // Redirect to dashboard
    //     } else {
    //       this.errorMessage = response.data; // Show backend response error
    //     }
    //   } catch (error) {
    //     this.errorMessage = "Login failed. Please check your credentials.";
    //   }
    // },
  
    login() {
      if (this.username && this.password) {
        // Call the store's login action to update the reactive auth state.
        this.authStore.login();
        this.$router.push("/dashboard");
      } else {
        alert("Please enter your credentials.");
      }
    },
  },
};
</script>
