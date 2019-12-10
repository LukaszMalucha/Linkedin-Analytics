<template>
<div class="row plain-element">
  <div class="row header">
      <div class="row">
          <div class="col-xs-2 col-sm-2 col-md-1 col-lg-2 text-right">
              <img src="@/assets/finance-medium.jpg" class="img responsive img-header">
          </div>

          <div class="col-xs-10 col-sm-10 col-md-11 col-lg-10">
              <div class="row summary">
                   <div class="box">
                      <h5>{{ companyCategory }} in Ireland </h5>
                      <a href="" class="btn-algorithm">View Companies</a>
                  </div>

                  <h6>Sector Companies: <b class="counter">{{ companyCount }}</b></h6>


              </div>
          </div>
      </div>
  </div>
  <div class="dashboard-cards">
      <div class="row row-cards">
          <div class="col-md-3 no-padding">
              <div class="row no-padding no-margin-bottom">
                  <div class="card insights-card">
                      <div class="card-header">
                          <img src="@/assets/finance-small.jpg" class="img-responsive">
                          <p><b>Linkedin Analytics</b> <br>{{ companyCategory }} </p>

                      </div>
                      <div class="row row-comment">
                          {{ companyCategory }} with the tradition:
                      </div>

                      <div class="row-image">
                          <div class="table-responsive">
                              <table class="table table-established">
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
              <div class="row no-padding">
                  <div class="card insights-card">
                      <div class="card-header">
                          <img src="@/assets/finance-small.jpg" class="img-responsive">
                          <p><b>Linkedin Analytics</b> <br>{{ companyCategory }} </p>
                      </div>
                      <div class="row row-comment">
                          {{ companyCategory }} by followers count:
                      </div>
                      <div class="chart-small">
                          <followers-chart  :chart-data="datacollection" :styles="myStyles"></followers-chart>
                      </div>
                  </div>
              </div>
          </div>

          <div class="col-md-6 no-padding">
              <div class="row no-padding">
                  <div class="card insights-card">
                      <div class="card-header">
                          <img src="@/assets/finance-small.jpg" class="img-responsive">
                          <p><b>Linkedin Analytics</b> <br>{{ companyCategory }} </p>

                      </div>
                      <div class="row row-comment">
                          {{ companyCategory }} by type:
                      </div>
                      <div class="chart">
                          <canvas id="typeChart"></canvas>
                      </div>
                  </div>
              </div>
              <div class="row no-padding">
                  <div class="card insights-card">
                      <div class="card-header">
                          <img src="@/assets/finance-small.jpg" class="img-responsive">
                          <p><b>Linkedin Analytics</b> <br>{{ companyCategory }} </p>

                      </div>
                      <div class="row row-comment">
                          {{ companyCategory }} by employee count:
                      </div>
                      <div class="chart">
                          <canvas id="ecountChart"></canvas>
                      </div>
                  </div>
              </div>
          </div>
          <div class="col-md-3 no-padding">
              <div class="card insights-card">
                  <div class="card-header">
                      <img src="@/assets/finance-small.jpg" class="img-responsive">
                      <p><b>Linkedin Analytics</b> <br>{{ companyCategory }}</p>
                  </div>
                  <div class="row row-comment">
                      {{ companyCategory }} business specialties:
                  </div>
                  <div class="row-image">
                      <div class="table-responsive">
                          <table class="table table-established table-long">
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

let endpoint = "/api/finance/";
export default {
  name: 'Finance',
  components: {
    FollowersChart
  },
  data() {
    return {
      companyCategory: "",
      companyCount: null,
      oldestTenCompanies: [],
      specialties: {},
      followersCount: {},
      datacollection: {},
    }
  },
  methods: {
    getSectorData() {
      apiService(endpoint)
        .then(data =>{
          this.companyCount = data.count;
          this.companyCategory = data.sector_strings[0];
          this.oldestTenCompanies = data.oldest_10_dict;
          this.specialties = data.spec_dict;
          this.followersCount = data.followers_dict;
          this.fillData();
          window.console.log(data)
        })
    },
    fillData() {
      var dataset = this.followersCount

      var dataLabels = Object.keys(dataset)

      var dataValues = Object.values(dataset)
      this.datacollection = {
        labels: dataLabels,
        datasets: [
          {
            backgroundColor: ["#4e79a7", "#f28e2b"],
            data: dataValues
          }
        ]
      }
    }
  },
  computed: {
    myStyles () {
      return {
        height: `100%`,
        position: 'relative'
      }
    }
  },
  created() {
    this.getSectorData();
    document.title = "Linkedin Analytics - Financial Companies";
  }
};

</script>
