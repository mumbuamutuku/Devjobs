<template>
    <HeaderArea/>
    <MainArea/>
</template>

<script>
import HeaderArea from '@/components/HeaderArea.vue';
import MainArea from '@/components/MainArea.vue';
export default {
    name: 'jobViews',
    components:{
        HeaderArea,
        MainArea
    },
    
}
</script>