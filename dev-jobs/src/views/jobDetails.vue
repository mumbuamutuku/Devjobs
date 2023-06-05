<template>
    <HeaderArea/>
    <JobArea/>
</template>

<script>
import HeaderArea from '@/components/HeaderArea.vue';
import JobArea from '@/components/JobArea.vue';
export default {
    name: 'headerArea',
    components:{
        HeaderArea,
        JobArea
    },
    data () {
        return{

        }
    },
    
}
</script>