import { createRouter, createWebHistory} from "vue-router";
import jobDetails from '../views/jobDetails.vue'
import jobViews from '../views/jobViews.vue'

const routes = [
    {
        path: '/',
        name: 'jobViews',
        component: jobViews
    },
    {
        path: '/job/:company/:id',
        name: 'jobDetails',
        component: jobDetails
    }
    
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router