<template>
<div class="row plain-element">
  <div class="row header">
          <div class="col s1 text-left plain-element">
              <img src="https://linkedin-analytics.s3-eu-west-1.amazonaws.com/static/img/insights/finance-medium.jpg" class="img responsive img-header">
          </div>
          <div class="col s11 plain-element">
              <div class="row summary">
                   <div class="box">
                      <h5>{{ getTitle() }} Listing </h5>
                      <router-link class="btn-algorithm" :to="{ name: 'sector', params: { category: category } }">
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
      <div v-if="getCompanies" class="row row-cards">
          <div v-for="(company, i) in filteredList" class="col s12 m4 l3 plain-element" :key="i">
            <a target="_blank" :href="company.websiteUrl">
              <div class="card company-card">
                  <div class="card-header">
                     <div class="row plain-element">
                          <div class="col s3  plain-element">
                              <div class="card-image">
                                  <img :src="company.squareLogoUrl"
                                       class="img responsive">
                              </div>
                              </div>
                          <div class="col s9 plain-element">
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

                      </p>
                  </div>

              </div>

          </a>
        </div>

      </div>
  </div>
</div>
</template>


<script>

import { mapGetters, mapActions } from "vuex";


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
      search: "",
    }
  },
  methods: {
    ...mapGetters(["getCompanies", "getTitle"  ]),
    ...mapActions(["fetchCompanies", "fetchTitle"]),
    fetchCompaniesData(category) {
      this.fetchCompanies(category);
      this.fetchTitle(category);
    }

  },
  computed: {
//  Search company function
    filteredList() {
      return this.getCompanies().filter(company => {
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
    this.fetchCompaniesData("finance");
    document.title = "Linkedin Analytics - " + this.getTitle();
  }
}

</script>