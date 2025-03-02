import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../views/Dashboard.vue";
import DocumentAuditing from "../views/DocumentAuditing.vue";
import Login from "../views/Login.vue";
import Profile from "../views/Profile.vue";
import UploadRules from "../views/UploadRules.vue";

const routes = [
  { path: "/", redirect: "/login" },
  { path: "/login", name: "Login", component: Login },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
    meta: { requiresAuth: true },
  },
  {
    path: "/upload",
    name: "UploadRules",
    component: UploadRules,
    meta: { requiresAuth: true },
  },
  {
    path: "/auditing",
    name: "DocumentAuditing",
    component: DocumentAuditing,
    meta: { requiresAuth: true },
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Global navigation guard to protect routes
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem("auth") === "true";
  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ path: "/login" });
  } else {
    next();
  }
});

export default router;
