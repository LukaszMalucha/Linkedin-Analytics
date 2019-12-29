<template>
<div class="row plain-element">
  <div class="row header">
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 text-left plain-element">
              <img src="https://linkedin-analytics.s3-eu-west-1.amazonaws.com/static/img/insights/finance-medium.jpg" class="img responsive img-header">
          </div>
          <div class="col-xs-11 col-sm-11 col-md-11 col-lg-11 plain-element">
              <div class="row summary">
                   <div class="box">
                      <h5>{{ companiesType }} Listing </h5>
                      <router-link class="btn-algorithm" :to="{ name: category }">
                        Sector Insights
                      </router-link>
                  </div>
                  <div class="box">
                  <h6>Search Company:</h6>
                  <div class="search-wrapper">
                    <input type="text" v-model="search"/>
                  </div>
                  </div>
              </div>
          </div>

  </div>
  <div class="dashboard-cards">
      <div class="row row-cards">
          <div v-for="(company, i) in filteredList" class="col-xs-12 col-sm-4 col-md-4 col-lg-3 plain-element" :key="i">
            <div class="card company-card">
                <div class="card-header">
                   <div class="row plain-element">
                        <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3  plain-element">
                            <div class="card-image">
                                <img :src="company.squareLogoUrl"
                                     class="img responsive">
                            </div>
                            </div>
                        <div class="col-xs-9 col-sm-9 col-md-9 col-lg-9 plain-element">
                        <div class="card-title text-left">
                            <h5>{{ company.name | truncate(50) }}</h5>
                            <table class="table table-company">
                                <tbody>
                                <tr>
                                    <td>Co. Type:</td>
                                    <td><b>{{company.companyType}}</b></td>
                                </tr>
                                <tr>
                                    <td>Industry:</td>
                                    <td><b>{{company.industries | truncate(23)}}</b></td>
                                </tr>
                                <tr>
                                    <td>Employees:</td>
                                    <td><b>{{company.employeeCountRange}}</b></td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                       </div>
                </div>
                </div>
                <div class="card-content">
                    <p>Company established in {{ company.foundedYear }}. <b>{{ company.name }}</b> specializes in: {{ company.specialities }}.
                    <a target="_blank" :href="company.websiteUrl">Visit Website</a>
                    </p>


                </div>

            </div>
        </div>
      </div>
  </div>
</div>
</template>


<script>
import { apiService } from "@/common/api.service.js";


export default {
  name: "Companies",
  components: {

  },
  props: {
    category: {
    type: String,
    required: true
    }
  },
  data() {
    return{
      search: '',
      results: [],
      companiesCount: 0,
      companiesType: ''
    }
  },
  methods: {
    getCompaniesData() {
    let endpoint = `/api/${this.category}-list/`;
    apiService(endpoint)
      .then(data => {
          this.results = data.results,
          this.companiesCount = data.count
      })
    },
    getTitleString() {
      if (this.category == 'finance') {
          this.companiesType = 'Financial Companies'
      }
      else if (this.category == 'it') {
          this.companiesType = 'IT Companies'
      }
      else {
         this.companiesType = 'Educational Institutions'
      }
    },
  },
  computed: {
//  Search company function
    filteredList() {
      return this.results.filter(company => {
        return company.name.toLowerCase().includes(this.search.toLowerCase()) ||
               company.industries.toLowerCase().includes(this.search.toLowerCase()) ||
               company.companyType.toLowerCase().includes(this.search.toLowerCase()) ||
               company.specialities.toLowerCase().includes(this.search.toLowerCase()) ||
               company.foundedYear.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  filters: {
      truncate (value, limit) {
          if (value.length > limit) {
              value = value.substring(0, limit);
          }
          return value
      }
  },
  created() {
    this.getCompaniesData();
    this.getTitleString();
    document.title = "Linkedin Analytics - " + this.companiesType;
  }
}

</script>