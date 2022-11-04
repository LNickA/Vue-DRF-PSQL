import { createApp } from 'vue'
import App from './App.vue'
import components from "@/components/UI";
import router from '@/router/router';
import JsonExcel from "vue-json-excel3";



const app = createApp(App)

components.forEach(component=>{
    app.component(component.name, component)
})


app
    .component("downloadExcel", JsonExcel)
    .use(router)
    .mount('#app')
