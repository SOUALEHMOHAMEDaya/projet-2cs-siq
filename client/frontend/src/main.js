import { createApp } from 'vue'
import App from './App.vue'

import routes from './routes'

// document.addEventListener('contextmenu', event => event.preventDefault());

createApp(App)
    .use(routes)
    .mount('#app')
