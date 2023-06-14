<template>
  <main>
    <!-- Search Section -->
    <div class="search-section">
      <div class="search-by-title">
        <img src="/images/icon-search.svg" alt=""/>
        <input
          type="search"
          name=""
          id=""
          v-model="filter.search"
          placeholder="Filter by title, companies, expertise..."
        />
      </div>
      <div class="search-by-location">
        <img src="/images/icon-location.svg" alt="" />
        <input
          type="search"
          name=""
          id=""
          v-model="filter.location"
          placeholder="Filter by location..."
        />
      </div>
      <div class="search-button">
        <input type="checkbox" name="" id="full" value="Full Time" v-model="filter.checked" />
        <p>Full Time only</p>
        <button>Search</button>
      </div>
    </div>
    <!-- Display not found if no job is found -->
    <div class="job-section-list-no-list" v-if="filteredList < 1">No Job Found</div>
    <div class="job-section" v-else>
      <div class="job-section-list" v-for="job in filteredList" :key="job.id">
        <router-link :to="{ path: 'job/' + job.company + '/' + job.id }" style="text-decoration: none;">
          <div class="image-head" :style="{background: job.logoBackground}">
            <img :src="job.logo" alt="" />
          </div>
          <div class="job-section-list--content">
            <div class="job-section-list--time">
              <p>{{job.postedAt}}</p>
              <p
                class="dot-notation"
                style="font-size: 20px; padding-right: 10px; padding-left: 12px"
              >
                &#x2022;
              </p>
              <p>{{job.contract}}</p>
            </div>
            <h3>{{job.position}}</h3>
            <p>{{job.company}}</p>
          </div>
          <div style="margin-top: 19px; color: #5964e0">
            <h4>{{job.location}}</h4>
          </div>
        </router-link>
        
      </div>
    </div>
  </main>
</template>

<script>
import json from "../assets/data.json";
export default {
  name: "mainArea",
  data() {
    return {
      jobs: json,
      filter:{
        search: "",
        location: "",
        checked:[]
      },
      isChecked: false
    };
  },
  methods: {
  
  },
  computed:{
    filteredList() {
        const {search, location, checked} = this.filter
        
        return this.jobs.filter(job => {
            const searchMatch = job.position.toLowerCase().includes(search.toLowerCase())
            const companiesMatch = job.company.toLowerCase().includes(search.toLowerCase())
            const locationMatch = job.location.toLowerCase().includes(location.toLowerCase())
            const checkedMatch = job.contract.includes(checked)

            return (searchMatch || companiesMatch) && locationMatch && checkedMatch
        })
    },
  },
  mounted() {
  },
};
</script>
