import MainPage from "@/pages/MainPage.vue";
import DealPage from "@/pages/DealPage.vue";
import CounterPartyPage from "@/pages/CounterPartyPage.vue";
import ReportPage from "@/pages/ReportPage.vue";
import CounterPartyId from "@/pages/CounterPartyId.vue";
import {createRouter, createWebHistory} from 'vue-router';


const routes = [
    {
        path:'/',
        component: MainPage
    },
    {
        path:'/deals',
        component: DealPage
    },
    {
        path:'/counterparty',
        component: CounterPartyPage
    },
    {
        path:'/report',
        component: ReportPage
    },
    {
        path:'/counterparty/:id',
        component: CounterPartyId
    }
]


const router  = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router