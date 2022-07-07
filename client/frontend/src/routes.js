
import Login from './components/Login.vue';
import Client from './components/Client.vue';
import Admin from './components/Admin.vue';
import Home from './components/Home.vue';
import { createRouter, createWebHistory } from 'vue-router';
import { isAuthenticated, isAdmin } from './services/UserService';



const routes = [
    {
        path: '/login',
        name: 'login',
        component: Login,
        // guest middleware
        beforeEnter: (to, from) => {
            if (isAuthenticated()) {
                return { name: 'home' };
            }
        }
    },
    {
        path: '/',
        name: 'home',
        component: Home,
    },

]



const router = createRouter({
    history: createWebHistory(),
    routes
});

// auth middleware
router.beforeEach(async (to, from) => {
    // alert(isAuthenticated)
    if (
        !isAuthenticated() &&
        to.name !== 'login'
    ) {
        return { name: 'login' };
    }
})




export default router;

