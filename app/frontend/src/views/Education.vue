<template>
<div class="row plain-element">
  <div class="row header">
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 text-left plain-element">
              <img src="https://linkedin-analytics.s3-eu-west-1.amazonaws.com/static/img/insights/education-medium.jpg" class="img responsive img-header">
          </div>
          <div class="col-xs-11 col-sm-11 col-md-11 col-lg-11 plain-element">
              <div class="row summary">
                   <div class="box">
                      <h5>{{ companyCategory }} Insights </h5>
                      <router-link class="btn-algorithm" :to="{ name: 'companies', params: { category: category } }">
                        View Companies
                      </router-link>
                  </div>
                  <h6>Sector Companies: <b class="counter">{{ companyCount }}</b></h6>
              </div>
          </div>

  </div>
  <div class="dashboard-cards">
      <div class="row row-cards">
          <div class="col-sm-3 col-md-3 col-lg-3 plain-element">
              <div class="row plain-element no-margin-bottom">
                  <div class="card insights-card insights-card-narrow-left" id="establishedCard">
                      <div class="card-header">
                          <img src="https://linkedin-analytics.s3-eu-west-1.amazonaws.com/static/img/insights/education-small.jpg" class="img-responsive">
                          <p><b>Linkedin Analytics</b> <br>{{ companyCategory }} </p>

                      </div>
                      <div class="row row-comment">
                          {{ companyCategory }} with tradition:
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

                                  <tr v-for="(company, i) in oldestTenCompanies" :key="i">
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
                          <img src="https://linkedin-analytics.s3-eu-west-1.amazonaws.com/static/img/insights/education-small.jpg" class="img-responsive">
                          <p><b>Linkedin Analytics</b> <br>{{ companyCategory }} </p>
                      </div>
                      <div class="row row-comment">
                          {{ companyCategory }} followers:
                      </div>
                      <div class="chart-small">
                          <followers-chart  :chart-data="followersCountData" :styles="chartStyles"></followers-chart>
                      </div>
                  </div>
              </div>
          </div>

          <div class="col-sm-6 col-md-6 col-lg-6 plain-element">
              <div class="row plain-element">
                  <div class="card insights-card insights-card-middle">
                      <div class="card-header">
                          <img src="https://linkedin-analytics.s3-eu-west-1.amazonaws.com/static/img/insights/education-small.jpg" class="img-responsive">
                          <p><b>Linkedin Analytics</b> <br>{{ companyCategory }} </p>

                      </div>
                      <div class="row row-comment">
                          {{ companyCategory }} by type:
                      </div>
                      <div class="chart">
                          <types-chart  :chart-data="companyTypesData" :styles="chartStyles"></types-chart>
                      </div>
                  </div>
              </div>
              <div class="row plain-element">
                  <div class="card insights-card insights-card-middle">
                      <div class="card-header">
                          <img src="https://linkedin-analytics.s3-eu-west-1.amazonaws.com/static/img/insights/education-small.jpg" class="img-responsive">
                          <p><b>Linkedin Analytics</b> <br>{{ companyCategory }} </p>

                      </div>
                      <div class="row row-comment">
                          {{ companyCategory }} by employee count:
                      </div>
                      <div class="chart">
                          <employees-chart  :chart-data="employeeCountData" :styles="chartStyles"></employees-chart>
                      </div>
                  </div>
              </div>
          </div>
          <div class="col-sm-3 col-md-3 col-lg-3 plain-element">
              <div class="card insights-card insights-card-narrow-right" id="tableSpecialities">
                  <div class="card-header">
                      <img src="https://linkedin-analytics.s3-eu-west-1.amazonaws.com/static/img/insights/education-small.jpg" class="img-responsive">
                      <p><b>Linkedin Analytics</b> <br>{{ companyCategory }}</p>
                  </div>
                  <div class="row row-comment">
                      {{ companyCategory }} by specialties:
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
                              <tr  v-for="(key, value, i) in specialties" :key="i">
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
import { apiService } from "@/common/api.service.js";
import FollowersChart from "@/common/FollowersChart.js";
import EmployeesChart from "@/common/EmployeesChart.js";
import TypesChart from "@/common/TypesChart.js";

let endpoint = "/api/education/";
export default {
  name: 'education',
  components: {
    FollowersChart,
    EmployeesChart,
    TypesChart,
  },
  data() {
    return {
      category: "",
      companyCategory: "",
      companyCount: null,
      oldestTenCompanies: [],
      specialties: {},
      followersCount: {},
      followersCountData: {},
      employeeCountData: {},
      companyTypesData: {},
      employeeCount: {},
      companyTypes: {},
    }
  },
  methods: {
    getSectorData() {
      apiService(endpoint)
        .then(data =>{
          this.companyCount = data.count;
          this.companyCategory = data.sector_strings[0];
          this.category = data.sector_strings[1];
          this.oldestTenCompanies = data.oldest_10_dict;
          this.specialties = data.spec_dict;
          this.followersCount = data.followers_dict;
          this.employeeCount = data.e_count_dict;
          this.companyTypes = data.type_dict;
          this.fillCompanyTypesChart();
          this.fillFollowersCountChart();
          this.fillEmployeeCountChart();
        })
    },
    fillFollowersCountChart() {
      var dataset = this.followersCount
      var dataLabels = Object.keys(dataset)
      var dataValues = Object.values(dataset)
      this.followersCountData = {
        labels: dataLabels,
        datasets: [
          {
            backgroundColor: ["#4e79a7", "#f28e2b"],
            data: dataValues
          }
        ]
      }
    },
    fillEmployeeCountChart() {
      var dataset = this.employeeCount
      var dataLabels = Object.keys(dataset)
      var dataValues = Object.values(dataset)
      this.employeeCountData = {
        labels: dataLabels,
        datasets: [
          {
            backgroundColor: ["#2b5b89","#356899", "#5789b6", "#7bb0d5", "#89bddc", "#90c3df", "#98c8e2", "#9ccae3", "#9ccae3"],
            data: dataValues
          }
        ]
      }
    },
    fillCompanyTypesChart() {
      var dataset = this.companyTypes
      var dataLabels = Object.keys(dataset)
      var dataValues = Object.values(dataset)
      this.companyTypesData = {
        labels: dataLabels,
        datasets: [
          {
            backgroundColor: ["#4e79a7","#f28e2b", "#e15759", "#76b7b2", "#59a14f", "#edc948"],
            data: dataValues
          }
        ]
      }
    }
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
    this.getSectorData();
    document.title = "Linkedin Analytics - Educational Institutions";
  }
};

</script>