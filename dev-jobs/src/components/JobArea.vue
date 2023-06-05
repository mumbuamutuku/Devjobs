<template>
    <div class="job-details-banner">
        <div class="banner-img" :style="{background: job.logoBackground}">
            <img :src="job.logo" alt="">
        </div>
        <div class="banner-text">
            <h2>{{job.company}}</h2>
            <p>{{job.company}}.com</p>
        </div>
            <button :href="job.website">Company Site</button>
    </div>
    <div class="job-details-card">
        <div class="card-1" style="">
            <div class="card-1-sub">
                <div style="display:flex">
                    <p>{{job.postedAt}}</p>
                    <p
                    class="dot-notation"
                    style="font-size: 20px; padding-right: 10px; padding-left: 12px"
                    >
                    &#x2022;
                    </p>
                    <p>{{job.contract}}</p>
                </div>
                <h2>{{job.position}}</h2>
                <p style="color:#5964e0">{{job.location}}</p>
            </div>
            <button :href="job.apply">Apply Now</button>
        </div>
        <p class="card-text-1">{{job.description}}</p>
        <div class="card-text-2">
            <h2>Requirements</h2>
            <p>{{job.requirements.content}}</p>
            <ul v-for="(i, index) in job.requirements.items" :key="index">
                <li>{{i}}</li>
            </ul>
        </div>
        <div class="card-text-2">
            <h2>What you will do</h2>
            <p>{{job.role.content}}</p>
            <ul v-for="(i, index) in job.role.items" :key="index">
                <li :id="index">{{i}}</li>
            </ul>
        </div>
    </div>
    <footer>
        <div class="job-details-footer">
            <div>
                <h4>{{job.position}}</h4>
                <p>{{job.company}}</p>
            </div>
            <button :href="job.apply">Apply Now</button>
        </div>
    </footer>
</template>
<script>
import json from "../assets/data.json";
export default {
    name: 'jobArea',
    components:{
       
    },
    data () {
        return{
            jobs: json,
            job: null,
            id: this.$route.params.id
        }
    },
    
    created(){
        console.log(this.id, 'id')
        this.job = this.jobs.find((x) => x.id == this.id);
        console.log(this.job)
        console.log(this.job.logo)
    }
    
}
</script>