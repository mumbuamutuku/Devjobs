<template>
    <header>
        <nav>
            <router-link :to="{ path: '/' }" style="text-decoration: none;">
            <div class="logo">
                <img src="/images/logo.svg" alt="" srcset="">
            </div>
            </router-link>
            <div class="switcher">
                
               
                <label id="switch" class="switch">
                   <img src="/images/icon-sun.svg" alt="" style="margin-left: -11px;">
                    <input type="checkbox" @change="toggleTheme" id="slider">
                    <span class="slider round"></span>
                    <img src="/images/icon-moon.svg" alt="" style="    margin-left: 66px;">
                    
                </label>
               
            </div>
        </nav>
        
    </header>
</template>

<script>
export default {
    name: 'headerArea',
    data () {
        return{

        }
    },
    methods:{
        setTheme(themeName) {
        localStorage.setItem('theme', themeName);
        document.documentElement.className = themeName;
        },
        toggleTheme() {
            if (localStorage.getItem('theme') === 'theme-dark') {
                this.setTheme('theme-light');
            } 
            else {
                this.setTheme('theme-dark');
            }
        },
        setThemeNow () {
            if (localStorage.getItem('theme') === 'theme-light') {
                this.setTheme('theme-light');
                document.getElementById('slider').checked = false;
            } else {
                this.setTheme('theme-light');
                document.getElementById('slider').checked = true;
            }
        }
    },
    mounted(){
        this.setThemeNow()
    }
}
</script>