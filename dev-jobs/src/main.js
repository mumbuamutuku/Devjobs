import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'
import '../src/assets/styles.css'

createApp(App).use(router).mount('#app')
