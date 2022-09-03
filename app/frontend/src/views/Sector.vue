<template>
<div class="row plain-element">
  <div class="row header">
          <div class="col s1 text-left plain-element">
              <img src="https://linkedin-analytics.s3-eu-west-1.amazonaws.com/static/img/insights/finance-medium.jpg" class="img responsive img-header">
          </div>
          <div class="col s11 plain-element">
              <div class="row summary">
                   <div class="box">
                      <h5>{{ getTitle() }} Insights </h5>
                      <router-link class="btn-algorithm" :to="{ name: 'companies', params: { category: category } }">
                        View Companies
                      </router-link>
                  </div>
                  <h6>Sector Companies: <b class="counter">{{ getCompanyCount() }}</b></h6>
              </div>
          </div>

  </div>
  <div class="dashboard-cards">
      <div class="row row-cards">
          <div class="col s12 m6 l3 plain-element">
              <div class="row plain-element no-margin-bottom">
                  <div class="card insights-card insights-card-narrow-left" id="establishedCard">
                      <div class="card-header">
                          <img src="https://linkedin-analytics.s3-eu-west-1.amazonaws.com/static/img/insights/finance-small.jpg" class="img-responsive">
                          <p><b>Linkedin Analytics</b> <br>{{ getTitle() }} </p>

                      </div>
                      <div class="row row-comment">
                          {{ getTitle() }} with tradition:
                      </div>

                      <div class="row-image">
                          <div class="table-responsive">
                              <table class="table table-content" id="tableEstablished">
                                  <thead>
                                  <tr>
                                      <th>Company</th>
                                      <th class="center">Established</th>
                                  </tr>
                                  </thead>
                                  <tbody>

                                  <tr v-for="(company, i) in getOldestTenCompanies()" :key="i">
                                      <td>{{ company ["name"]}}</td>
                                      <td class="center">{{ company ["foundedYear"]}}</td>
                                  </tr>

                                  </tbody>
                              </table>
                          </div>
                      </div>
                  </div>
              </div>
              <div class="row plain-element">
                  <div class="card insights-card insights-card-narrow-left" id="smallCard">
                      <div class="card-header">
                          <img src="https://linkedin-analytics.s3-eu-west-1.amazonaws.com/static/img/insights/finance-small.jpg" class="img-responsive">
                          <p><b>Linkedin Analytics</b> <br>{{ getTitle() }} </p>
                      </div>
                      <div class="row row-comment">
                          {{ getTitle() }} followers:
                      </div>
                      <div class="chart-small">
                          <followers-chart  :chart-data="getFollowersCountData()" :styles="chartStyles"></followers-chart>
                      </div>
                  </div>
              </div>
          </div>

          <div class="col s12 m6 l6 plain-element">
              <div class="row plain-element">
                  <div class="card insights-card insights-card-middle">
                      <div class="card-header">
                          <img src="https://linkedin-analytics.s3-eu-west-1.amazonaws.com/static/img/insights/finance-small.jpg" class="img-responsive">
                          <p><b>Linkedin Analytics</b> <br>{{ getTitle() }} </p>

                      </div>
                      <div class="row row-comment">
                          {{ getTitle() }} by type:
                      </div>
                      <div class="chart">
                          <types-chart  :chart-data="getCompanyTypesData()" :styles="chartStyles"></types-chart>
                      </div>
                  </div>
              </div>
              <div class="row plain-element">
                  <div class="card insights-card insights-card-middle">
                      <div class="card-header">
                          <img src="https://linkedin-analytics.s3-eu-west-1.amazonaws.com/static/img/insights/finance-small.jpg" class="img-responsive">
                          <p><b>Linkedin Analytics</b> <br>{{ getTitle() }} </p>

                      </div>
                      <div class="row row-comment">
                          {{ getTitle() }} by employee count:
                      </div>
                      <div class="chart">
                          <employees-chart  :chart-data="getEmployeeCountData()" :styles="chartStyles"></employees-chart>
                      </div>
                  </div>
              </div>
          </div>
          <div class="col s12 m6 l3 plain-element">
              <div class="card insights-card insights-card-narrow-right" id="tableSpecialities">
                  <div class="card-header">
                      <img src="https://linkedin-analytics.s3-eu-west-1.amazonaws.com/static/img/insights/finance-small.jpg" class="img-responsive">
                      <p><b>Linkedin Analytics</b> <br>{{ getTitle() }}</p>
                  </div>
                  <div class="row row-comment">
                      {{ getTitle() }} by specialties:
                  </div>
                  <div class="row-image">
                      <div class="table-responsive">
                          <table class="table table-content table-long">
                              <thead>
                              <tr>
                                  <th>Speciality</th>
                                  <th class="center">Occurence</th>
                              </tr>
                              </thead>
                              <tbody>
                              <tr  v-for="(key, value, i) in getSpecialties()" :key="i">
                                  <td>{{ value }}</td>
                                  <td class="center">{{ key }}</td>
                              </tr>
                              </tbody>
                          </table>
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </div>
</div>
</template>


<script>
import FollowersChart from "@/common/FollowersChart.js";
import EmployeesChart from "@/common/EmployeesChart.js";
import TypesChart from "@/common/TypesChart.js";
import { mapGetters, mapActions } from "vuex";



export default {
  name: "Finance",
  components: {
    FollowersChart,
    EmployeesChart,
    TypesChart,
  },
  props: {
    category: {
    type: String,
    required: true
    }
  },
  data() {
    return {
      companyCategory: "",
    }
  },
  methods: {
    ...mapGetters(["getTitle", "getCompanyCount", "getCompanyCategory",
                    "getOldestTenCompanies", "getSpecialties", "getFollowersCount",
                    "getEmployeeCount", "getCompanyTypes", "getFollowersCountData",
                    "getEmployeeCountData","getCompanyTypesData"]),
    ...mapActions(["fetchSectorData", "fetchTitle"]),
    getSectorData(category) {
      this.fetchSectorData(category)
      this.fetchTitle(category);
    },

  },
  computed: {
    chartStyles () {
      return {
        height: `100%`,
        position: "relative"
      }
    }
  },
  created() {
    this.getSectorData(this.category);
    document.title = "Linkedin Analytics - Financial Companies";
  }
};

</script>
